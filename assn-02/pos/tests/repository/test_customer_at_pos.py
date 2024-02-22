import unittest

from pos.app.person.customer import Customer, CustomerBuilder
from pos.app.person.customer_at_pos import CustomerAtPos
from pos.app.posrandom.attribute_generator import TestAttributeGenerator
from pos.app.product.product import PosProduct
from pos.app.repository.product_repository import PosProductRepository
from pos.app.types.payment_type import PaymentType


class TestCustomerAtPos(unittest.TestCase):
    def test_customer_at_pos_builds(self) -> None:
        customer_at_pos: CustomerAtPos = CustomerAtPos(
            CustomerBuilder(), TestAttributeGenerator()
        )

        customer: Customer = customer_at_pos.arrive(PosProductRepository())
        items: dict[PosProduct, int] = {
            PosProduct(1, "Milk", 4.99, 1, 0): 1,
            PosProduct(3, "Beer", 5.69, 1, 0): 1,
        }

        self.assertEqual(customer.items, items)
        self.assertEqual(customer.payment_type, PaymentType.CASH)


if __name__ == "__main__":
    unittest.main()
