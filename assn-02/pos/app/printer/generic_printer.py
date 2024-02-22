from typing import Any

from tabulate import tabulate


class GenericPrinter:
    @staticmethod
    def print_information(headers: list[str], rows: list[Any]) -> None:
        table = tabulate(rows, headers, tablefmt="pipe")
        print(table)
