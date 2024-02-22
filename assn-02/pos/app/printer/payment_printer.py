from pos.app.types.payment_type import PaymentType


class PaymentPrinter:
    @staticmethod
    def print_payment(payment_type: PaymentType) -> None:
        print(f"Customer paid with {payment_type.value}")
