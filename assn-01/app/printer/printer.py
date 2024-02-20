from app.state.initial_state import InitialState, PredatorState


class Printer:
    @staticmethod
    def print_characteristics(state: InitialState) -> None:
        if isinstance(state, PredatorState):
            print("Predator's characteristics:")
        else:
            print("Prey's characteristics:")

        print(state)
        print()  # newline
