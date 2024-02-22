from pos.app.product.product import PosProduct
from pos.app.receipt.receipt_product import ReceiptProduct


class PosProductMapper:
    @staticmethod
    def map(pos_product: PosProduct) -> ReceiptProduct:
        return ReceiptProduct(pos_product.name, 0, pos_product.price, 0)
