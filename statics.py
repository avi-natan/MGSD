import consts
from board import Board
from simulation import Simulation
from agent import Agent

from typing import List

def get_pick_color(color_id):
    return consts.colors[color_id % 12]

def get_hardcoded_simulations() -> List[Simulation]:
    # Initializing agents
    agents: List[Agent] = [Agent(name='a'+str(i), is_faulty=(i == 0 or i == 1)) for i in list(range(6))]

    # Initializing boards
    b0: Board = Board(name='Intersection', width=12, height=12, critical_areas=[((4, 4), (8, 8))])
    b1: Board = Board(name='Traffic circle', width=12, height=12,
                      critical_areas=[((4, 4), (8, 5)), ((4, 7), (8, 8)),
                                      ((4, 5), (5, 7)), ((7, 5), (8, 7))])

    # Creating simulations
    s0: Simulation = Simulation(name='Simulation Intersection',
                                board=b0,
                                plans=consts.custom_plans_intersection,
                                agents=agents,
                                threshold=0.85)
    s1: Simulation = Simulation(name='Simulation Traffic circle1',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents,
                                threshold=0.85)
    # s2: Simulation = Simulation(name='Simulation Traffic circle2',
    #                             board=b1,
    #                             plans=consts.custom_plans_traffic_circle,
    #                             agents=agents,
    #                             threshold=0.85)
    # s3: Simulation = Simulation(name='Simulation Traffic circle3',
    #                             board=b1,
    #                             plans=consts.custom_plans_traffic_circle,
    #                             agents=agents,
    #                             threshold=0.85)

    return [
        s0,
        s1,
        # s2,
        # s3
    ]

def get_from_filename(config_filename: str) -> List[Simulation]:
    print(f'Getting from configuration file {config_filename}')
    # # TODO: implement
    return []

def conflict_directed_search(conflicts: List[List[int]]) -> List[List[int]]:
    diagnoses = []
    new_diagnoses = [[conflicts[0][i]] for i in range(len(conflicts[0]))]
    for conflict in conflicts[1:]:
        diagnoses = new_diagnoses
        new_diagnoses = []
        while len(diagnoses) != 0:
            diagnosis = diagnoses.pop(0)
            intsec = list(set(diagnosis) & set(conflict))
            if len(intsec) == 0:
                new_diags = [diagnosis + [c] for c in conflict]

                def filter_supersets(new_diag: List[int]) -> bool:
                    for d in diagnoses + new_diagnoses:
                        if set(d) <= set(new_diag):
                            return False
                    return True
                filtered_new_diags = list(filter(filter_supersets, new_diags))
                new_diagnoses += filtered_new_diags
            else:
                new_diagnoses.append(diagnosis)
    diagnoses = new_diagnoses
    return diagnoses
