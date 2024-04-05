import pathlib

import click

from rolodex import rolodex


@click.command()
@click.option("--display", "-d", "display_format", type=click.Choice(["json", "table"]))
@click.option(
    "--output",
    "-o",
    "output_file_path",
    type=click.Path(path_type=pathlib.Path),
)
@click.option("--add_record", "-a", "records", multiple=True, type=click.STRING)
@click.option("--filter", "-f", "filters", multiple=True)
@click.argument(
    "files",
    nargs=-1,
    type=click.Path(exists=True, path_type=pathlib.Path),
)
def cli(
    files: tuple[pathlib.Path],
    filters: tuple[str],
    records: tuple[str],
    output_file_path: pathlib.Path,
    display_format: str,
) -> None:
    rolo = rolodex.Rolodex()

    for file in files:
        rolo.load_from_file(file)

    rolo.add_records_from_string(records)

    for fi in filters:
        field, glob_pattern = fi.split("=")

        if field not in ["name", "address", "phone_number"]:
            raise click.UsageError("Field must be one of [name, address, phone_number]")

        # Since we won't be implementing input validation in this MMVP to get the correct types for "field",
        # we will choose to ignore the type error that is raised by the linter
        rolo = rolo.filter_records(field, glob_pattern)  # type: ignore[arg-type]

    if output_file_path:
        if output_file_path.suffix not in [".json", ".csv"]:
            raise click.UsageError(f"Unsupported output format specified: {output_file_path}")

        rolo.export_to_file(output_file_path)

    if display_format == "json":
        click.echo(rolo.format_as_json())
    elif display_format == "table":
        click.echo(rolo.format_as_table())
    elif not output_file_path:
        click.echo(rolo.format_as_json())


if __name__ == "__main__":
    cli()
