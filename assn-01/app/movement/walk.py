from dataclasses import dataclass, field

from app.movement.move import Move
from app.movement.no_move import NoMove
from app.state.initial_state import InitialState


@dataclass
class Walk:
    state: InitialState
    following: Move = field(default_factory=NoMove)

    REQUIRES_STAMINA: int = 40
    USES_STAMINA: int = 2
    REQUIRED_NUM_LEGS: int = 2
    SPEED: int = 4

    def move(self) -> None:
        if (
            self.state.stamina <= self.REQUIRES_STAMINA
            or self.state.number_of_legs < self.REQUIRED_NUM_LEGS
        ):
            self.following.move()
            return None

        self.state.location += self.SPEED
        self.state.stamina -= self.USES_STAMINA
