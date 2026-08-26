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
LEDGER_URL = (
    "https://wcng30x0nvef.feishu.cn/base/"
    "KP9UbfeesaatN0sKe7Tc9JDDnFc?table=tblGvMJoDoqu5Xeb&view=vewnhIL5Fp"
)


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
        if LEDGER_URL not in text:
            fail(f"missing fund ledger link: {page.relative_to(ROOT)}")

    chinese = (ROOT / "README.md").read_text(encoding="utf-8")
    required_uses = [
        "专项黑客松举办赞助资金",
        "线下活动资金",
        "线上项目分享资金",
        "免费课程赞助资金",
        "项目治理资金",
        "内部重大贡献奖励资金",
    ]
    for item in required_uses:
        if item not in chinese:
            fail(f"missing fund use on homepage: {item}")


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
