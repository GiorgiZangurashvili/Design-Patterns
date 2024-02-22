import random
from dataclasses import dataclass
from typing import Protocol

from pos.app.product.product import BaseProduct, PosProduct
from pos.app.repository.product_repository import BaseProductRepository
from pos.app.types.payment_type import PaymentType


@dataclass
class AttributeGenerator(Protocol):
    def get_payment_type(self) -> PaymentType:
        pass

    def get_products(self, repository: BaseProductRepository) -> dict[BaseProduct, int]:
        pass


@dataclass
class RandomAttributeGenerator:
    def get_payment_type(self) -> PaymentType:
        return random.choice(list(PaymentType))

    def get_products(self, repository: BaseProductRepository) -> dict[BaseProduct, int]:
        MIN_QUANTITY: int = 1
        MAX_QUANTITY: int = 3
        products: list[BaseProduct] = repository.read_products()
        order_quantity: int = random.randint(MIN_QUANTITY, len(products))
        selected_products: list[BaseProduct] = random.sample(products, order_quantity)

        result: dict[BaseProduct, int] = {}

        for product in selected_products:
            random_quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)
            result[product] = random_quantity
            # print(f"PRODUCT: {product}")

        return result


@dataclass
class TestAttributeGenerator:
    def get_payment_type(self) -> PaymentType:
        return PaymentType.CASH

    def get_products(self, repository: BaseProductRepository) -> dict[BaseProduct, int]:
        return {
            PosProduct(1, "Milk", 4.99, 1, 0): 1,
            PosProduct(3, "Beer", 5.69, 1, 0): 1,
        }
