from __future__ import annotations

import sys
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from update_project_status import license_label, project_state, render_markdown  # noqa: E402


class ProjectStatusTest(unittest.TestCase):
    def test_license_labels(self) -> None:
        self.assertEqual(license_label(None), "未检测到")
        self.assertEqual(license_label({"spdx_id": "NOASSERTION"}), "自定义／未识别")
        self.assertEqual(license_label({"spdx_id": "MIT"}), "MIT")

    def test_project_state(self) -> None:
        self.assertEqual(project_state({"visibility": "public"}), "公开")
        self.assertEqual(project_state({"visibility": "private"}), "非公开")
        self.assertEqual(project_state({"visibility": "public", "archived": True}), "已归档")

    def test_render_has_no_contributor_identity_fields(self) -> None:
        markdown = render_markdown(
            {
                "checked_at": "2026-08-23T06:00:00Z",
                "projects": [
                    {
                        "repository": "powerycy/example",
                        "html_url": "https://github.com/powerycy/example",
                        "state": "公开",
                        "default_branch": "main",
                        "configured_default_branch": "main",
                        "pushed_at": "2026-08-20T00:00:00Z",
                        "license": "MIT",
                    }
                ],
            }
        )
        self.assertIn("powerycy/example", markdown)
        self.assertNotIn("贡献者 |", markdown)
        self.assertNotIn("contributor", markdown.lower())


if __name__ == "__main__":
    unittest.main()

