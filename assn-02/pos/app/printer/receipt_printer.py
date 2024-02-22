from pos.app.printer.generic_printer import GenericPrinter
from pos.app.receipt.receipt_product import ReceiptProduct


class ReceiptPrinter:
    @staticmethod
    def print_receipt(receipt_products: list[ReceiptProduct]) -> None:
        headers: list[str] = ["Product", "Units", "Price", "Total"]
        rows: list[tuple[str, int, float, float]] = [
            (product.product_name, product.units, product.price, product.total)
            for product in receipt_products
        ]
        GenericPrinter.print_information(headers, rows)
