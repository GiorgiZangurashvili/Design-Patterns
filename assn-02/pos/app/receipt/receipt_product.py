from dataclasses import dataclass


@dataclass
class ReceiptProduct:
    product_name: str
    units: int
    price: float
    total: float

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ReceiptProduct):
            return False
        return self.product_name == other.product_name
