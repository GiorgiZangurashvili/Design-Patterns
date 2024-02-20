import random
from dataclasses import dataclass

from app.randomgenerator.random_generator import BaseRandomGenerator


@dataclass
class InitialState:
    claws_strengths: list[int]
    teeth_strengths: list[int]

    MIN_NUM_LIMBS: int = 0
    MAX_NUM_LIMBS: int = 4

    MIN_HEALTH: int = 300
    MAX_HEALTH: int = 600

    MIN_STAMINA: int = 50
    MAX_STAMINA: int = 100

    MIN_INITIAL_POWER: int = 50
    MAX_INITIAL_POWER: int = 100

    def __init__(self, random_generator: BaseRandomGenerator) -> None:
        self.claws_strengths = [1, 2, 3, 4]
        self.teeth_strengths = [3, 6, 9]
        [
            self.number_of_wings,
            self.number_of_legs,
            self.health,
            self.stamina,
            self.power,
            self.claws_strength,
            self.teeth_strength,
        ] = random_generator.generate_random_values(
            self.MIN_NUM_LIMBS,
            self.MAX_NUM_LIMBS,
            self.MIN_HEALTH,
            self.MAX_HEALTH,
            self.MIN_STAMINA,
            self.MAX_STAMINA,
            self.MIN_INITIAL_POWER,
            self.MAX_INITIAL_POWER,
            self.claws_strengths,
            self.teeth_strengths,
        )
        self.power *= self.claws_strength
        self.power += self.teeth_strength
        self.location = 0

    def __str__(self) -> str:
        return f"""Number of Wings: {self.number_of_wings},
            Number of Legs: {self.number_of_legs},
            Claws Strength: {self.claws_strength},
            Teeth Strength: {self.teeth_strength},
            Health: {self.health},
            Stamina: {self.stamina},
            Power: {self.power},
            Location: {self.location}"""


@dataclass
class PredatorState(InitialState):
    def __init__(self, random_generator: BaseRandomGenerator) -> None:
        super().__init__(random_generator)
        self.location = 0


@dataclass
class PreyState(InitialState):
    MIN_LOCATION: int = 0
    MAX_LOCATION: int = 1000

    def __init__(self, random_generator: BaseRandomGenerator) -> None:
        super().__init__(random_generator)
        self.location = random.randint(self.MIN_LOCATION, self.MAX_LOCATION)
