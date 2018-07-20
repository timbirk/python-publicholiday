import pytest
from click.testing import CliRunner
from publicholiday import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner, caplog):
    result = runner.invoke(cli.main)
    assert result.exit_code in (0, 1)
    assert caplog.text == ''


def test_cli_with_unknown_country(runner, caplog):
    result = runner.invoke(cli.main, ['--country', 'UNKNOWNCOUNTRY'])
    assert result.exception
    assert result.exit_code == 127
    assert 'Country: UNKNOWNCOUNTRY not found.' in caplog.text
