from app import PredatorState
from app.creature.creature import Creature
from app.movement.crawl import Crawl
from app.movement.fly import Fly
from app.movement.hop import Hop
from app.movement.run import Run
from app.movement.walk import Walk
from app.randomgenerator.random_generator import RandomGenerator


def test_greedy_creature() -> None:
    state = PredatorState(RandomGenerator())
    state.stamina = 100
    state.number_of_legs = 2
    state.number_of_wings = 2
    creature = Creature(
        state,
        Fly(
            state,
            Run(
                state,
                Walk(state, Hop(state, Crawl(state))),
            ),
        ),
    )
    while state.stamina > 0:
        creature.move()
    assert state.location == 160


if __name__ == "__main__":
    test_greedy_creature()
