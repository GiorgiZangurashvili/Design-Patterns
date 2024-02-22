from dataclasses import dataclass, field
from typing import Self

from pos.app.product.product import BaseProduct
from pos.app.types.payment_type import PaymentType


@dataclass
class Customer:
    payment_type: PaymentType = PaymentType.CASH
    items: dict[BaseProduct, int] = field(default_factory=dict)


@dataclass
class CustomerBuilder:
    payment_type: PaymentType = PaymentType.CASH
    items: dict[BaseProduct, int] = field(default_factory=dict)

    def with_payment_method(self, payment_type: PaymentType) -> Self:
        self.payment_type = payment_type
        return self

    def with_items(self, items: dict[BaseProduct, int]) -> Self:
        self.items = items
        return self

    def build(self) -> Customer:
        return Customer(self.payment_type, self.items)
