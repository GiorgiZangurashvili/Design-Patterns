from app.creature.creature import Creature
from app.fight.fight import Fight
from app.movement.crawl import Crawl
from app.movement.fly import Fly
from app.movement.hop import Hop
from app.movement.run import Run
from app.movement.walk import Walk
from app.printer.printer import Printer
from app.randomgenerator.random_generator import RandomGenerator
from app.state.initial_state import PredatorState, PreyState


class Simulation:
    @staticmethod
    def simulate(n: int, fight: Fight) -> None:
        count: int = 0
        for i in range(n):
            predator_st = PredatorState(RandomGenerator())
            Printer.print_characteristics(predator_st)
            prey_st = PreyState(RandomGenerator())
            Printer.print_characteristics(prey_st)
            predator_creature = Creature(
                predator_st,
                Fly(
                    predator_st,
                    Run(
                        predator_st,
                        Walk(predator_st, Hop(predator_st, Crawl(predator_st))),
                    ),
                ),
            )
            prey_creature = Creature(
                prey_st,
                Fly(prey_st, Run(prey_st, Walk(prey_st, Hop(prey_st, Crawl(prey_st))))),
            )

            while True:
                if predator_st.stamina <= predator_st.MIN_STAMINA:
                    print("Prey ran into infinity")
                    break
                if predator_st.location >= prey_st.location:
                    winner: bool = fight.fight(predator_st, prey_st)
                    if winner:
                        print("Some R-rated things have happened")
                        count += 1
                    else:
                        print("Prey ran into infinity")
                    break
                predator_creature.move()
                prey_creature.move()
        print(f"{count}/{n} times predator killed prey")
