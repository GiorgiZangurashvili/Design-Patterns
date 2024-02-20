from simulation import Simulation

from app.fight.simple_fight import SimpleFight

if __name__ == "__main__":
    Simulation.simulate(100, SimpleFight())
