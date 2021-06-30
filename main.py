# MGSD - Multi Game SFL based Diagnosis
import os
import json
import random

import consts
from mgsd import MGSD

def print_hi(name: str) -> None:
    print(f'Hi, {name}')

def sandbox() -> None:
    """
    Sandbox for testing
    :return: nothing
    """

    # # Testing constructors
    # tests.test_empty_constructors()
    # tests.test_board_constructors()
    # tests.test_agent_constructors()
    # tests.test_simulation_constructors()

    # # Testing colors
    # tests.test_simulation_agent_colors()

    # # Testing custom scenarios creation
    # tests.test_custom_scenarios_creation()

    # # Testing simulation
    # tests.test_simulate()

def generate_benchmarks(agents_counts,
        faulty_agents_counts,
        faulty_agents_fail_probs,
        boards,
        plans_length,
        plans_intersections_count,
        plans_type,
        simulations_count) -> None:
    """
    :param agents_counts:                           ac
    :param faulty_agents_counts:                    fac
    :param faulty_agents_fail_probs:                fafp
    :param boards:                                  b
    :param plans_type:                              pt
    :param plans_length:                            pl
    :param plans_intersections_count:               pic
    :param simulations_count                        sc
    :return: nothing
    """

    # Delete old benchmarks
    benchmarks_dir = 'benchmarks'
    for f in os.listdir(benchmarks_dir):
        os.remove(os.path.join(benchmarks_dir, f))

    # generate new benchmarks
    generated_benchmarks_amount = 0
    for ac in agents_counts:
        print(f'ac: {ac}')
        for fac in faulty_agents_counts:
            print(f'\tfac: {fac}')
            for fafp in faulty_agents_fail_probs:
                print(f'\t\tfafp: {fafp}')
                for b in boards:
                    print(f'\t\t\tb: {b}')
                    for pl in plans_length:
                        print(f'\t\t\t\tpl: {pl}')
                        for pic in plans_intersections_count:
                            print(f'\t\t\t\t\tpic: {pic}')
                            for pt in plans_type:
                                print(f'\t\t\t\t\t\tpt: {pt}')
                                for sc in simulations_count:
                                    print(f'\t\t\t\t\t\t\tsc: {sc}')
                                    benchmark_name = f'benchmark#ac-{ac}#fac-{fac}#fafp-{fafp}#b-{b}#' \
                                                     f'pl-{pl}#pic-{pic}#pt-{pt}#sc-{sc}'
                                    print(f'\t\t\t\t\t\t\t\tbenchmark: {benchmark_name}')
                                    benchmark_data = {}
                                    # adding the agents to the json (ac, fac, fafp)
                                    faulty_agents_choice = [True] * fac + [False] * (ac-fac)
                                    random.shuffle(faulty_agents_choice)
                                    benchmark_data["agents"] = [{"agent_num": i,
                                                                 "agent_name": f"a{i}",
                                                                 "agent_is_faulty": faulty_agents_choice[i],
                                                                 "agent_fail_prob": fafp if faulty_agents_choice[i]
                                                                 else 0.0}
                                                                for i in range(len(faulty_agents_choice))]
                                    # adding the board to the json (b)
                                    benchmark_data["board"] = consts.boards[b]
                                    # adding plan to the json (pl, pic, pt)
                                    plan_name = f'{b}_plan_pl_{pl}_pic_{pic}'
                                    if pt == 'manual':
                                        plan = consts.plans['traffic_circle_plans'][plan_name]  # TODO: write manual plans for 10, 20, 30 intersections
                                    else:
                                        plan = consts.plans['traffic_circle_plans'][plan_name]  # TODO: implement generated plans
                                    benchmark_data["plan"] = {
                                        "plan_name": plan_name,
                                        "plan": plan
                                    }
                                    # adding simulations to the json (sc)
                                    benchmark_data["simulations"] = [{
                                        "simulation_num": i,
                                        "simulation_name": f"s{i}",
                                        "simulation_agent_nums": [i for i in range(ac)]
                                    } for i in range(sc)]
                                    with open(f'benchmarks/{benchmark_name}.json', 'w') as outfile:
                                        json.dump(benchmark_data, outfile)
                                    generated_benchmarks_amount += 1
    print(f'Amount of benchmarks generated: {generated_benchmarks_amount}')

def run_mgsd():
    # Create benchmark files
    # agents_counts = [6, 8, 10]
    # faulty_agents_counts = [2, 3, 4]
    # faulty_agents_fail_probs = [0.05, 0.1, 0.2, 0.3]
    # boards = ['intersection', 'traffic_circle']  # board must be manually built
    # plans_length = [10, 12, 14]
    # plans_intersections_count = [10, 20, 30]
    """
    'manual' or 'generated' in case of manual the generator will pick a manual plan that was created for that kind
    of board from the consts module.
    TODO: create ('plans_length' times 'plans_intersections_count') manual plans in consts module
    TODO: for every board (in the above case: 3 times 3 = 9). make sure that the plans are in custom made length and
    TODO: have the according number of intersections count
    """
    # plans_type = ['manual', 'generated']
    # simulations_count = [10, 15, 20]

    agents_counts = [6]
    faulty_agents_counts = [2]
    faulty_agents_fail_probs = [0.3]
    boards = ['traffic_circle']  # board must be manually built
    plans_length = [12]
    plans_intersections_count = [78]
    plans_type = ['manual', 'generated']
    simulations_count = [10]

    generate_benchmarks(
        agents_counts,
        faulty_agents_counts,
        faulty_agents_fail_probs,
        boards,
        plans_length,
        plans_intersections_count,
        plans_type,
        simulations_count
    )

    # Running the algorithm
    """
    Available parameters
    ====================
    Methods that determine the fault and conflict for the simulation
    * delay_and_wait_for_it
      - args: {}

    Methods that determine a simulation success/fail:
    * percentage_free_ca
      - args: {'threshold': float}

    Methods that determine the agents success/fail:
    * reach_final_res
      - args: {}

    Methods that determine how to populate the spectra:
    * agent_pass_fail_contribution
      - args: {'invert_for_success': bool}

    Methods for calculating diagnoses and their probabilities:
    * ochiai
      - args: {}
    * barinel_avi
      - args: {'method_for_calculating_priors': str
                                                <priors_one,
                                                priors_static,
                                                priors_amir,
                                                priors_paper,
                                                priors_intersections1,
                                                priors_intersections2>}
    * barinel_amir
      - args: {'method_for_calculating_priors': str <priors_one,
                                                priors_static,
                                                priors_amir,
                                                priors_paper,
                                                priors_intersections1,
                                                priors_intersections2>}

    Methods for evaluating the algorithm:
    * wasted_effort
      - args: {}
    * precision_recall
      - args: {}

    """
    mgsd: MGSD = MGSD('delay_and_wait_for_it',
                      {},
                      'percentage_free_ca',
                      {'threshold': 0.85},
                      'reach_final_res',
                      {},
                      'agent_pass_fail_contribution',
                      {'invert_for_success': True},
                      'barinel_amir',
                      {'method_for_calculating_priors': 'priors_one'},
                      'wasted_effort',
                      {})

    # Make sure that the file with the same name is located inside the
    # 'benchmarks' directory
    # mgsd.run_algorithm()
    for filename in os.listdir('benchmarks'):
        print(f'Running MGSD for benchmark: {filename}')
        mgsd.run_algorithm(config_filename=filename)


if __name__ == '__main__':
    print_hi('MGSD')
    # sandbox()
    run_mgsd()
