from pos.app.printer.generic_printer import GenericPrinter
from pos.app.product.product import BaseProduct


class StoreInformationPrinter:
    @staticmethod
    def print_store_information(products: list[BaseProduct]) -> None:
        headers: list[str] = ["Product", "Price", "Batch size", "Discout"]
        rows: list[tuple[str, float, int, int]] = [
            (product.name, product.price, product.batch_size, product.discount)
            for product in products
        ]
        GenericPrinter.print_information(headers, rows)
