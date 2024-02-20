from dataclasses import dataclass

from app.state.initial_state import PredatorState, PreyState


@dataclass
class SimpleFight:
    def fight(self, predator_st: PredatorState, prey_st: PreyState) -> bool:
        while True:
            prey_st.health -= predator_st.power
            if prey_st.health <= 0:
                return True
            predator_st.health -= prey_st.power
            if predator_st.health <= 0:
                return False
