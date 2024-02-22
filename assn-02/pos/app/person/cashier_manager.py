from dataclasses import dataclass

from pos.app.person.cashier import Cashier
from pos.app.receipt.receipt import PosReceipt
from pos.app.repository.revenue_repository import BaseRevenueRepository
from pos.app.repository.sales_repository import BaseSalesRepository


@dataclass
class CashierManager:
    sales_repository: BaseSalesRepository
    revenue_repository: BaseRevenueRepository

    def create_cashier(self) -> Cashier:
        return Cashier(self.sales_repository, self.revenue_repository, PosReceipt())
