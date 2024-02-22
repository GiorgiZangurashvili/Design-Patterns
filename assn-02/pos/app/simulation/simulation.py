from pos.app.calculator.number_is_prime import NumberIsPrime
from pos.app.person.cashier import Cashier
from pos.app.person.cashier_manager import CashierManager
from pos.app.person.customer import Customer, CustomerBuilder
from pos.app.person.customer_at_pos import CustomerAtPos
from pos.app.posrandom.attribute_generator import RandomAttributeGenerator
from pos.app.printer.payment_printer import PaymentPrinter
from pos.app.printer.report_printer import ReportPrinter
from pos.app.prompt.should_make_report import ShouldMakeReport
from pos.app.repository.product_repository import PosProductRepository
from pos.app.repository.revenue_repository import PosRevenueRepository
from pos.app.repository.sales_repository import PosSalesRepository
from pos.app.types.report_type import ReportType


class PosSimulation:
    @staticmethod
    def simulate(num_shifts: int, x_report_num: int, z_report_num: int) -> None:
        cashier_manager: CashierManager = CashierManager(
            PosSalesRepository(), PosRevenueRepository()
        )

        for i in range(num_shifts):
            cashier: Cashier = cashier_manager.create_cashier()
            customer_number: int = 0
            while True:
                customer_number += 1
                customer: Customer = CustomerAtPos(
                    CustomerBuilder(), RandomAttributeGenerator()
                ).arrive(PosProductRepository())
                total_revenue: float = cashier.register_items(
                    customer.items, NumberIsPrime.is_prime(customer_number)
                )
                PaymentPrinter.print_payment(customer.payment_type)
                cashier.close_receipt()
                cashier.update_revenue(customer.payment_type.value, total_revenue)
                if ShouldMakeReport.should_make_report(
                    customer_number, x_report_num, ReportType.X
                ):
                    ReportPrinter.print_reports(
                        cashier.products_report, cashier.revenue_report
                    )
                elif ShouldMakeReport.should_make_report(
                    customer_number, z_report_num, ReportType.Z
                ):
                    cashier.end_shift()
                    break
