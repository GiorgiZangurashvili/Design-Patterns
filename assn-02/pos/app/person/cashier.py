from dataclasses import dataclass, field

from pos.app.payment.payment import BasePayment, CardPayment, CashPayment
from pos.app.printer.receipt_printer import ReceiptPrinter
from pos.app.product.product import BaseProduct
from pos.app.product.product_with_quantity import PosProductWithQuantity
from pos.app.receipt.receipt import PosReceipt
from pos.app.receipt.receipt_product import ReceiptProduct
from pos.app.repository.revenue_repository import BaseRevenueRepository
from pos.app.repository.sales_repository import BaseSalesRepository
from pos.app.types.payment_type import PaymentType


@dataclass
class Cashier:
    sales_repository: BaseSalesRepository
    revenue_repository: BaseRevenueRepository
    receipt: PosReceipt
    products_report: list[PosProductWithQuantity] = field(default_factory=list)
    revenue_report: list[BasePayment] = field(
        default_factory=lambda: [CashPayment(), CardPayment()]
    )

    CASH_PAYMENT_INDEX: int = 0
    CARD_PAYMENT_INDEX: int = 1
    PRIME_NUMBER_DISCOUNT: int = 17

    def register_items(self, products: dict[BaseProduct, int], is_prime: bool) -> float:
        total_revenue: float = 0.0
        for product, quantity in products.items():
            if is_prime:
                product.discount = self.PRIME_NUMBER_DISCOUNT
            receipt: ReceiptProduct = self.receipt.register_item(product, quantity)
            total_revenue += receipt.total
            self.sales_repository.update(PosProductWithQuantity(product.name, quantity))
            self.add_product_to_reports(product, quantity)
        ReceiptPrinter.print_receipt(self.receipt.items)
        return total_revenue

    def add_product_to_reports(self, product: BaseProduct, quantity: int) -> None:
        for existing_item in self.products_report:
            if existing_item.product_name == product.name:
                existing_item.sold_quantity += quantity
        else:
            self.products_report.append(PosProductWithQuantity(product.name, quantity))

    def update_revenue(self, payment_type: str, total_revenue: float) -> None:
        if payment_type == PaymentType.CASH.value:
            self.revenue_repository.update(CashPayment(revenue=total_revenue))
            self.revenue_report[self.CASH_PAYMENT_INDEX].revenue += total_revenue
        elif payment_type == PaymentType.CARD.value:
            self.revenue_repository.update(CardPayment(revenue=total_revenue))
            self.revenue_report[self.CARD_PAYMENT_INDEX].revenue += total_revenue

    def close_receipt(self) -> None:
        self.receipt.clear()

    def end_shift(self) -> None:
        print("Cashier ended shift")
