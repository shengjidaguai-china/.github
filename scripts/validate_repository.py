#!/usr/bin/env python3
"""Validate the community repository's public structure and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PROJECTS = {
    "shengjidaguai-china/BossHunter",
    "shengjidaguai-china/personal-homepage-skill",
    "shengjidaguai-china/goutoujunshi",
    "shengjidaguai-china/qiangshou-skill",
    "shengjidaguai-china/multi-model-review",
    "shengjidaguai-china/multi-style-image-generator",
}
def fail(message: str) -> None:
    raise AssertionError(message)


def check_config() -> None:
    config = json.loads((ROOT / "config/community.json").read_text(encoding="utf-8"))
    actual = {item["repository"] for item in config["projects"]}
    if actual != EXPECTED_PROJECTS:
        fail(f"project allowlist mismatch: {sorted(actual)}")


def check_public_homepages() -> None:
    pages = [
        ROOT / "README.md",
        ROOT / "README_EN.md",
        ROOT / "profile/README.md",
        ROOT / "profile/README_EN.md",
    ]
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if "README_SYNC:" not in text:
            fail(f"missing README sync marker: {page.relative_to(ROOT)}")
        if "multi-style-image-generator" not in text:
            fail(f"missing current project: {page.relative_to(ROOT)}")
        if "xiyouji-interactive-museum" in text:
            fail(f"removed project still present: {page.relative_to(ROOT)}")


def check_relative_links() -> None:
    missing: list[str] = []
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        targets = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)
        targets += re.findall(r'<img[^>]+src="([^"]+)"', text)
        for target in targets:
            clean = target.split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            if not (path.parent / clean).resolve().exists():
                missing.append(f"{path.relative_to(ROOT)} -> {clean}")
    if missing:
        fail("missing relative targets:\n" + "\n".join(missing))


def check_community_scope() -> None:
    removed_paths = [
        ROOT / "CONTRIBUTIONS.md",
        ROOT / "data/manual-contributions.json",
        ROOT / ".github/ISSUE_TEMPLATE/contribution.yml",
    ]
    existing = [str(path.relative_to(ROOT)) for path in removed_paths if path.exists()]
    if existing:
        fail("community contributor registry files returned: " + ", ".join(existing))


def main() -> int:
    check_config()
    check_public_homepages()
    check_relative_links()
    check_community_scope()
    print("Community repository validation: PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, json.JSONDecodeError) as exc:
        print(f"Community repository validation: FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
