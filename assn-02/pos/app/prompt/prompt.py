from pos.app.types.report_type import ReportType


class AskForPrompt:
    @staticmethod
    def ask_for_report(report_type: ReportType) -> bool:
        user_input = input(
            f"Do you want to make the {report_type.value} report? (y/n): "
        ).lower()
        return user_input == "y"
