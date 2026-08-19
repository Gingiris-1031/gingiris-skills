"""Regression tests for the local Skill installer."""

import importlib.util
import os
import unittest
from pathlib import Path

SCRIPT_PATH = Path(__file__).with_name("sync-local.py")
SPEC = importlib.util.spec_from_file_location("sync_local", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load {SCRIPT_PATH}")
SYNC_LOCAL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC_LOCAL)


class RepositorySkillsDirTests(unittest.TestCase):
    """Protect clone-relative source discovery."""

    def test_resolves_skills_next_to_scripts_directory(self) -> None:
        self.assertEqual(
            SYNC_LOCAL.repository_skills_dir(
                os.path.join(
                    os.sep,
                    "workspace",
                    "other-clone",
                    "scripts",
                    "sync-local.py",
                )
            ),
            os.path.join(os.sep, "workspace", "other-clone", "skills"),
        )

    def test_configured_directory_belongs_to_current_clone(self) -> None:
        self.assertEqual(
            SYNC_LOCAL.MONO_SKILLS,
            str(SCRIPT_PATH.parent.parent / "skills"),
        )


if __name__ == "__main__":
    unittest.main()
