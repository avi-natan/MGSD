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

from typing import List, Tuple, Dict, Callable
from scipy.optimize import minimize
import numpy as np


def get_pick_color(color_id):
    return consts.colors[color_id % 12]


def get_hardcoded_simulations() -> List[Simulation]:
    # Initializing agents
    agents: List[Agent] = [Agent(name='a' + str(i), is_faulty=(i == 0 or i == 1)) for i in list(range(6))]

    # Initializing boards
    b0: Board = Board(name='Intersection0', width=12, height=12, critical_areas=[((4, 4), (8, 8))])
    b1: Board = Board(name='Intersection1', width=12, height=12, critical_areas=[((3, 3), (9, 9))])
    b2: Board = Board(name='Traffic circle0', width=12, height=12,
                      critical_areas=[((4, 4), (8, 5)), ((4, 7), (8, 8)),
                                      ((4, 5), (5, 7)), ((7, 5), (8, 7))])

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
        [Agent(name=a['agent_name'], is_faulty=a['agent_is_faulty'], fail_prob=a['agent_fail_prob'])
         for a in data['agents']]

    # Initializing boards
    b = data['board']
    board: Board = Board(name=b['board_name'], width=b['board_width'], height=b['board_height'],
                         critical_areas=[((ca[0][0], ca[0][1]), (ca[1][0], ca[1][1])) for ca in
                                         b['board_critical_areas']])

    # Creating plans
    p = data['plan']
    plans: List[List[Tuple[int, int]]] = [[(pat[0], pat[1]) for pat in pa] for pa in p['plan']]

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
                    return True
    return False


def print_matrix(matrix_type: str, matrix: List[List]):
    print(f'{matrix_type}:')
    for row in matrix:
        print(row)


#############################################################
# Methods that determine the fault and conflict for the simulation
#############################################################
def available(wanted_resource: Tuple[int, int], occupied_resources: List[Tuple[int, int]]) -> bool:
    for ocr in occupied_resources:
        if wanted_resource == ocr:
            return False
    return True


def simulate_delay_and_wait_for_it(agents: List[Agent],
                                   plans: List[List[Tuple[int, int]]],
                                   facm_args: Dict) -> Tuple[List[List[bool]], List[List[Tuple[int, int]]]]:
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
        # initialize next step
        next_step = [[(-1, -1)] * agent_count, [(-1, -1)] * agent_count]

        # set next step for agents that have fault in this timestep
        for ai in range(agent_count):
            if delay_table[ai][timestep]:
                next_step[0][ai] = plans[ai][p[ai]]
        next_step.reverse()

        # find all the agents that are blocked due to conflicts this round
        # an iterative pass until there is a convergence
        while next_step[0] != next_step[1]:
            next_step[0] = list(next_step[1])
            for ai in range(agent_count):
                if next_step[0][ai] == (-1, -1):
                    if not available(plans[ai][p[ai] + 1], next_step[1]) \
                            or not available(plans[ai][p[ai] + 1], next_step[0]):
                        next_step[0][ai] = plans[ai][p[ai]]
            next_step.reverse()

        # set next step for the remaining agents - agents could still get stuck due to mutual exclusions
        # an iterative pass until there is a convergence
        for ai in range(agent_count):
            if next_step[0][ai] == (-1, -1):
                p[ai] = p[ai] + 1
                next_step[0][ai] = plans[ai][p[ai]]
                next_step.reverse()

                while next_step[0] != next_step[1]:
                    next_step[0] = list(next_step[1])
                    for ai2 in range(agent_count):
                        if next_step[0][ai2] == (-1, -1):
                            if not available(plans[ai2][p[ai2] + 1], next_step[1]) \
                                    or not available(plans[ai2][p[ai2] + 1], next_step[0]):
                                next_step[0][ai2] = plans[ai2][p[ai2]]
                    next_step.reverse()

        # insert the next step to the outcomes
        for ai in range(agent_count):
            outcome[ai].append(next_step[0][ai])

    # check for no collisions (this code should never get invoked in a correct code)
    if has_collisions(outcome):
        for oc in outcome:
            print(oc)
        raise Exception('found collisions')

    return delay_table, outcome
    # return consts.traffic_circle_custom_plan1_outcomes[3]


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

    return diagnoses, probabilities


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
    priors = methods[kwargs['method_for_calculating_priors']](spectra,
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

    # return ordered and normalized diagnoses and probabilities
    return lz_diagnoses, lz_probabilities


def calculate_diagnoses_and_probabilities_barinel_amir(spectra: List[List[int]],
                                                       error_vector: List[int],
                                                       kwargs: Dict,
                                                       simulations: List[Simulation]) -> \
        Tuple[List[List[int]], List[float]]:
    # Calculate prior probabilities
    priors = methods[kwargs['method_for_calculating_priors']](spectra,
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

    print(f'used_components: {used_components}')
    print(f'diagnoses: {diagnoses}')

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
    print(f'pass_second: {[ps / len(error_vector) for ps in pass_second]}')

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
    'delay_and_wait_for_it': simulate_delay_and_wait_for_it,

    # Methods that determine a simulation success/fail
    'percentage_free_ca': simulation_success_method_percentage_free_ca,

    # Methods that determine the agents success/fail
    'reach_final_res': agent_success_method_reach_final_res,

    # Methods that determine how to populate the spectra
    'agent_pass_fail_contribution': error_vector_and_spectra_fill_method_agent_pass_fail_contribution,

    # Methods for calculating diagnoses and their probabilities
    'ochiai': calculate_diagnoses_and_probabilities_ochiai,
    'barinel_avi': calculate_diagnoses_and_probabilities_barinel_avi,
    'barinel_amir': calculate_diagnoses_and_probabilities_barinel_amir,

    # Methods for calculating priors
    'priors_one': calculate_priors_one,
    'priors_static': calculate_priors_static,
    'priors_intersections1': calculate_priors_intersections1,
    'priors_intersections2': calculate_priors_intersections2,

    # Methods for evaluating the algorithm
    'wasted_effort': evaluate_algorithm_wasted_effort,
    'precision_recall': evaluate_algorithm_precision_recall
}
