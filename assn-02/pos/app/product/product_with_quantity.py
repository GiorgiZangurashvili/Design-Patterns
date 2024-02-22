from dataclasses import dataclass


@dataclass
class PosProductWithQuantity:
    product_name: str = ""
    sold_quantity: int = 0
