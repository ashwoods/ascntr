from ascntr.cli import cli


def test_simple_spec(cli_runner, result, sample):
    response = cli_runner.invoke(cli, ['16:10'],  input=sample)
    assert not response.exception
    assert str(response.output).rstrip() == str(result).rstrip()  # click outputs an additional newline to stout

