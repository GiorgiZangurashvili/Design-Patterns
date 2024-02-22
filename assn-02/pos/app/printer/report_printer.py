from pos.app.payment.payment import BasePayment
from pos.app.printer.generic_printer import GenericPrinter
from pos.app.product.product_with_quantity import PosProductWithQuantity
from pos.app.types.payment_type import PaymentType


class ReportPrinter:
    @staticmethod
    def print_reports(
        sales: list[PosProductWithQuantity], revenues: list[BasePayment]
    ) -> None:
        ReportPrinter.print_sales(sales)
        print()
        ReportPrinter.print_revenues(revenues)

    @staticmethod
    def print_sales(sales: list[PosProductWithQuantity]) -> None:
        headers: list[str] = ["Product", "Sales"]
        rows: list[tuple[str, int]] = [
            (sale.product_name, sale.sold_quantity) for sale in sales
        ]
        GenericPrinter.print_information(headers, rows)

    @staticmethod
    def print_revenues(revenues: list[BasePayment]) -> None:
        headers: list[str] = ["Payment", "Revenue"]
        rows: list[tuple[PaymentType, float]] = [
            (revenue.payment_method, revenue.revenue) for revenue in revenues
        ]
        GenericPrinter.print_information(headers, rows)
