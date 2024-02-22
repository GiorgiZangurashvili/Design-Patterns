from pos.app.prompt.prompt import AskForPrompt
from pos.app.types.report_type import ReportType


class ShouldMakeReport:
    @staticmethod
    def should_make_report(
        customer_number: int, report_num: int, report_type: ReportType
    ) -> bool:
        return customer_number % report_num == 0 and AskForPrompt.ask_for_report(
            report_type
        )
