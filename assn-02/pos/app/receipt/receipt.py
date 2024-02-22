from dataclasses import dataclass, field
from typing import Protocol

from pos.app.calculator.revenue_calculator import RevenueCalculator
from pos.app.product.product import BaseProduct
from pos.app.receipt.receipt_product import ReceiptProduct
from pos.app.repository.product_repository import PosProductRepository


@dataclass
class Receipt(Protocol):
    def register_item(self, product: BaseProduct, quantity: int) -> ReceiptProduct:
        pass

    def clear(self) -> None:
        pass


@dataclass
class PosReceipt:
    items: list[ReceiptProduct] = field(default_factory=list)
    repository: PosProductRepository = field(default_factory=PosProductRepository)

    def register_item(self, product: BaseProduct, quantity: int) -> ReceiptProduct:
        receipt_product: ReceiptProduct = ReceiptProduct(
            product.name,
            quantity,
            product.price,
            RevenueCalculator.calculate(product.price, product.discount) * quantity,
        )

        for existing_item in self.items:
            if existing_item.__eq__(receipt_product):
                existing_item.units += quantity
                existing_item.total += receipt_product.total
                break
        else:
            self.items.append(receipt_product)

        return receipt_product

    def clear(self) -> None:
        self.items.clear()
