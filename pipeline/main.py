import json
import os
import shutil

import statics
from pipeline.diagnoser import Diagnoser
from pipeline.scenario_builder import ScenarioBuilder
from pipeline.simulator import Simulator
from pipeline.spectra_generator import SpectraGenerator
from pipeline.world_builder import WorldBuilder

if __name__ == '__main__':
    print(f'Hi MGSD pipeline!')

    # at start, clean the worlds folder
    shutil.rmtree(f'../worlds')
    os.mkdir(f'../worlds')

    # IMPORTANT - to run static pipeline, insert 'static' in every argument that allows it
    # IMPORTANT - MUST NOT USE STATIC AFTER USING GENERATED OR THIRD_PARTY

    # # all available parameters:
    # # worlds
    # worlds = [                                          # worlds (include map, critical areas and plans)
    #     ['intersection0', 6, 12, 19, 'static'],         # world name, number of plans, plans length, number of intersections
    #     ['intersection1', 6, 12, 18, 'static'],
    #     ['tcircle0', 6, 12, 78, 'static']
    # ]
    # # scenarios
    # ans = [3, 4, 5, 6]                                  # an - agents number
    # fans = [1, 2, 3, 4, 5]                              # fan - faulty agents number
    # fps = [0.05, 0.1, 0.2, 0.3]                         # fp - fault probabilities
    # sns = [10, 50, 100]                                 # sn - simulations number
    # # outcomes
    # facms = [                                           # facms - fault and conflict methods
    #     ['dawfi', {}]
    # ]
    # # spectras
    # ssms = [                                            # ssm - system success method
    #     ['pfc', {'t': 0.95}]                            # t - threshold
    # ]
    # asms = [                                            # asm - agent success method
    #     ['rfr', {}]
    # ]
    # evasfms = [                                         # apfc - error vector and spectra fill method
    #     ['apfc', {'ifs': True}]                         # ifs - invert for success
    # ]
    # # results
    # dpcms = [                                           # dpcm - diagnoses and probabilities calculation methods
    #     ['barinelavi', {'mfcp': 'pone'}],               # mfcp - method for calculating priors
    #     ['barinelavi', {'mfcp': 'pstatic'}],
    #     ['barinelavi', {'mfcp': 'pintersections1'}],
    #     ['barinelavi', {'mfcp': 'pintersections2'}],
    #     ['barinelamir', {'mfcp': 'pone'}],
    #     ['barinelamir', {'mfcp': 'pstatic'}],
    #     ['barinelamir', {'mfcp': 'pintersections1'}],
    #     ['barinelamir', {'mfcp': 'pintersections2'}]
    # ]

    # # chosen parameters:
    # worlds
    worlds = [                                          # worlds (include map, critical areas and plans)
        ['intersection0', 6, 12, 19, 'static'],       # world name, number of plans, plans length, number of intersections
        ['intersection1', 6, 12, 18, 'static'],
        ['tcircle0', 6, 12, 78, 'static'],
        # ['generated1', 6, 12, -1, 'thirdparty'],
        # ['generated2', 6, 12, -1, 'thirdparty'],
        # ['generated3', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty'],
        # ['intersection', 12, 12, -1, 'thirdparty']
    ]
    # scenarios
    ans = [6]                                           # an - agents number
    fans = [2]                                       # fan - faulty agents number
    fps = [0.1]                                         # fp - fault probabilities
    sns = [10]                                          # sn - simulations number
    # TODO: number of games
    # outcomes
    facms = [                                           # facms - fault and conflict methods
        ['dawfi', {}]
    ]
    # spectras
    ssms = [                                            # ssm - system success method
        ['pfc', {'t': 0.95}]                            # t - threshold
    ]
    asms = [                                            # asm - agent success method
        ['rfr', {}]
    ]
    evasfms = [                                         # apfc - error vector and spectra fill method
        ['apfc', {'ifs': True}]                         # ifs - invert for success
    ]
    # results
    dpcms = [                                           # dpcm - diagnoses and probabilities calculation methods
        ['barinelavi', {'mfcp': 'pone'}],               # mfcp - method for calculating priors
        # ['barinelavi', {'mfcp': 'pstatic'}],
        # ['barinelavi', {'mfcp': 'pintersections1'}],
        ['barinelavi', {'mfcp': 'pintersections2'}],
        # ['barinelamir', {'mfcp': 'pone'}],
        # ['barinelamir', {'mfcp': 'pstatic'}],
        # ['barinelamir', {'mfcp': 'pintersections1'}],
        # ['barinelamir', {'mfcp': 'pintersections2'}]
    ]

    # create various worlds
    world_builder = WorldBuilder('../boards', '../static/worlds', '../worlds')
    created_worlds_count = 0
    for world in worlds:
        success = world_builder.build_world(world[0], world[1], world[2], world[3], world[4])
        if success:
            created_worlds_count += 1
    print(f'created_worlds_count: {created_worlds_count}')
    # visualize worlds
    world_json_names = next(os.walk(f'../worlds'))[2]
    for world_json_name in world_json_names:
        world_json = json.load(open(f'../worlds/{world_json_name}'))
        plan = world_json['plan']['individual_plans']
        board = world_json['board']
        statics.visualize(plan, board)
        print(world_json_name)

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
        for an in ans:
            # iterate over the faulty agent numbers
            for fan in fans:
                # iterate over the fault probabilities
                for fp in fps:
                    # iterate over the number of simulations
                    for sn in sns:
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
            for facm in facms:
                success = simulator.generate_outcome(scenario_name,
                                                     f'../worlds/{scenario_folder}',
                                                     facm[0],
                                                     facm[1],
                                                     'generated')
                if success:
                    created_outcomes_count += 1
    print(f'created_outcomes_count: {created_outcomes_count}')

    # go over outcomes and generate spectras
    worlds_contents = next(os.walk('../worlds'))
    worlds_scenarios_folders = worlds_contents[1]
    spectra_generator = SpectraGenerator('../boards', '../static/worlds', '../worlds')
    created_spectra_count = 0
    for scenario_folder in worlds_scenarios_folders:
        scenario_folder_contents = next(os.walk(f'../worlds/{scenario_folder}'))
        scenario_outcomes_folders = scenario_folder_contents[1]
        for outcome_folder in scenario_outcomes_folders:
            outcome_folder_contents = next(os.walk(f'../worlds/{scenario_folder}/{outcome_folder}'))
            outcome_names = list(map(lambda fn: fn[:-5], outcome_folder_contents[2]))
            for outcome_name in outcome_names:
                print(f'\ngenerating spectra for {outcome_name} from {scenario_folder}/{outcome_folder}...')
                for ssm in ssms:
                    for asm in asms:
                        for evasfm in evasfms:
                            success = spectra_generator.generate_spectra(outcome_name,
                                                                         f'../worlds/{scenario_folder}/{outcome_folder}',
                                                                         ssm[0],  # percentage_free_ca
                                                                         ssm[1],  # threshold
                                                                         asm[0],  # reach_final_res
                                                                         asm[1],
                                                                         evasfm[0],  # agent_pass_fail_contribution
                                                                         evasfm[1],  # invert_for_success
                                                                         'generated')
                            if success:
                                created_spectra_count += 1
    print(f'created_spectra_count: {created_spectra_count}')

    # go over spectras and generate results
    worlds_contents = next(os.walk('../worlds'))
    worlds_scenarios_folders = worlds_contents[1]
    diagnoser = Diagnoser('../boards', '../static/worlds', '../worlds')
    created_results_count = 0
    for scenario_folder in worlds_scenarios_folders:
        scenario_folder_contents = next(os.walk(f'../worlds/{scenario_folder}'))
        scenario_outcomes_folders = scenario_folder_contents[1]
        for outcome_folder in scenario_outcomes_folders:
            outcome_folder_contents = next(os.walk(f'../worlds/{scenario_folder}/{outcome_folder}'))
            outcome_spectras_folders = outcome_folder_contents[1]
            for spectra_folder in outcome_spectras_folders:
                spectra_folder_contents = next(
                    os.walk(f'../worlds/{scenario_folder}/{outcome_folder}/{spectra_folder}'))
                spectra_names = list(map(lambda fn: fn[:-5], spectra_folder_contents[2]))
                for spectra_name in spectra_names:
                    print(
                        f'\ngenerating result for {spectra_name} from {scenario_folder}/{outcome_folder}/{spectra_folder}...')
                    for dpcm in dpcms:
                        try:
                            success = diagnoser.diagnose(spectra_name,
                                                         f'../worlds/{scenario_folder}/{outcome_folder}/{spectra_folder}',
                                                         dpcm[0],  # barinel_amir
                                                         dpcm[1],  # method_for_calculating_priors - priors_one
                                                         'generated')
                        except IndexError as e:
                            print('Index Error')
                            success = False
                        if success:
                            created_results_count += 1
                        print('')
    print(f'created_results_count: {created_results_count}')

    print(f'final:')
    print(f'created_worlds_count: {created_worlds_count}')
    print(f'created_scenarios_count: {created_scenarios_count}')
    print(f'created_outcomes_count: {created_outcomes_count}')
    print(f'created_spectra_count: {created_spectra_count}')
    print(f'created_results_count: {created_results_count}')
