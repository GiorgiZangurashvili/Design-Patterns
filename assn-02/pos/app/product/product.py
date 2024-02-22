from dataclasses import dataclass


@dataclass
class BaseProduct:
    id: int
    name: str
    price: float
    batch_size: int
    discount: int

    def __init__(self) -> None:
        pass


@dataclass
class PosProduct(BaseProduct):
    id: int
    name: str
    price: float
    batch_size: int
    discount: int

    def __hash__(self) -> int:
        return hash(self.id)
