from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import management_prompt as m  # noqa: E402


class ManagementPromptTests(unittest.TestCase):
    def test_marker(self) -> None:
        body = "<!-- MANAGEMENT_DUTY_BEGIN -->x<!-- MANAGEMENT_DUTY_END -->"
        self.assertEqual(m.marked(body, "MANAGEMENT_DUTY"), "x")

    def test_prepare_uses_generic_stage(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            policy = root / "policy.md"
            policy.write_text(
                "<!-- PROFESSIONAL_DUTY_BEGIN -->执行专业任务<!-- PROFESSIONAL_DUTY_END -->",
                encoding="utf-8",
            )
            config = root / "config.json"
            config.write_text(
                json.dumps(
                    {
                        "works": {
                            "w": {
                                "stage": "OBSERVATION_ITERATION",
                            }
                        }
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            out = m.prepare(policy, config, "w", "professional", "任务正文", ["exact/ref"])
            self.assertEqual(out["stage"], "OBSERVATION_ITERATION")
            self.assertIn("执行专业任务", out["payload"])
            self.assertIn("exact/ref", out["payload"])
            self.assertEqual(len(out["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
