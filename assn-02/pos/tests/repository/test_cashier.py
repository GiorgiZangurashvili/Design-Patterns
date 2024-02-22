import unittest

from pos.app.person.cashier import Cashier
from pos.app.product.product import BaseProduct, PosProduct
from pos.app.receipt.receipt import PosReceipt
from pos.app.repository.revenue_repository import PosRevenueRepository
from pos.app.repository.sales_repository import PosSalesRepository


class TestCashier(unittest.TestCase):
    def test_register_items_with_prime_discount(self) -> None:
        cashier = Cashier(PosSalesRepository(), PosRevenueRepository(), PosReceipt())
        product: BaseProduct = PosProduct(1, "Milk", 4.99, 1, 0)

        products = {product: 2}
        total_revenue = cashier.register_items(products, is_prime=True)

        self.assertEqual(product.discount, cashier.PRIME_NUMBER_DISCOUNT)
        self.assertAlmostEqual(total_revenue, 8.2, delta=0.1)

    def test_register_items_with_regular_discount(self) -> None:
        cashier = Cashier(PosSalesRepository(), PosRevenueRepository(), PosReceipt())
        product: BaseProduct = PosProduct(1, "Milk", 4.99, 1, 5)

        products = {product: 1}
        total_revenue = cashier.register_items(products, is_prime=False)

        self.assertEqual(product.discount, 5)
        self.assertAlmostEqual(total_revenue, 4.74, delta=0.1)


if __name__ == "__main__":
    unittest.main()
