import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import homebrew_report


class HomebrewReportTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = pathlib.Path(self.directory.name)
        self.source = self.root / "input.elf"
        self.source.write_bytes(b"fixture")
        self.output = self.root / "output" / "app.exe"
        self.digest = homebrew_report.sha256(self.source)

    def run_report(self):
        return homebrew_report.relink(pathlib.Path("relinker.exe"), self.source, self.output, self.digest, 1)

    @patch("homebrew_report.subprocess.run")
    def test_checksum_mismatch_refuses_execution(self, run):
        self.source.write_bytes(b"modified")
        self.assertEqual(self.run_report()["stage"], "NOT_TESTED")
        run.assert_not_called()

    @patch("homebrew_report.subprocess.run")
    def test_missing_input_refuses_execution(self, run):
        self.source.unlink()
        self.assertEqual(self.run_report()["stage"], "NOT_TESTED")
        run.assert_not_called()

    @patch("homebrew_report.subprocess.run")
    def test_stale_output_refused(self, run):
        self.output.parent.mkdir()
        self.output.write_bytes(b"stale")
        with self.assertRaises(ValueError):
            self.run_report()
        run.assert_not_called()

    @patch("homebrew_report.subprocess.run")
    def test_success_without_artifacts_is_failure(self, run):
        run.return_value = subprocess.CompletedProcess([], 0, b"", b"")
        self.assertEqual(self.run_report()["stage"], "RELINK_FAILED")

    @patch("homebrew_report.subprocess.run")
    def test_success_is_only_relinked(self, run):
        def write_output(*args, **kwargs):
            self.output.write_bytes(b"MZ")
            self.output.with_suffix(".registry.json").write_text("{}")
            return subprocess.CompletedProcess([], 0, b"", b"")
        run.side_effect = write_output
        result = self.run_report()
        self.assertEqual(result["stage"], "RELINKED")
        self.assertFalse(result["runtime_tested"])
        self.assertNotIn("--autorun", result["command"])
        self.assertTrue(all(v == "NOT_TESTED" for v in result["checks"].values()))

    @patch("homebrew_report.subprocess.run")
    def test_failure_keeps_diagnostics(self, run):
        run.return_value = subprocess.CompletedProcess([], 2, b"", b"bad input\xff")
        result = self.run_report()
        self.assertEqual(result["stage"], "RELINK_FAILED")
        self.assertIn("bad input", result["stderr"])

    @patch("homebrew_report.subprocess.run", side_effect=subprocess.TimeoutExpired("relinker", 1))
    def test_timeout_is_not_success(self, run):
        result = self.run_report()
        self.assertEqual(result["stage"], "RELINK_FAILED")
        self.assertTrue(result["timed_out"])

    @patch("homebrew_report.subprocess.run", side_effect=FileNotFoundError("relinker unavailable"))
    def test_missing_tool_remains_not_tested(self, run):
        self.assertEqual(self.run_report()["stage"], "NOT_TESTED")


if __name__ == "__main__":
    unittest.main()
