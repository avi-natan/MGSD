import math

import consts
from board import Board
from simulation import Simulation
from agent import Agent

from typing import List, Tuple, Dict, Callable
from scipy.optimize import minimize
import numpy as np


def get_pick_color(color_id):
    return consts.colors[color_id % 12]


def get_hardcoded_simulations() -> List[Simulation]:
    # Initializing agents
    agents: List[Agent] = [Agent(name='a' + str(i), is_faulty=(i == 0 or i == 1)) for i in list(range(6))]

    # Initializing boards
    # b0: Board = Board(name='Intersection', width=12, height=12, critical_areas=[((4, 4), (8, 8))])
    b1: Board = Board(name='Traffic circle', width=12, height=12,
                      critical_areas=[((4, 4), (8, 5)), ((4, 7), (8, 8)),
                                      ((4, 5), (5, 7)), ((7, 5), (8, 7))])

    # Creating simulations
    # s0: Simulation = Simulation(name='Simulation Intersection',
    #                             board=b0,
    #                             plans=consts.custom_plans_intersection,
    #                             agents=agents)
    s1: Simulation = Simulation(name='Simulation Traffic circle1',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s2: Simulation = Simulation(name='Simulation Traffic circle2',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s3: Simulation = Simulation(name='Simulation Traffic circle3',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s4: Simulation = Simulation(name='Simulation Traffic circle4',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s5: Simulation = Simulation(name='Simulation Traffic circle5',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s6: Simulation = Simulation(name='Simulation Traffic circle6',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s7: Simulation = Simulation(name='Simulation Traffic circle7',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s8: Simulation = Simulation(name='Simulation Traffic circle8',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s9: Simulation = Simulation(name='Simulation Traffic circle9',
                                board=b1,
                                plans=consts.custom_plans_traffic_circle,
                                agents=agents)
    s10: Simulation = Simulation(name='Simulation Traffic circle10',
                                 board=b1,
                                 plans=consts.custom_plans_traffic_circle,
                                 agents=agents)
    s11: Simulation = Simulation(name='Simulation Traffic circle11',
                                 board=b1,
                                 plans=consts.custom_plans_traffic_circle,
                                 agents=agents)
    s12: Simulation = Simulation(name='Simulation Traffic circle12',
                                 board=b1,
                                 plans=consts.custom_plans_traffic_circle,
                                 agents=agents)
    s13: Simulation = Simulation(name='Simulation Traffic circle13',
                                 board=b1,
                                 plans=consts.custom_plans_traffic_circle,
                                 agents=agents)

    return [
        # s0,
        s1,
        s2,
        s3,
        s4,
        s5,
        s6,
        s7,
        s8,
        s9,
        s10,
        s11,
        s12,
        s13
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


#############################################################
#     Methods that determine a simulation success/fail      #
#############################################################
def simulation_success_method_percentage_free_ca(simulation: Simulation, ssm_args: Dict) -> bool:
    # Getting the threshold
    threshold = ssm_args['threshold']

    # Get all the occupied positions
    occupied_positions: List[Tuple[int, int]] = []
    for a in simulation.outcome:
        occupied_positions.append(a[-1])

    # For each critical area, check how much of its positions
    # is not in the occupied positions
    critical_positions: List[List[Tuple[int, int]]] = []
    for ca in simulation.board.critical_areas:
        ca_positions = [(i, j) for i in range(ca[0][0], ca[1][0]) for j in range(ca[0][1], ca[1][1])]
        critical_positions.append(ca_positions)
    critical_positions_flat = [position for ca in critical_positions for position in ca]

    # Calculate the percentage
    number_of_ca_that_are_free = 0
    for ca in critical_positions_flat:
        if ca not in occupied_positions:
            number_of_ca_that_are_free += 1
    percentage_free = number_of_ca_that_are_free / len(critical_positions_flat)
    print(f'Method <simulation_success_method_percentage_free_ca>: Threshold is {threshold}')
    print(f'Percentage free critical areas in {simulation.name}: {percentage_free}')
    simulation_success = percentage_free > threshold
    return simulation_success


#############################################################
#      Methods that determine the agents success/fail       #
#############################################################
def agent_success_method_reach_final_res(simulation: Simulation, j: int, asm_args: Dict) -> bool:
    return simulation.outcome[j][-1] == simulation.plans[j][-1]


#############################################################
#    Methods that determine how to populate the spectra     #
#############################################################
def error_vector_and_spectra_fill_method_agent_pass_fail_contribution(simulations: List[Simulation],
                                                                      simulation_success_method: str,
                                                                      ssm_args: Dict,
                                                                      agent_success_method: str,
                                                                      asm_args: Dict,
                                                                      evsfm_args: Dict)\
        -> Tuple[List[int], List[List[int]]]:
    error_vector = []
    spectra = []
    for i, s in enumerate(simulations):
        simulation_success = methods[simulation_success_method](s, ssm_args)
        if simulation_success:
            error_vector.append(0)
            spectra.append([])
            for j, _ in enumerate(s.outcome):
                agent_success = methods[agent_success_method](s, j, asm_args)
                if agent_success:
                    if evsfm_args['invert_for_success']:
                        spectra[i].append(1)  # Original
                    else:
                        spectra[i].append(0)  # Alternative
                else:
                    if evsfm_args['invert_for_success']:
                        spectra[i].append(0)  # Original
                    else:
                        spectra[i].append(1)  # Alternative
        else:
            error_vector.append(1)
            spectra.append([])
            for j, _ in enumerate(s.outcome):
                agent_success = methods[agent_success_method](s, j, asm_args)
                if agent_success:
                    spectra[i].append(0)
                else:
                    spectra[i].append(1)
    return error_vector, spectra


#############################################################
# Methods for calculating diagnoses and their probabilities #
#############################################################
def calculate_dichotomy_matrix(spectra: List[List[int]], error_vector: List[int]) -> List[List[int]]:
    dichotomy_matrix = [[],  # n11
                        [],  # n10
                        [],  # n01
                        []]  # n00
    for cj in range(len(spectra[0])):
        n11, n10, n01, n00 = 0, 0, 0, 0
        cj_vector = [spectra[i][cj] for i in range(len(spectra))]
        for i in range(len(cj_vector)):
            if cj_vector[i] == 1 and error_vector[i] == 1:
                n11 += 1
            elif cj_vector[i] == 1 and error_vector[i] == 0:
                n10 += 1
            elif cj_vector[i] == 0 and error_vector[i] == 1:
                n01 += 1
            else:
                n00 += 1
        dichotomy_matrix[0].append(n11)
        dichotomy_matrix[1].append(n10)
        dichotomy_matrix[2].append(n01)
        dichotomy_matrix[3].append(n00)
    return dichotomy_matrix

def calculate_e_dk(dk: List[int], spectra: List[List[int]], error_vector: List[int]):
    funcArr = ['(-1)']
    objective: Callable[[List[float]], float] = None
    active_vars = [False] * len(spectra[0])

    # get the active vars in this diagnosis
    for i, e in enumerate(error_vector):
        for j, c in enumerate(spectra[i]):
            if spectra[i][j] == 1 and j in dk:
                active_vars[j] = True

    # re-labeling variables to conform to scipy's requirements
    index_rv = 0
    renamed_vars = {}
    for i, av in enumerate(active_vars):
        if av:
            renamed_vars[str(i)] = index_rv
            index_rv += 1

    # building the target function as a string
    for i, e in enumerate(error_vector):
        fa = "1*"
        for j, c in enumerate(spectra[i]):
            if spectra[i][j] == 1 and j in dk:
                fa = fa + f"x[{renamed_vars[str(j)]}]*"
        fa = fa[:-1]
        if error_vector[i] == 1:
            fa = "*(1-" + fa + ")"
        else:
            fa = "*(" + fa + ")"
        funcArr.append(fa)

    # using dynamic programming to initialize the target function
    func = ""
    for fa in funcArr:
        func = func + fa
    objective = eval(f'lambda x: {func}')

    # building bounds over the variables
    # and the initial health vector
    b = (0.0, 1.0)
    initial_h = 0.5
    bnds = []
    h0 = []
    for av in active_vars:
        if av:
            bnds.append(b)
            h0.append(initial_h)

    # solving the minimization problem
    h0 = np.array(h0)
    sol = minimize(objective, h0, method='SLSQP', bounds=bnds)

    # print(sol)
    # print(-sol.fun)
    # print(sol.x)
    return -sol.fun


def calculate_diagnoses_and_probabilities_ochiai(spectra: List[List[int]],
                                                 error_vector: List[int],
                                                 kwargs: Dict) -> Tuple[List[List[int]], List[float]]:
    diagnoses = [[i] for i in range(len(spectra[0]))]

    dm = calculate_dichotomy_matrix(spectra, error_vector)
    print('Dichotomy matrix:')
    for i in range(len(dm)):
        print(dm[i])
    """
    dichotomy matrix example:
                    c0  c1  ..  cJ
            n11:    1   0       1
            n10:    1   1       0
            n01:    0   0       2
            n00:    3   4       2
    """
    probabilities = []
    for j in range(len(spectra[0])):
        soj = ((dm[0][j] * 1.0) / math.sqrt((dm[0][j] + dm[1][j]) * (dm[0][j] + dm[2][j]))) if dm[0][j] != 0 else 0
        probabilities.append(soj)

    return diagnoses, probabilities


def calculate_diagnoses_and_probabilities_barinel(spectra: List[List[int]],
                                                  error_vector: List[int],
                                                  kwargs: Dict) -> Tuple[List[List[int]], np.ndarray]:
    # # Calculate diagnoses using hitting sets with CDS
    conflicts = []
    for i in range(len(error_vector)):
        if error_vector[i] == 1:
            c = []
            for j in range(len(spectra[i])):
                if spectra[i][j] == 1:
                    c.append(j)
            conflicts.append(c)
    diagnoses: List[List[int]] = conflict_directed_search(conflicts=conflicts)

    # # calculate probabilities
    # Dummy implementation
    # probabilities = [1 / len(diagnoses) for _ in diagnoses]

    # Real implementation
    probabilities = [0 for _ in diagnoses]
    e_dks = []
    for i, dk in enumerate(diagnoses):
        e_dk = calculate_e_dk(dk, spectra, error_vector)
        e_dks.append(e_dk)

    # # sanity check
    # print('e_dks')
    # for i, d in enumerate(diagnoses):
    #     print(f'{d}: {e_dks[i]}')

    # normalize probabilities and order them
    e_dks_sum = sum(e_dks)
    for i, e_dk in enumerate(e_dks):
        probabilities[i] = e_dk / e_dks_sum
    probabilities = np.array(probabilities)
    probabilities = -np.sort(-probabilities)

    # # another sanity check
    # print('probabilities')
    # for i, d in enumerate(diagnoses):
    #     print(f'{d}: {probabilities[i]}')

    return diagnoses, probabilities


methods = {
    # Methods that determine a simulation success/fail
    'percentage_free_ca': simulation_success_method_percentage_free_ca,

    # Methods that determine the agents success/fail
    'reach_final_res': agent_success_method_reach_final_res,

    # Methods that determine how to populate the spectra
    'agent_pass_fail_contribution': error_vector_and_spectra_fill_method_agent_pass_fail_contribution,

    # Methods for calculating diagnoses and their probabilities
    'ochiai': calculate_diagnoses_and_probabilities_ochiai,
    'barinel': calculate_diagnoses_and_probabilities_barinel
}
