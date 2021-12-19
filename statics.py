import copy
import math
import json
from functools import reduce
import random

import consts
from board import Board
from sfl.Diagnoser.Diagnosis import Diagnosis
from sfl.Diagnoser.Barinel import Barinel
from sfl.Diagnoser.FullMatrix import FullMatrix
from sfl.Diagnoser.Staccato import Staccato
from simulation import Simulation
from agent import Agent

from typing import List, Dict, Callable
from typing import Tuple
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


def visualize(a_matrix, a_board, mode: str = 'grid') -> None:
    board = np.zeros((a_board['board_width'], a_board['board_height']))
    for ca in a_board['board_critical_areas']:
        board[ca[0][1]: ca[1][1], ca[0][0]:ca[1][0]] = 1
    for o in a_board['board_obstacles']:
        board[o[0][1]: o[1][1], o[0][0]:o[1][0]] = 2
    # plt.figure()
    plt.figure(dpi=300)
    cmap = colors.ListedColormap(['white', 'red', 'black'])
    plt.imshow(board, interpolation='none', vmin=0, vmax=2, aspect='equal', cmap=cmap)

    ax = plt.gca()

    # Major ticks
    ax.set_xticks(np.arange(0, a_board['board_height'], 1))
    ax.set_yticks(np.arange(0, a_board['board_width'], 1))

    # Labels for major ticks
    ax.set_xticklabels(np.arange(0, a_board['board_height'], 1))
    ax.set_yticklabels(np.arange(0, a_board['board_width'], 1))

    # Minor ticks
    ax.set_xticks(np.arange(-.5, a_board['board_height'], 1), minor=True)
    ax.set_yticks(np.arange(-.5, a_board['board_width'], 1), minor=True)

    # We change the fontsize of minor ticks label
    ax.tick_params(axis='both', which='major', labelsize=6)
    ax.tick_params(axis='both', which='minor', labelsize=1)

    # Gridlines based on minor ticks
    if mode == 'net':
        ax.grid(which='major', color='black', linestyle='-', linewidth=2, zorder=0)
    elif mode == 'grid':
        ax.grid(which='minor', color='black', linestyle='-', linewidth=2, zorder=0)
    else:
        raise Exception("mode needs to be either 'grid' or 'net'")

    ax.xaxis.tick_top()
    for ai, _ in enumerate(a_matrix):
        for i in range(len(a_matrix[ai][:-2])):
            plt.arrow(a_matrix[ai][i][0], a_matrix[ai][i][1],
                      a_matrix[ai][i + 1][0] - a_matrix[ai][i][0],
                      a_matrix[ai][i + 1][1] - a_matrix[ai][i][1],
                      width=0.5 - (0.5 / len(a_matrix)) * (ai % len(a_matrix)), color=get_pick_color(ai),
                      head_length=0, head_width=0, zorder=3 + ai % len(a_matrix))
        plt.arrow(a_matrix[ai][-2][0], a_matrix[ai][-2][1],
                  a_matrix[ai][-1][0] - a_matrix[ai][-2][0],
                  a_matrix[ai][-1][1] - a_matrix[ai][-2][1],
                  width=0.5 - (0.5 / len(a_matrix)) * (ai % len(a_matrix)), color=get_pick_color(ai),
                  head_width=0.5, head_length=0.5, zorder=3 + ai % len(a_matrix))

    plt.show()
    # plt.savefig('books_read.png')

def count_intersections(current_plans):
    intersections_table = np.zeros((len(current_plans), len(current_plans)), dtype=int)
    for a in range(len(current_plans)):
        for t in range(len(current_plans[a]) - 1):
            for a2 in range(len(current_plans)):
                if a2 != a:
                    for t2 in range(t + 1, len(current_plans[a2])):
                        if current_plans[a][t] == current_plans[a2][t2]:
                            # print(
                            #     f'intersection at {a},{t} ({current_plans[a][t]}) and {a2},{t2} ({current_plans[a2][t2]})')
                            intersections_table[a][a2] += 1
    print(np.sum(intersections_table))
    return np.sum(intersections_table)

def count_actual_execution_conflicts(outcome_json):
    simulations = outcome_json['simulations']
    n_agents = outcome_json['scenario']['parameters']['agents_number']
    l_plan = outcome_json['scenario']['world']['parameters']['plan_length']
    conflict_matrix = [[0 for _ in range(n_agents)] for _ in simulations]

    for si, s in enumerate(simulations):
        n = s['name']
        ft = s['fault_table']
        ae = s['actual_execution']
        for a in range(n_agents):
            for t in range(l_plan-1):
                if ae[a][t] == ae[a][t+1]:
                    if ft[a][t]:
                        pass
                        # print(f'Delay in n: {n}, a: {a}, t: {t}, Fault')
                    else:
                        # print(f'Delay in n: {n}, a: {a}, t: {t}, Conflict')
                        conflict_matrix[si][a] += 1
    return conflict_matrix


def get_pick_color(color_id):
    return consts.colors[color_id % 12]


def get_hardcoded_simulations() -> List[Simulation]:
    # Initializing agents
    agents: List[Agent] = [Agent(num=i, name='a' + str(i), is_faulty=(i == 0 or i == 1)) for i in list(range(6))]

    # Initializing boards
    b0: Board = Board(name='Intersection0', width=12, height=12, critical_areas=[[[4, 4], [8, 8]]])
    b1: Board = Board(name='Intersection1', width=12, height=12, critical_areas=[[[3, 3], [9, 9]]])
    b2: Board = Board(name='Traffic circle0', width=12, height=12,
                      critical_areas=[[[4, 4], [8, 5]], [[4, 7], [8, 8]],
                                      [[4, 5], [5, 7]], [[7, 5], [8, 7]]])

    # Creating simulations
    sims_intersection0 = []
    for i in range(len(consts.intersection_plan_pl_12_pic_19_outcomes)):
        s: Simulation = Simulation(name='Simulation intersection_plan_pl_12_pic_19 ' + str(i),
                                   board=b0,
                                   plans=consts.intersection0_plan_pl_12_pic_19,
                                   agents=agents)
        s.outcome = consts.intersection_plan_pl_12_pic_19_outcomes[i]
        s.delay_table = consts.intersection_plan_pl_12_pic_19_delay_tables[i]
        sims_intersection0.append(s)

    sims_intersection1 = []
    for i in range(len(consts.intersection_plan_pl_12_pic_18_outcomes)):
        s: Simulation = Simulation(name='Simulation intersection_plan_pl_12_pic_18 ' + str(i),
                                   board=b1,
                                   plans=consts.intersection1_plan_pl_12_pic_18,
                                   agents=agents)
        s.outcome = consts.intersection_plan_pl_12_pic_18_outcomes[i]
        s.delay_table = consts.intersection_plan_pl_12_pic_18_delay_tables[i]
        sims_intersection1.append(s)

    sims_traffic_circle0 = []
    for i in range(len(consts.traffic_circle_plan_pl_12_pic_78_outcomes)):
        s: Simulation = Simulation(name='Simulation traffic_circle_plan_pl_12_pic_78 ' + str(i),
                                   board=b2,
                                   plans=consts.traffic_circle0_plan_pl_12_pic_78,
                                   agents=agents)
        s.outcome = consts.traffic_circle_plan_pl_12_pic_78_outcomes[i]
        s.delay_table = consts.traffic_circle_plan_pl_12_pic_78_delay_tables[i]
        sims_traffic_circle0.append(s)

    return sims_intersection0 + sims_intersection1 + sims_traffic_circle0


def get_from_filename(config_filename: str) -> List[Simulation]:
    print(f'Getting from configuration file {config_filename}')
    # # TODO: implement

    # Opening JSON file
    f = open('benchmarks/' + config_filename)
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Initializing agents
    agents: List[Agent] = \
        [Agent(num=i, name=a['agent_name'], is_faulty=a['agent_is_faulty'], fail_prob=a['agent_fail_prob'])
         for i, a in enumerate(data['agents'])]

    # Initializing boards
    b = data['board']
    board: Board = Board(name=b['board_name'], width=b['board_width'], height=b['board_height'],
                         critical_areas=[[[ca[0][0], ca[0][1]], [ca[1][0], ca[1][1]]] for ca in
                                         b['board_critical_areas']])

    # Creating plans
    p = data['plan']
    plans: List[List[List[int, int]]] = [[[pat[0], pat[1]] for pat in pa] for pa in p['plan']]

    # Creating simulations
    simulations: List[Simulation] = \
        [Simulation(name=s['simulation_name'],
                    board=board,
                    plans=plans,
                    agents=[agents[a] for a in s['simulation_agent_nums']])
         for s in data['simulations']]

    return simulations


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


def has_collisions(plan):
    for t in range(len(plan[0])):
        for curr_a in range(0, len(plan) - 1):
            for other_a in range(curr_a + 1, len(plan)):
                # print(plan[curr_a][t], plan[other_a][t])
                if plan[curr_a][t][0] == plan[other_a][t][0] and plan[curr_a][t][1] == plan[other_a][t][1]:
                    return True, t
    return False, -1


def print_matrix(matrix_type: str, matrix: List[List]):
    print(f'{matrix_type}:')
    for row in matrix:
        print(row)


#############################################################
# Methods that determine the fault and conflict for the simulation
#############################################################
def available(wanted_resource: List[int], occupied_resources: List[List[int]]) -> bool:
    for ocr in occupied_resources:
        if wanted_resource == ocr:
            return False
    return True

def delay_and_wait_for_it_one_step_advance(present, next_planned, present_delay, p):
    # Initialize databases
    actual = [None for a in present]
    togo = [True for a in present]
    L = []
    ixs = None

    # a queue for agents management. first are faulty. then those that fall back to a resource
    # that other agent wants. then the rest.
    management_queue_idxs = []
    agents_idxs = [i for i in range(len(present))]
    for i, pd in enumerate(present_delay):
        if pd:
            if i not in management_queue_idxs:
                management_queue_idxs.append(i)
    for i, idx in enumerate(management_queue_idxs):
        if idx in agents_idxs:
            agents_idxs.remove(idx)
    for i, pst in enumerate(present):
        if pst in next_planned:
            if i not in management_queue_idxs:
                management_queue_idxs.append(i)
    for i, idx in enumerate(management_queue_idxs):
        if idx in agents_idxs:
            agents_idxs.remove(idx)
    for i, ai in enumerate(agents_idxs):
        if ai not in management_queue_idxs:
            management_queue_idxs.append(ai)
    for i, idx in enumerate(management_queue_idxs):
        if idx in agents_idxs:
            agents_idxs.remove(idx)

    # print(f'present: {present}')
    # print(f'next_planned: {next_planned}')
    # print(f'present_delay: {present_delay}')
    # print(f'management_queue_idxs: {management_queue_idxs}')
    # print(f'actual: {actual}')
    # Fill delay to actual; Remove delays from togo; get delayed to list L
    for i, pd in enumerate(present_delay):
        if pd:
            actual[i] = present[i]
            togo[i] = False
            L.append(present[i])
            management_queue_idxs.remove(i)

    # print(f'management_queue_idxs after fail: {management_queue_idxs}')
    # While !togo.empty()
    while any(togo):
        if len(L) > 0:
            x = L.pop(0)
            if x in actual:
                ixs = [ix for ix, s in enumerate(next_planned) if s == x]
                ixs = [ix for ix in ixs if actual[ix] is None]
                if len(ixs) > 0:
                    for ix in ixs:
                        actual[ix] = present[ix]
                        togo[ix] = False
                        L.append(present[ix])
                        # print(f'actual: {actual}')
        else:
            a = management_queue_idxs.pop(0)
            # print(f'management_queue_idxs after pop: {management_queue_idxs}')
            if next_planned[a] not in actual:
                actual[a] = next_planned[a]
                p[a] += 1
                togo[a] = False
                L.append(next_planned[a])
            else:
                actual[a] = present[a]
                togo[a] = False
                L.append(present[a])
            # print(f'actual: {actual}')

    # return actual
    # print(f'actual: {actual}')
    return actual, p


def simulate_delay_and_wait_for_it(agents: List[Agent],
                                   plans: List[List[List[int]]],
                                   facm_args: Dict) -> Tuple[List[List[bool]], List[List[List[int]]]]:
    # some consts
    agent_count = len(agents)
    timesteps_count = len(plans[0])

    # generate a delay table
    delay_table = \
        [[True if a.is_faulty and random.uniform(0, 1) < a.fail_prob else False
          for t in range(timesteps_count - 1)] + [False]
         for a in agents]

    ############## DEBUG ##############
    # plans = [[(6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (3, 5), (2, 5)],
    #          [(5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (8, 6), (9, 6)],
    #          [(8, 5), (7, 5), (7, 4), (6, 4), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9)],
    #          [(3, 6), (4, 6), (4, 7), (5, 7), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2)],
    #          [(6, 9), (6, 8), (6, 7), (7, 7), (7, 6), (7, 5), (7, 4), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)],
    #          [(5, 2), (5, 3), (5, 4), (4, 4), (4, 5), (4, 6), (4, 7), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]]
    # delay_table = [[True, False, True, False, False, False, False, True, False, False, True, False],
    #                [True, False, False, False, False, False, False, False, True, False, False, False],
    #                [False, False, False, False, False, False, False, False, False, False, False, False],
    #                [False, False, False, False, False, False, False, False, False, False, False, False],
    #                [False, False, False, False, False, False, False, False, False, False, False, False],
    #                [False, False, False, False, False, False, False, False, False, False, False, False]]
    ############## DEBUG ##############

    # initialize outcome with the starting resources
    outcome = [[plans[i][0]] for i in range(agent_count)]

    # initialize pointers
    p = [0] * agent_count

    # advance the agents step by step according to the delay table
    for timestep in range(timesteps_count - 1):
        # prepare present
        present = [outcome[a][timestep] for a in range(len(outcome))]
        # prepare next_planned
        next_planned = [plans[i][p+1] for i, p in enumerate(p)]
        # prepare present_delay
        present_delay = [delay_table[a][timestep] for a in range(len(delay_table))]
        # print(f'time:{timestep}')
        next_actual, p = delay_and_wait_for_it_one_step_advance(present, next_planned, present_delay, p)
        # insert the next step to the outcomes
        for ai in range(agent_count):
            outcome[ai].append(next_actual[ai])

    # check for no collisions (this code should never get invoked in a correct code)
    hc, time = has_collisions(outcome)
    if hc:
        print(f'Collisions in time {time}')
        print(f'Plan:')
        for p in plans:
            print(p)
        print(f'Delay table:')
        for d in delay_table:
            print(d)
        print(f'Actual execution:')
        for oc in outcome:
            print(oc)
        delay_table, outcome = None, None

    return delay_table, outcome


#############################################################
#     Methods that determine a simulation success/fail      #
#############################################################
def simulation_success_method_percentage_free_ca(simulation: Simulation, ssm_args: Dict) -> bool:
    # Getting the threshold
    threshold = ssm_args['t']

    # Get all the occupied positions
    occupied_positions: List[List[int, int]] = []
    for a in simulation.outcome:
        occupied_positions.append(a[-1])

    # For each critical area, check how much of its positions
    # is not in the occupied positions
    critical_positions: List[List[List[int, int]]] = []
    for ca in simulation.board.critical_areas:
        ca_positions = [[i, j] for i in range(ca[0][0], ca[1][0]) for j in range(ca[0][1], ca[1][1])]
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
                                                                      evsfm_args: Dict) \
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
                    if evsfm_args['ifs']:
                        spectra[i].append(1)  # Original
                    else:
                        spectra[i].append(0)  # Alternative
                else:
                    if evsfm_args['ifs']:
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
    sol = minimize(objective, h0, method="L-BFGS-B", bounds=bnds, tol=1e-3, options={'maxiter': 100})

    return -sol.fun


def calculate_diagnoses_and_probabilities_ochiai(spectra: List[List[int]],
                                                 error_vector: List[int],
                                                 kwargs: Dict,
                                                 simulations: List[Simulation]) -> Tuple[List[List[int]], List[float]]:
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

    # normalize probabilities and order them
    probabilities_sum = sum(probabilities)
    for i, probability in enumerate(probabilities):
        probabilities[i] = probabilities[i] / probabilities_sum if probabilities_sum !=0 else 1.0 / len(probabilities)
    z_probabilities, z_diagnoses = zip(*[(d, p) for d, p in sorted(zip(probabilities, diagnoses))])
    lz_diagnoses = list(z_diagnoses)
    lz_probabilities = list(z_probabilities)
    lz_diagnoses.reverse()
    lz_probabilities.reverse()

    print(f'oracle: {[a.num for a in simulations[0].agents if a.is_faulty]}')

    print(f'diagnoses and probabilities:')
    for i, _ in enumerate(lz_diagnoses):
        print(f'{lz_diagnoses[i]}: {lz_probabilities[i]}')

    return lz_diagnoses, lz_probabilities

def calculate_diagnoses_and_probabilities_tarantula(spectra: List[List[int]],
                                                    error_vector: List[int],
                                                    kwargs: Dict,
                                                    simulations: List[Simulation]) -> Tuple[List[List[int]], List[float]]:
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
        try:
            soj = (dm[0][j] * 1.0 / (dm[0][j] + dm[2][j])) / ((dm[1][j] / (dm[1][j] + dm[3][j])) + (dm[0][j] / (dm[0][j] + dm[2][j])))
        except ZeroDivisionError as zde:
            soj = 0
        probabilities.append(soj)

    # normalize probabilities and order them
    probabilities_sum = sum(probabilities)
    for i, probability in enumerate(probabilities):
        probabilities[i] = probabilities[i] / probabilities_sum if probabilities_sum !=0 else 1.0 / len(probabilities)
    z_probabilities, z_diagnoses = zip(*[(d, p) for d, p in sorted(zip(probabilities, diagnoses))])
    lz_diagnoses = list(z_diagnoses)
    lz_probabilities = list(z_probabilities)
    lz_diagnoses.reverse()
    lz_probabilities.reverse()

    print(f'oracle: {[a.num for a in simulations[0].agents if a.is_faulty]}')

    print(f'diagnoses and probabilities:')
    for i, _ in enumerate(lz_diagnoses):
        print(f'{lz_diagnoses[i]}: {lz_probabilities[i]}')

    return lz_diagnoses, lz_probabilities


def calculate_diagnoses_and_probabilities_barinel_avi(spectra: List[List[int]],
                                                      error_vector: List[int],
                                                      kwargs: Dict,
                                                      simulations: List[Simulation]) -> Tuple[
    List[List[int]], List[float]]:
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
    priors = methods[kwargs['mfcp']](spectra,
                                                              error_vector,
                                                              kwargs,
                                                              simulations)
    probabilities = [0.0 for _ in diagnoses]
    e_dks = []
    for i, dk in enumerate(diagnoses):
        e_dk = calculate_e_dk(dk, spectra, error_vector)
        e_dks.append(e_dk)
        prior = math.prod([priors[c] for c in dk])
        probabilities[i] = prior * e_dk

    # normalize probabilities and order them
    probabilities_sum = sum(probabilities)
    for i, probability in enumerate(probabilities):
        probabilities[i] = probabilities[i] / probabilities_sum
    z_probabilities, z_diagnoses = zip(*[(d, p) for d, p in sorted(zip(probabilities, diagnoses))])
    lz_diagnoses = list(z_diagnoses)
    lz_probabilities = list(z_probabilities)
    lz_diagnoses.reverse()
    lz_probabilities.reverse()

    print(f'oracle: {[a.num for a in simulations[0].agents if a.is_faulty]}')

    print(f'diagnoses and probabilities:')
    for i, _ in enumerate(lz_diagnoses):
        print(f'{lz_diagnoses[i]}: {lz_probabilities[i]}')

    # return ordered and normalized diagnoses and probabilities
    return lz_diagnoses, lz_probabilities


def calculate_diagnoses_and_probabilities_barinel_amir(spectra: List[List[int]],
                                                       error_vector: List[int],
                                                       kwargs: Dict,
                                                       simulations: List[Simulation]) -> \
        Tuple[List[List[int]], List[float]]:
    # Calculate prior probabilities
    priors = methods[kwargs['mfcp']](spectra,
                                                              error_vector,
                                                              kwargs,
                                                              simulations)

    # calculate optimized probabilities
    failed_tests = list(
        map(lambda test: list(enumerate(test[0])), filter(lambda test: test[1] == 1, zip(spectra, error_vector))))
    used_components = dict(enumerate(sorted(reduce(set.__or__, map(
        lambda test: set(map(lambda comp: comp[0], filter(lambda comp: comp[1] == 1, test))), failed_tests), set()))))
    optimizedMatrix = FullMatrix()
    optimizedMatrix.set_probabilities([x[1] for x in enumerate(priors) if x[0] in used_components])
    newErr = []
    newMatrix = []
    used_tests = []
    for i, (test, err) in enumerate(zip(spectra, error_vector)):
        newTest = list(map(lambda i: test[i], sorted(used_components.values())))
        if 1 in newTest:  ## optimization could remove all comps of a test
            newMatrix.append(newTest)
            newErr.append(err)
            used_tests.append(i)
    optimizedMatrix.set_matrix(newMatrix)
    optimizedMatrix.set_error(newErr)
    used_tests = sorted(used_tests)

    # rename back the components of the diagnoses
    Opt_diagnoses = optimizedMatrix.diagnose()
    diagnoses = []
    for diag in Opt_diagnoses:
        diag = diag.clone()
        diag_comps = [used_components[x] for x in diag.diagnosis]
        diag.diagnosis = list(diag_comps)
        diagnoses.append(diag)

    # print(f'used_components: {used_components}')

    # transform diagnoses to 2 lists like the default barinel
    t_diagnoses, t_probabilities = [], []
    for d in diagnoses:
        t_diagnoses.append(d.diagnosis)
        t_probabilities.append(d.probability)

    # normalize probabilities and order them
    probabilities_sum = sum(t_probabilities)
    for i, probability in enumerate(t_probabilities):
        t_probabilities[i] = t_probabilities[i] / probabilities_sum
    z_probabilities, z_diagnoses = zip(*[(d, p) for d, p in sorted(zip(t_probabilities, t_diagnoses))])
    lz_diagnoses = list(z_diagnoses)
    lz_probabilities = list(z_probabilities)
    lz_diagnoses.reverse()
    lz_probabilities.reverse()

    print(f'oracle: {[a.num for a in simulations[0].agents if a.is_faulty]}')

    print(f'diagnoses and probabilities:')
    for i, _ in enumerate(lz_diagnoses):
        print(f'{lz_diagnoses[i]}: {lz_probabilities[i]}')

    return lz_diagnoses, lz_probabilities


#############################################################
#              Methods for calculating priors               #
#############################################################
def populate_intersections_table(num_agents, simulations) -> np.ndarray:
    # initialize intersections table
    intersections_table = np.zeros((num_agents, num_agents), dtype=int)

    # populate intersections table across the different simulations
    for i, simulation in enumerate(simulations):
        current_plans = simulation.plans
        for a in range(len(current_plans)):
            for t in range(len(current_plans[a]) - 1):
                for a2 in range(len(current_plans)):
                    if a2 != a:
                        for t2 in range(t + 1, len(current_plans[a2])):
                            if current_plans[a][t] == current_plans[a2][t2]:
                                intersections_table[a][a2] += 1
    return intersections_table


def calculate_priors_one(spectra: List[List[int]],
                         error_vector: List[int],
                         kwargs: Dict,
                         simulations: List[Simulation]) -> List[float]:
    p = 1
    priors = [p for _ in range(len(spectra[0]))]  # priors
    return priors


def calculate_priors_static(spectra: List[List[int]],
                            error_vector: List[int],
                            kwargs: Dict,
                            simulations: List[Simulation]) -> List[float]:
    p = 0.1
    priors = [p for _ in range(len(spectra[0]))]  # priors
    return priors


def calculate_priors_intersections1(spectra: List[List[int]],
                                    error_vector: List[int],
                                    kwargs: Dict,
                                    simulations: List[Simulation]) -> List[float]:
    """
    Simple method for calculating priors using intersections. A single table that holds information about
    agents intersections throughout the entire spectra is created.
    An agent has the number of times it passes first in an intersection and the number of
    times it passes as the second one. We call the difference between the two: forepass coefficient
    Diagnoses that involve agents with higher forepass coefficients have higher probabilities.
    :param spectra:
    :param error_vector:
    :param kwargs:
    :param simulations:
    :return:
    """
    # initialize and populate intersections table across the different simulations
    intersections_table = populate_intersections_table(len(spectra[0]), simulations)

    # calculate forepass coefficients
    passed_first = [sum(row) for row in intersections_table]
    passed_last = [sum(row) for row in intersections_table.transpose()]
    forepass_coefficient = np.subtract(passed_first, passed_last)

    # calculate priors
    priors = copy.deepcopy(forepass_coefficient)
    alpha = 2
    d = 5
    normalized_priors = [(float(i) - min(priors) + alpha) / (max(priors) - min(priors) + alpha * d) for i in priors]
    sum_normalized_priors = sum(normalized_priors)
    normalized_priors = [i / sum_normalized_priors for i in normalized_priors]
    return normalized_priors


def calculate_priors_intersections2(spectra: List[List[int]],
                                    error_vector: List[int],
                                    kwargs: Dict,
                                    simulations: List[Simulation]) -> List[float]:
    """
    Simple method for calculating priors using intersections. A single table that holds information about
    agents intersections throughout the entire spectra is created.
    An agent has the number of times it passes first in an intersection and the number of
    times it passes as the second one. For each agent we calculate the total number that an agent passes in
    intersections as the second agent (call this number pass_second), which gives an estimate on how probable
    it is for an agent to not reach its final resource because of other agents. We then transform those
    numbers to probabilities, giving agents with higher pass_second number a lower a-priori probability to
    be faulty.
    :param spectra:
    :param error_vector:
    :param kwargs:
    :param simulations:
    :return:
    """
    # initialize and populate intersections table across the different simulations
    intersections_table = populate_intersections_table(len(spectra[0]), simulations)

    # calculate pass_second numbers
    pass_second = [sum(row) for row in intersections_table.transpose()]

    # Print pass_second number
    # print(f'pass_second: {[ps / len(error_vector) for ps in pass_second]}')

    # normalize and invert pass_second numbers to get agent-wise probabilities
    priors = copy.deepcopy(pass_second)
    alpha = 2
    d = 5
    normalized_priors = [(float(i) - min(priors) + alpha) / (max(priors) - min(priors) + alpha * d) for i in priors]
    normalized_priors = [1 - p for p in normalized_priors]
    sum_normalized_priors = sum(normalized_priors)
    normalized_priors = [i / sum_normalized_priors for i in normalized_priors]
    return normalized_priors


#############################################################
#           Methods for evaluating the algorithm            #
#############################################################
def evaluate_algorithm_wasted_effort(kwargs: Dict) -> Dict:
    # TODO: implement
    return {'wasted_effort': 420}


def evaluate_algorithm_precision_recall(kwargs: Dict) -> Dict:
    # TODO: implement
    return {'Precision': 420, 'Recall': 420}


methods = {
    # Methods that determine the fault and conflict for the simulation
    'dawfi': simulate_delay_and_wait_for_it,

    # Methods that determine a simulation success/fail
    'pfc': simulation_success_method_percentage_free_ca,

    # Methods that determine the agents success/fail
    'rfr': agent_success_method_reach_final_res,

    # Methods that determine how to populate the spectra
    'apfc': error_vector_and_spectra_fill_method_agent_pass_fail_contribution,

    # Methods for calculating diagnoses and their probabilities
    'ochiai': calculate_diagnoses_and_probabilities_ochiai,
    'tarantula': calculate_diagnoses_and_probabilities_tarantula,
    'barinelavi': calculate_diagnoses_and_probabilities_barinel_avi,
    'barinelamir': calculate_diagnoses_and_probabilities_barinel_amir,

    # Methods for calculating priors
    'pone': calculate_priors_one,
    'pstatic': calculate_priors_static,
    'pintersections1': calculate_priors_intersections1,
    'pintersections2': calculate_priors_intersections2,

    # Methods for evaluating the algorithm
    'wasted_effort': evaluate_algorithm_wasted_effort,
    'precision_recall': evaluate_algorithm_precision_recall
}
