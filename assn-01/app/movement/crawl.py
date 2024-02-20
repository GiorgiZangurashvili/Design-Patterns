from dataclasses import dataclass, field

from app.movement.move import Move
from app.movement.no_move import NoMove
from app.state.initial_state import InitialState


@dataclass
class Crawl(Move):
    state: InitialState
    following: Move = field(default_factory=NoMove)

    REQUIRES_STAMINA: int = 0
    USES_STAMINA: int = 1
    SPEED: int = 1

    def move(self) -> None:
        if self.state.stamina <= self.REQUIRES_STAMINA:
            self.following.move()
            return

        self.state.location += self.SPEED
        self.state.stamina -= self.USES_STAMINA
