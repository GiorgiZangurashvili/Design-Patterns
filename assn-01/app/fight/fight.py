from typing import Protocol

from app.state.initial_state import PredatorState, PreyState


class Fight(Protocol):
    def fight(self, predator_st: PredatorState, prey_st: PreyState) -> bool:
        pass
