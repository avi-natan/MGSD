from board import Board
from simulation import Simulation
from agent import Agent
import consts

from typing import List
from typing import Tuple

def test_empty_constructors() -> None:
    print("""
#######################################################
#             Testing empty constructors              #
#######################################################
    """)
    b0: Board = Board()
    a0: Agent = Agent()
    s0: Simulation = Simulation()

    b0.summary()
    a0.summary()
    s0.summary()

    b0.visualize()
    s0.visualize()

def test_board_constructors() -> None:
    print("""
#######################################################
#             Testing board constructors              #
#######################################################
    """)

    print('Empty Constructor:')
    b0: Board = Board()
    b0.summary()
    b0.visualize()

    print('Custom Constructor:')
    b1: Board = Board(name='custom_board', width=12, height=12, critical_areas=[((4, 4), (8, 8))])
    b1.summary()
    b1.visualize()


def test_agent_constructors() -> None:
    print("""
#######################################################
#             Testing agent constructors              #
#######################################################
    """)
    print('Empty Constructor:')
    a0: Agent = Agent()
    a0.summary()

    print('Custom Constructor:')
    a1: Agent = Agent(name='custom_agent', color=(0.7, 0.7, 0.7), is_faulty=True)
    a1.summary()


def test_simulation_constructors() -> None:
    print("""
#######################################################
#          Testing simulation constructors            #
#######################################################
    """)
    print('Empty Constructor:')
    s0: Simulation = Simulation()
    s0.summary()
    s0.visualize()

    print('Custom Constructor:')
    b1: Board = Board(name='custom_board', width=12, height=12, critical_areas=[((3, 3), (5, 5))])
    p1: List[List[Tuple[int, int]]] = [[(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
                                       [(11, 11), (11, 10), (10, 10), (9, 10), (9, 9)]]
    a11: Agent = Agent(name='custom_agent_1', is_faulty=False)
    a12: Agent = Agent(name='custom_agent_2', is_faulty=True)
    s1: Simulation = Simulation(name='custom_simulation', board=b1, plans=p1, agents=[a11, a12])
    s1.summary()
    s1.visualize()


def test_simulation_agent_colors() -> None:
    print("""
#######################################################
#          Testing simulation agent colors            #
#######################################################
    """)
    b: Board = Board(width=12, height=12, critical_areas=[((3, 3), (5, 5))])
    s: Simulation = Simulation(board=b)
    s.summary()
    s.visualize()


def test_custom_scenarios_creation() -> None:
    print("""
#######################################################
#          Testing custom scenarios creation          #
#######################################################
    """)
    agents: List[Agent] = [Agent(name='a'+str(i), is_faulty=(i % 3 == 0)) for i in list(range(6))]
    for a in agents:
        a.summary()

    b0: Board = Board(name='Intersection', width=12, height=12, critical_areas=[((4, 4), (8, 8))])
    b0.summary()
    b0.visualize()
    plans0: List[List[Tuple[int, int]]] = consts.custom_plans_intersection
    s0: Simulation = Simulation(name='Sim Intersection', board=b0, plans=plans0, agents=agents)
    s0.summary()
    s0.visualize()

    b1: Board = Board(name='Traffic circle', width=12, height=12, critical_areas=[((4, 4), (8, 5)), ((4, 7), (8, 8)),
                                                                                  ((4, 5), (5, 7)), ((7, 5), (8, 7))])
    b1.summary()
    b1.visualize()
    plans1: List[List[Tuple[int, int]]] = consts.custom_plans_traffic_circle
    s1: Simulation = Simulation(name='Sim Traffic circle', board=b1, plans=plans1, agents=agents)
    s1.summary()
    s1.visualize()

def test_simulate() -> None:
    print("""
#######################################################
#          Testing custom scenarios creation          #
#######################################################
    """)
    sim_vars = ['board', 'agents', 'plans']
    for sv in sim_vars:
        print(f'Trying to simulate without {sv}, should fault')
        s0: Simulation = Simulation()
        setattr(s0, sv, None)
        try:
            s0.simulate(0)
        except Exception as e:
            print(f'Exception: {e}')

    print('Trying a real simulation - Intersection')
    b0: Board = Board(width=12, height=12, critical_areas=[((4, 4), (8, 8))])
    s0: Simulation = Simulation(board=b0, plans=consts.custom_plans_intersection, threshold=0.85)
    s0.summary()
    s0.simulate(0)
    s0.visualize(what='plans')
    s0.visualize(what='outcome')

    print('Trying a real simulation - Traffic circle')
    b1: Board = Board(width=12, height=12, critical_areas=[((4, 4), (8, 5)), ((4, 7), (8, 8)),
                                                           ((4, 5), (5, 7)), ((7, 5), (8, 7))])
    s1: Simulation = Simulation(board=b1, plans=consts.custom_plans_traffic_circle, threshold=0.85)
    s1.summary()
    s1.simulate(1)
    s1.visualize(what='plans')
    s1.visualize(what='outcome')
    print('fin')
