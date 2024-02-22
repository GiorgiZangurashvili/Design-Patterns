import unittest

from pos.app.product.product import PosProduct
from pos.app.receipt.receipt import PosReceipt
from pos.app.receipt.receipt_product import ReceiptProduct


class TestReceipt(unittest.TestCase):
    def test_register_item_new_product(self) -> None:
        product: PosProduct = PosProduct(1, "Milk", 4.99, 1, 0)
        receipt: PosReceipt = PosReceipt()

        receipt_product: ReceiptProduct = receipt.register_item(product, 2)

        self.assertEqual(receipt_product, ReceiptProduct("Milk", 2, 4.99, 9.98))
        self.assertEqual(receipt.items, [ReceiptProduct("Milk", 2, 4.99, 9.98)])

    def test_register_item_existing_product(self) -> None:
        product: PosProduct = PosProduct(1, "Milk", 4.99, 1, 0)
        receipt: PosReceipt = PosReceipt([ReceiptProduct("Milk", 2, 4.99, 9.98)])

        receipt_product: ReceiptProduct = receipt.register_item(product, 2)

        self.assertEqual(receipt_product, ReceiptProduct("Milk", 2, 4.99, 9.98))
        self.assertEqual(receipt.items, [ReceiptProduct("Milk", 4, 4.99, 19.96)])


if __name__ == "__main__":
    unittest.main()
