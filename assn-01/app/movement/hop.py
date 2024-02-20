from dataclasses import dataclass, field

from app.movement.move import Move
from app.movement.no_move import NoMove
from app.state.initial_state import InitialState


@dataclass
class Hop:
    state: InitialState
    following: Move = field(default_factory=NoMove)

    REQUIRES_STAMINA: int = 20
    USES_STAMINA: int = 2
    REQUIRED_NUM_LEGS: int = 1
    SPEED: int = 3

    def move(self) -> None:
        if (
            self.state.stamina <= self.REQUIRES_STAMINA
            or self.state.number_of_legs < self.REQUIRED_NUM_LEGS
        ):
            self.following.move()
            return

        self.state.location += self.SPEED
        self.state.stamina -= self.USES_STAMINA
