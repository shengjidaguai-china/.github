#!/usr/bin/env python3
"""Refresh public project metadata without collecting contributor identities."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class GitHubAPI:
    def __init__(self, token: str | None = None) -> None:
        self.token = token

    def get_repository(self, repository: str) -> dict[str, Any]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "level-up-open-source-project-status",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = urllib.request.Request(
            f"https://api.github.com/repos/{repository}", headers=headers
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"GitHub API {exc.code} for repository {repository}: {body}"
            ) from exc
        if not isinstance(payload, dict):
            raise RuntimeError(f"Unexpected GitHub response for {repository}")
        return payload


def license_label(license_data: Any) -> str:
    if not isinstance(license_data, dict):
        return "未检测到"
    spdx = license_data.get("spdx_id")
    if not spdx:
        return "未检测到"
    if spdx == "NOASSERTION":
        return "自定义／未识别"
    return str(spdx)


def project_state(payload: dict[str, Any]) -> str:
    if payload.get("disabled"):
        return "已停用"
    if payload.get("archived"):
        return "已归档"
    if payload.get("visibility") != "public":
        return "非公开"
    return "公开"


def collect_status(config: dict[str, Any], api: GitHubAPI) -> dict[str, Any]:
    projects: list[dict[str, Any]] = []
    for item in config["projects"]:
        repository = str(item["repository"])
        payload = api.get_repository(repository)
        projects.append(
            {
                "repository": repository,
                "html_url": str(payload["html_url"]),
                "state": project_state(payload),
                "default_branch": str(payload.get("default_branch") or ""),
                "configured_default_branch": str(item["default_branch"]),
                "pushed_at": payload.get("pushed_at"),
                "updated_at": payload.get("updated_at"),
                "license": license_label(payload.get("license")),
            }
        )
    return {
        "checked_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "projects": projects,
    }


def escape_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_markdown(status: dict[str, Any]) -> str:
    checked_at = str(status["checked_at"])
    lines = [
        "<!-- GENERATED: scripts/update_project_status.py; manual edits may be overwritten -->",
        "",
        "# 收录项目状态",
        "",
        "本页面每月核对一次已收录仓库的公开状态、默认分支、最后推送时间和 GitHub 检测到的许可证。贡献署名和贡献者页面由各项目独立维护。",
        "",
        f"最近检查：`{checked_at}`",
        "",
        "| 项目 | 状态 | 默认分支 | 最后推送 | GitHub 许可证识别 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for project in status["projects"]:
        repository = escape_cell(project["repository"])
        branch = escape_cell(project["default_branch"])
        configured = escape_cell(project["configured_default_branch"])
        if branch != configured:
            branch = f"{branch}（配置为 {configured}）"
        pushed_at = escape_cell(project.get("pushed_at") or "无公开记录")
        lines.append(
            "| "
            + " | ".join(
                [
                    f"[{repository}]({project['html_url']})",
                    escape_cell(project["state"]),
                    f"`{branch}`",
                    pushed_at,
                    escape_cell(project["license"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "GitHub 显示“自定义／未识别”时，以仓库实际 `LICENSE` 文件为准。人工确认的范围和许可证说明见 [`COMMUNITY_PROJECTS.md`](./COMMUNITY_PROJECTS.md)。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config/community.json")
    parser.add_argument("--output-data", default="data/project-status.json")
    parser.add_argument("--output-markdown", default="PROJECT_STATUS.md")
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    api = GitHubAPI(os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"))
    status = collect_status(config, api)
    Path(args.output_data).write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    Path(args.output_markdown).write_text(render_markdown(status), encoding="utf-8")
    print(datetime.now(timezone.utc).strftime("%Y-%m"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
