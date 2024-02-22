import sqlite3
from sqlite3 import Cursor
from typing import Protocol, Tuple

from pos.app.payment.payment import BasePayment, CardPayment, CashPayment
from pos.app.types.payment_type import PaymentType


class BaseRevenueRepository(Protocol):
    def create(self, payment: BasePayment) -> None:
        pass

    def read(self, payment_name: str) -> BasePayment:
        pass

    def read_revenues(self) -> list[BasePayment]:
        pass

    def update(self, payment: BasePayment) -> None:
        pass

    def delete(self, payment_name: str) -> None:
        pass


def fetch_revenue_row(row: Tuple[str, float]) -> BasePayment:
    if row[0] == PaymentType.CARD.value:
        return CardPayment(revenue=row[1])
    return CashPayment(revenue=row[1])


class PosRevenueRepository(BaseRevenueRepository):
    def __init__(self, db_file: str = "POS.db"):
        self.conn = sqlite3.connect(db_file)

    def create(self, payment: BasePayment) -> None:
        pass

    def read(self, payment_name: str) -> BasePayment:
        cursor: Cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM revenues WHERE payment_method = ?", (payment_name,)
        )
        row = cursor.fetchone()
        return fetch_revenue_row(row)

    def read_revenues(self) -> list[BasePayment]:
        cursor: Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM revenues")
        rows = cursor.fetchall()

        revenues: list[BasePayment] = []
        for row in rows:
            revenues.append(fetch_revenue_row(row))
        return revenues

    def update(self, payment: BasePayment) -> None:
        persisted_revenue: BasePayment = self.read(payment.payment_method.value)
        cursor: Cursor = self.conn.cursor()
        update_query: str = "UPDATE revenues SET revenue = ? WHERE payment_method = ?"
        cursor.execute(
            update_query,
            (persisted_revenue.revenue + payment.revenue, payment.payment_method.value),
        )
        self.conn.commit()

    def delete(self, payment_name: str) -> None:
        pass
