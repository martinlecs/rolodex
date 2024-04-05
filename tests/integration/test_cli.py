from click.testing import CliRunner

from rolodex.cli import cli


def test_cli_works():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            # load files
            "tests/integration/data/test1.csv",
            "tests/integration/data/test2.json",
            # apply filter
            "-f",
            "name=*3",
            # add record
            "-a",
            "'mart3,asdadada asdasd asdsadsa asd,12321321'",
            # apply another filter
            "-f",
            "address=*ay*",
            # print results to screen as nicely formatted json
            "-d",
            "json",
        ],
    )

    assert result.exit_code == 0
    assert (
        result.output
        == '[\n    {\n        "name": "Mart1n L3",\n        "address": "42 Eallaby Day Sodney",\n        "phone_number": "21321321302"\n    },\n    {\n        "name": "M4rtjn l3",\n        "address": "91 Eastase Say Brosbin",\n        "phone_number": "12310192130"\n    }\n]\n'  # noqa: E501
    )
