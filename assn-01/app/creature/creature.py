from dataclasses import dataclass, field

from app.movement.move import Move
from app.movement.no_move import NoMove
from app.state.initial_state import InitialState


@dataclass
class Creature:
    state: InitialState
    following: Move = field(default_factory=NoMove)

    def move(self) -> None:
        self.following.move()
