import random
from dataclasses import dataclass


@dataclass
class BaseRandomGenerator:
    def generate_random_values(
        self,
        min_limbs: int,
        max_limbs: int,
        min_hp: int,
        max_hp: int,
        min_stamina: int,
        max_stamina: int,
        min_power: int,
        max_power: int,
        claws_strengths: list[int],
        teeth_strengths: list[int],
    ) -> list[int]:
        return []


@dataclass
class RandomGenerator(BaseRandomGenerator):
    def generate_random_values(
        self,
        min_limbs: int,
        max_limbs: int,
        min_hp: int,
        max_hp: int,
        min_stamina: int,
        max_stamina: int,
        min_power: int,
        max_power: int,
        claws_strengths: list[int],
        teeth_strengths: list[int],
    ) -> list[int]:
        number_of_wings = random.randint(min_limbs, max_limbs)
        number_of_legs = random.randint(min_limbs, max_limbs)
        health = random.randint(min_hp, max_hp)
        stamina = random.randint(min_stamina, max_stamina)
        power = random.randint(min_power, max_power)
        claws_strength = random.choice(claws_strengths)
        teeth_strength = random.choice(teeth_strengths)
        return [
            number_of_wings,
            number_of_legs,
            health,
            stamina,
            power,
            claws_strength,
            teeth_strength,
        ]
