from typing import Protocol


class Move(Protocol):
    def move(self) -> None:
        pass
