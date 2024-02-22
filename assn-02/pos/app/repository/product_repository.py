import sqlite3
from sqlite3 import Cursor
from typing import Protocol

from pos.app.product.product import BaseProduct, PosProduct


class BaseProductRepository(Protocol):
    def create(self, product: BaseProduct) -> None:
        pass

    def read(self, product_id: int) -> BaseProduct:
        pass

    def read_products(self) -> list[BaseProduct]:
        pass

    def update(self, product: BaseProduct) -> None:
        pass

    def delete(self, product_name: str) -> None:
        pass


class PosProductRepository:
    def __init__(self, db_file: str = "POS.db"):
        self.conn = sqlite3.connect(db_file)

    def create(self, product: BaseProduct) -> None:
        pass

    def read(self, product_id: int) -> BaseProduct:
        cursor: Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        return PosProduct(*row)

    def read_products(self) -> list[BaseProduct]:
        cursor: Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        products: list[BaseProduct] = []
        for row in rows:
            product = PosProduct(*row)
            products.append(product)
        return products

    def update(self, product: BaseProduct) -> None:
        pass

    def delete(self, product_name: str) -> None:
        pass
