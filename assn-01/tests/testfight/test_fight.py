from app.fight.fight import Fight
from app.fight.simple_fight import SimpleFight
from app.randomgenerator.random_generator import RandomGenerator
from app.state.initial_state import PredatorState, PreyState


def test_simple_fight_predator_win(fight: Fight) -> None:
    predator_st = PredatorState(RandomGenerator())
    prey_st = PreyState(RandomGenerator())

    predator_st.power = 200
    prey_st.power = 100
    predator_st.health = 800
    prey_st.health = 500

    assert fight.fight(predator_st, prey_st)


def test_simple_fight_prey_win(fight: Fight) -> None:
    predator_st = PredatorState(RandomGenerator())
    prey_st = PreyState(RandomGenerator())

    predator_st.power = 100
    prey_st.power = 200
    predator_st.health = 400
    prey_st.health = 500

    assert not fight.fight(predator_st, prey_st)


if __name__ == "__main__":
    test_simple_fight_predator_win(SimpleFight())
    test_simple_fight_prey_win(SimpleFight())
