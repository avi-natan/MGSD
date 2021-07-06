import os
import shutil

from pipeline.scenario_builder import ScenarioBuilder
from pipeline.simulator import Simulator
from pipeline.spectra_generator import SpectraGenerator
from pipeline.world_builder import WorldBuilder

if __name__ == '__main__':
    print(f'Hi MGSD pipeline!')

    # at start, clean the worlds folder
    shutil.rmtree(f'../worlds')
    os.mkdir(f'../worlds')

    # important - to run static pipeline, insert 'static' in every argument that allows it

    # create various worlds
    world_builder = WorldBuilder('../boards', '../static/worlds', '../worlds')
    created_worlds_count = 0
    success = world_builder.build_world('intersection0', 6, 12, 19, 'static')
    if success:
        created_worlds_count += 1
    success = world_builder.build_world('intersection1', 6, 12, 18, 'static')
    if success:
        created_worlds_count += 1
    success = world_builder.build_world('tcircle0', 6, 12, 78, 'static')
    if success:
        created_worlds_count += 1
    print(f'created_worlds_count: {created_worlds_count}')

    # create scenarios
    worlds_contents = next(os.walk('../worlds'))
    world_names = list(map(lambda fn: fn[:-5], worlds_contents[2]))
    scenario_builder = ScenarioBuilder('../boards', '../static/worlds', '../worlds')
    created_scenarios_count = 0
    # iterate over the different worlds
    for wn in world_names:
        print(f'\ngenerating scenarios for world {wn}...')
        max_agent_size = int(wn.split('_')[5])
        # iterate over the agent numbers
        for an in range(3, max_agent_size + 1):
            # iterate over the faulty agent numbers
            for fan in range(1, an):
                # iterate over the fault probabilities
                for fp in [0.05, 0.1, 0.2, 0.3]:
                    # iterate over the number of simulations
                    for sn in range(10, 11):
                        success = scenario_builder.build_scenario(wn, an, fan, fp, sn, 'static')
                        if success:
                            created_scenarios_count += 1
    print(f'created_scenarios_count: {created_scenarios_count}')

    # run simulations and generate outcomes
    worlds_contents = next(os.walk('../worlds'))
    worlds_scenarios_folders = worlds_contents[1]
    simulator = Simulator('../boards', '../static/worlds', '../worlds')
    created_outcomes_count = 0
    for scenario_folder in worlds_scenarios_folders:
        scenario_folder_contents = next(os.walk(f'../worlds/{scenario_folder}'))
        scenario_names = list(map(lambda fn: fn[:-5], scenario_folder_contents[2]))
        for scenario_name in scenario_names:
            print(f'\ngenerating outcomes for {scenario_name} from {scenario_folder}...')
            success = simulator.generate_outcome(scenario_name,
                                                 f'../worlds/{scenario_folder}',
                                                 'dawfi',
                                                 {},
                                                 'static')
            if success:
                created_outcomes_count += 1
    print(f'created_outcomes_count: {created_outcomes_count}')

    # generate spectra
    worlds_contents = next(os.walk('../worlds'))
    worlds_scenarios_folders = worlds_contents[1]
    spectra_generator = SpectraGenerator('../boards', '../static/worlds', '../worlds')
    created_spectra_count = 0
    for scenario_folder in worlds_scenarios_folders:
        scenario_folder_contents = next(os.walk(f'../worlds/{scenario_folder}'))
        scenarios_outcomes_folders = scenario_folder_contents[1]
        for outcome_folder in scenarios_outcomes_folders:
            outcome_folder_contents = next(os.walk(f'../worlds/{scenario_folder}/{outcome_folder}'))
            outcome_names = list(map(lambda fn: fn[:-5], outcome_folder_contents[2]))
            for outcome_name in outcome_names:
                print(f'\ngenerating spectra for {outcome_name} from {scenario_folder}/{outcome_folder}...')
                success = spectra_generator.generate_spectra(outcome_name,
                                                             f'../worlds/{scenario_folder}/{outcome_folder}',
                                                             'pfc',             # percentage_free_ca
                                                             {'t': 0.95},       # threshold
                                                             'rfr',             # reach_final_res
                                                             {},
                                                             'apfc',            # agent_pass_fail_contribution
                                                             {'ifs': True},     # invert_for_success
                                                             'static')
                if success:
                    created_spectra_count += 1
    print(f'created_spectra_count: {created_spectra_count}')


    # run MGSD to generate diagnoses
