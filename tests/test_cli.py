import subprocess
import pytest

CLI_FILE = "bletchley/cli.py"  # Update this path if cli.py is located elsewhere.

def run_cli_command(args):
    """Run the CLI file with the given arguments and return the result."""
    result = subprocess.run(
        ["python", CLI_FILE] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result

def test_cli_help():
    """Test that the CLI displays the help message."""
    result = run_cli_command(["--help"])
    assert result.returncode == 0, f"Help command failed: {result.stderr}"
    assert "Usage:" in result.stdout, "Help message not displayed correctly"

def test_cli_version():
    """Test that the CLI displays the version."""
    result = run_cli_command(["--version"])
    assert result.returncode == 0, f"Version command failed: {result.stderr}"
    assert "1.0.0" in result.stdout, "Version number not displayed correctly"

@pytest.mark.parametrize("input_args,expected_output", [
    (["command1"], "Expected output for command1"),
    (["command2", "--option", "value"], "Expected output for command2 with option"),
])
def test_cli_commands(input_args, expected_output):
    """Test various CLI commands and their outputs."""
    result = run_cli_command(input_args)
    assert result.returncode == 0, f"CLI command {input_args} failed: {result.stderr}"
    assert expected_output in result.stdout, f"Unexpected output for {input_args}: {result.stdout}"

def test_cli_invalid_command():
    """Test that an invalid command returns an error."""
    result = run_cli_command(["invalid-command"])
    assert result.returncode != 0, "Invalid command should return a non-zero exit code"
    assert "Error:" in result.stderr, "Error message not displayed for invalid command"
