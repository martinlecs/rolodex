from __future__ import annotations

import csv
import fnmatch
import json
import sys
from typing import Literal, TypedDict

from tabulate import tabulate


class Record(TypedDict):
    name: str
    address: str
    phone_number: str


class Rolodex:
    def __init__(self, records: list[Record] | None = None):
        self.records: list[Record] = records or []

    def add_records(self, records: list[Record]) -> None:
        self.records.extend(records)

    def filter_records(self, field: Literal["name", "address", "phone_number"], pattern: str) -> list[Record]:
        """Filter records using Unix shell-style wildcards on a specfic field.

        Syntax details: https://docs.python.org/3/library/fnmatch.html
        """
        return [r for r in self.records if fnmatch.filter([r[field]], pattern)]

    def display_as_json(self) -> None:
        sys.stdout.write(json.dumps(self.records, indent=4))

    def display_as_table(self) -> None:
        sys.stdout.write(tabulate(self.records, headers="keys"))

    def export_to_json(self, export_path: str) -> None:
        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=4)

    def export_to_csv(self, export_path: str) -> None:
        with open(export_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile,
                delimiter=",",
                quotechar="|",
                quoting=csv.QUOTE_MINIMAL,
                fieldnames=["name", "address", "phone_number"],
            )
            writer.writeheader()
            writer.writerows(self.records)
