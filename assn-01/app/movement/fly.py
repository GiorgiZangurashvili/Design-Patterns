from dataclasses import dataclass, field

from app.movement.move import Move
from app.movement.no_move import NoMove
from app.state.initial_state import InitialState


@dataclass
class Fly:
    state: InitialState
    following: Move = field(default_factory=NoMove)

    REQUIRED_STAMINA: int = 80
    USES_STAMINA: int = 4
    REQUIRED_NUM_WINGS: int = 2
    SPEED: int = 8

    def move(self) -> None:
        if (
            self.state.number_of_wings < self.REQUIRED_NUM_WINGS
            or self.state.stamina <= self.REQUIRED_STAMINA
        ):
            self.following.move()
            return

        self.state.stamina -= self.USES_STAMINA
        self.state.location += self.SPEED
