import pytest

from click.testing import CliRunner

# from hauberk import hauberk
from hauberk import cli


# @pytest.mark.xfail
def test_command_line_interface(tmpdir):
    """Test the CLI."""

    p = tmpdir.mkdir("inputs").join("input.yaml")
    p.write("test: other")
    runner = CliRunner()
    result = runner.invoke(cli.main, [str(p)])
    assert result.exit_code == 0

    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert 'Show this message and exit.' in help_result.output

def test_cli_bad_log_level(tmpdir):

    p = tmpdir.mkdir("inputs").join("input.yaml")
    p.write("test: other")
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--log-level', 'asdf', str(p)])
    assert result.exit_code != 0


