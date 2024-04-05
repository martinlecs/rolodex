from __future__ import annotations

import csv
import fnmatch
import json
from typing import TYPE_CHECKING, Literal, TypedDict

from tabulate import tabulate

if TYPE_CHECKING:
    import pathlib


class Record(TypedDict):
    name: str
    address: str
    phone_number: str


FilterFieldType = Literal["name", "address", "phone_number"]


class Rolodex:
    def __init__(self, records: list[Record] | None = None):
        self.records: list[Record] = records or []

    def add_records_from_dicts(self, records: list[Record]) -> None:
        self.records.extend(records)

    def add_records_from_string(self, records: list[str] | tuple[str]) -> None:
        converted_records: list[Record] = []
        for r in records:
            name, address, phone_number = r.split(",")
            converted_records.append({"name": name, "address": address, "phone_number": phone_number})

        self.add_records_from_dicts(converted_records)

    def filter_records(self, field: FilterFieldType, pattern: str) -> Rolodex:
        """Filter records using Unix shell-style wildcards on a specfic field.

        Returns a new instance of Rolodex containing the filtered records. Allows for filter chaining.

        Glob syntax details: https://docs.python.org/3/library/fnmatch.html
        """
        return Rolodex([r for r in self.records if fnmatch.filter([r[field]], pattern)])

    def format_as_json(self) -> str:
        return json.dumps(self.records, indent=4)

    def format_as_table(self) -> str:
        return tabulate(self.records, headers="keys")

    def export_to_json(self, export_path: pathlib.Path) -> None:
        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=4)

    def export_to_csv(self, export_path: pathlib.Path) -> None:
        with open(export_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                delimiter=",",
                quoting=csv.QUOTE_MINIMAL,
                fieldnames=["name", "address", "phone_number"],
            )
            writer.writeheader()
            writer.writerows(self.records)

    def export_to_file(self, export_file_path: pathlib.Path) -> None:
        if (file_format := export_file_path.suffix) == ".csv":
            self.export_to_csv(export_file_path)
        elif file_format == ".json":
            self.export_to_json(export_file_path)

    def load_from_csv(self, file_path: pathlib.Path) -> None:
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            records: list[Record] = [{"name": r[0], "address": r[1], "phone_number": r[2]} for r in reader]
            self.add_records_from_dicts(records)

    def load_from_json(self, file_path: pathlib.Path) -> None:
        with open(file_path) as jsonfile:
            self.add_records_from_dicts(json.load(jsonfile))

    def load_from_file(self, file_path: pathlib.Path) -> None:
        if (ext := file_path.suffix) == ".csv":
            self.load_from_csv(file_path)
        elif ext == ".json":
            self.load_from_json(file_path)
        else:
            raise ValueError(f"Unhandled file type: {file_path}")
