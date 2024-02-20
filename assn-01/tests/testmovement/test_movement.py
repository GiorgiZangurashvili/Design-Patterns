import copy

from app.creature.creature import Creature
from app.movement.crawl import Crawl
from app.movement.fly import Fly
from app.movement.hop import Hop
from app.movement.run import Run
from app.movement.walk import Walk
from app.randomgenerator.random_generator import RandomGenerator
from app.state.initial_state import PredatorState


def test_crawl_no_stamina(state: PredatorState) -> None:
    crawl = Crawl(state)
    state.stamina = 0
    creature = Creature(state, crawl)
    creature.move()
    assert state.location == 0


def test_crawl_with_stamina(state: PredatorState) -> None:
    crawl = Crawl(state)
    state.stamina = 1
    creature = Creature(state, crawl)
    creature.move()
    assert state.location == 1 and state.stamina == 0


def test_hop_no_stamina(state: PredatorState) -> None:
    hop = Hop(state)
    state.stamina = 20
    creature = Creature(state, hop)
    creature.move()
    assert state.location == 0


def test_hop_with_stamina_and_leg(state: PredatorState) -> None:
    hop = Hop(state)
    state.stamina = 21
    state.number_of_legs = 1
    creature = Creature(state, hop)
    creature.move()
    assert state.location == 3 and state.stamina == 19


def test_hop_with_stamina_and_no_leg(state: PredatorState) -> None:
    hop = Hop(state)
    state.stamina = 21
    state.number_of_legs = 0
    creature = Creature(state, hop)
    creature.move()
    assert state.location == 0 and state.stamina == 21


def test_walk_no_stamina(state: PredatorState) -> None:
    walk = Walk(state)
    state.stamina = 40
    creature = Creature(state, walk)
    creature.move()
    assert state.location == 0


def test_walk_with_stamina_and_legs(state: PredatorState) -> None:
    walk = Walk(state)
    state.stamina = 41
    state.number_of_legs = 2
    creature = Creature(state, walk)
    creature.move()
    assert state.location == 4 and state.stamina == 39


def test_walk_with_stamina_and_no_legs(state: PredatorState) -> None:
    walk = Walk(state)
    state.stamina = 41
    state.number_of_legs = 1
    creature = Creature(state, walk)
    creature.move()
    assert state.location == 0 and state.stamina == 41


def test_run_no_stamina(state: PredatorState) -> None:
    run = Run(state)
    state.stamina = 60
    creature = Creature(state, run)
    creature.move()
    assert state.location == 0


def test_run_with_stamina_and_legs(state: PredatorState) -> None:
    run = Run(state)
    state.stamina = 61
    state.number_of_legs = 2
    creature = Creature(state, run)
    creature.move()
    assert state.location == 6 and state.stamina == 57


def test_run_with_stamina_and_no_legs(state: PredatorState) -> None:
    run = Run(state)
    state.stamina = 61
    state.number_of_legs = 1
    creature = Creature(state, run)
    creature.move()
    assert state.location == 0 and state.stamina == 61


def test_fly_no_stamina(state: PredatorState) -> None:
    fly = Fly(state)
    state.stamina = 79
    creature = Creature(state, fly)
    creature.move()
    assert state.location == 0


def test_fly_with_stamina_and_wings(state: PredatorState) -> None:
    fly = Fly(state)
    state.stamina = 81
    state.number_of_wings = 2
    creature = Creature(state, fly)
    creature.move()
    assert state.location == 8 and state.stamina == 77


def test_fly_with_stamina_and_no_wings(state: PredatorState) -> None:
    fly = Fly(state)
    state.stamina = 81
    state.number_of_wings = 1
    creature = Creature(state, fly)
    creature.move()
    assert state.location == 0 and state.stamina == 81


if __name__ == "__main__":
    predator_st = PredatorState(RandomGenerator())
    test_crawl_no_stamina(copy.deepcopy(predator_st))
    test_crawl_with_stamina(copy.deepcopy(predator_st))
    test_hop_no_stamina(copy.deepcopy(predator_st))
    test_hop_with_stamina_and_leg(copy.deepcopy(predator_st))
    test_hop_with_stamina_and_no_leg(copy.deepcopy(predator_st))
    test_walk_no_stamina(copy.deepcopy(predator_st))
    test_walk_with_stamina_and_legs(copy.deepcopy(predator_st))
    test_walk_with_stamina_and_no_legs(copy.deepcopy(predator_st))
    test_run_no_stamina(copy.deepcopy(predator_st))
    test_run_with_stamina_and_legs(copy.deepcopy(predator_st))
    test_run_with_stamina_and_no_legs(copy.deepcopy(predator_st))
    test_fly_no_stamina(copy.deepcopy(predator_st))
    test_fly_with_stamina_and_wings(copy.deepcopy(predator_st))
    test_fly_with_stamina_and_no_wings(copy.deepcopy(predator_st))
