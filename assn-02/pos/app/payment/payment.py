from dataclasses import dataclass

from pos.app.types.payment_type import PaymentType


@dataclass
class BasePayment:
    payment_method: PaymentType = PaymentType.CASH
    revenue: float = 0.0

    def __init__(self) -> None:
        pass


@dataclass
class CashPayment(BasePayment):
    payment_method: PaymentType = PaymentType.CASH
    revenue: float = 0.0


@dataclass
class CardPayment(BasePayment):
    payment_method: PaymentType = PaymentType.CARD
    revenue: float = 0.0
