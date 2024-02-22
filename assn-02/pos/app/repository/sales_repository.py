import sqlite3
from sqlite3 import Cursor
from typing import Protocol

from pos.app.product.product_with_quantity import PosProductWithQuantity


class BaseSalesRepository(Protocol):
    def create(self, product_with_quantity: PosProductWithQuantity) -> None:
        pass

    def read(self, product_name: str) -> PosProductWithQuantity:
        pass

    def read_products_with_quantity(self) -> list[PosProductWithQuantity]:
        pass

    def update(self, product_with_quantity: PosProductWithQuantity) -> None:
        pass

    def delete(self, product_name: str) -> None:
        pass


class PosSalesRepository(BaseSalesRepository):
    def __init__(self, db_file: str = "POS.db") -> None:
        self.conn = sqlite3.connect(db_file)

    def create(self, product_with_quantity: PosProductWithQuantity) -> None:
        pass

    def read(self, product_name: str) -> PosProductWithQuantity:
        cursor: Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM sales WHERE product_name = ?", (product_name,))
        row = cursor.fetchone()
        return PosProductWithQuantity(*row)

    def read_products_with_quantity(self) -> list[PosProductWithQuantity]:
        cursor: Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM sales")
        rows = cursor.fetchall()

        sales: list[PosProductWithQuantity] = []
        for row in rows:
            sale = PosProductWithQuantity(*row)
            sales.append(sale)
        return sales

    def update(self, product_with_quantity: PosProductWithQuantity) -> None:
        persisted_sale: PosProductWithQuantity = self.read(
            product_with_quantity.product_name
        )
        cursor: Cursor = self.conn.cursor()
        update_query: str = "UPDATE sales SET sold_quantity = ? WHERE product_name = ?"
        cursor.execute(
            update_query,
            (
                persisted_sale.sold_quantity + product_with_quantity.sold_quantity,
                product_with_quantity.product_name,
            ),
        )
        self.conn.commit()

    def delete(self, product_name: str) -> None:
        pass
