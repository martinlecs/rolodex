from __future__ import annotations

import csv
import fnmatch
import json
import sys
from pprint import pprint
from typing import Literal, TypedDict


class Record(TypedDict):
    name: str
    address: str
    phone_number: str


class Rolodex:
    def __init__(self, records: list[Record] | None = None):
        self.records: list[Record] = records or []

    def add_records(self, records: list[Record]) -> None:
        self.records.extend(records)

    # https://docs.python.org/3/library/fnmatch.html
    def filter_records(self, field: Literal["name", "address", "phone_number"], pattern: str) -> list[Record]:
        return [r for r in self.records if fnmatch.filter([r[field]], pattern)]

    def display(self):
        pprint(self.records)

    def display_as_table(self):
        pass

    def export_to_json(self, export_path: str) -> None:
        if export_path == "":
            # if no path is provided, just print json as is to screen
            sys.stdout.write(json.dumps(self.records))

        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(self.records, f, ensure_ascii=False, indent=4)

    def export_to_csv(self, export_path: str) -> None:
        if export_path == "":
            # if no path is provided, just print csv as is to screen
            sys.stdout.write(json.dumps(self.records))

        # https://docs.python.org/3/library/csv.html#csv.DictWriter
        with open(export_path, "w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["name", "address", "phoneumber"])
            writer.writerows(self.records)
