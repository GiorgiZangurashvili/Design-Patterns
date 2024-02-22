from typer import Typer

from pos.app.payment.payment import BasePayment
from pos.app.printer.report_printer import ReportPrinter
from pos.app.printer.store_information_printer import StoreInformationPrinter
from pos.app.product.product import BaseProduct
from pos.app.product.product_with_quantity import PosProductWithQuantity
from pos.app.repository.product_repository import PosProductRepository
from pos.app.repository.revenue_repository import PosRevenueRepository
from pos.app.repository.sales_repository import PosSalesRepository
from pos.app.simulation.simulation import PosSimulation

cli = Typer()


@cli.command("simulate")
def simulate(num_shifts: int, x_report_num: int, z_report_num: int) -> None:
    PosSimulation.simulate(num_shifts, x_report_num, z_report_num)


@cli.command("list")
def print_store_information() -> None:
    products_repository: PosProductRepository = PosProductRepository()
    products: list[BaseProduct] = products_repository.read_products()
    StoreInformationPrinter.print_store_information(products)


@cli.command("report")
def print_reports() -> None:
    sales_repository: PosSalesRepository = PosSalesRepository()
    sales: list[PosProductWithQuantity] = sales_repository.read_products_with_quantity()
    revenues_repository: PosRevenueRepository = PosRevenueRepository()
    revenues: list[BasePayment] = revenues_repository.read_revenues()
    ReportPrinter.print_reports(sales, revenues)
