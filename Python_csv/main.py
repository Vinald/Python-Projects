import argparse
import csv
import sys
from pathlib import Path
from pprint import pprint

#!/usr/bin/env python3
"""
Simple CSV reader example.

Usage:
    python main.py path/to/file.csv        # prints rows as lists
    python main.py path/to/file.csv --dict # prints rows as dicts using header
"""


def read_csv_as_lists(path, encoding="utf-8"):
        with open(path, newline="", encoding=encoding) as fh:
                reader = csv.reader(fh)
                for row in reader:
                        yield row


def read_csv_as_dicts(path, encoding="utf-8"):
        with open(path, newline="", encoding=encoding) as fh:
                reader = csv.DictReader(fh)
                for row in reader:
                        yield row


def main():
        p = argparse.ArgumentParser(description="Read a CSV file and print rows.")
        p.add_argument("file", type=Path, help="Path to CSV file")
        p.add_argument("--dict", action="store_true", help="Use header and yield dicts (csv.DictReader)")
        p.add_argument("-n", "--limit", type=int, default=20, help="Max rows to print (default 20)")
        args = p.parse_args()

        if not args.file.exists():
                print(f"File not found: {args.file}", file=sys.stderr)
                sys.exit(2)

        reader = read_csv_as_dicts if args.dict else read_csv_as_lists
        for i, row in enumerate(reader(args.file)):
                if i >= args.limit:
                        print(f"... printed {args.limit} rows (use -n to change).")
                        break
                pprint(row)


if __name__ == "__main__":
        main()