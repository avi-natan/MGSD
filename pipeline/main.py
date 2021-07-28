import json
import math
import os
import shutil
import xlsxwriter
from datetime import datetime

import statics
from pipeline.diagnoser import Diagnoser
from pipeline.scenario_builder import ScenarioBuilder
from pipeline.simulator import Simulator
from pipeline.spectra_generator import SpectraGenerator
from pipeline.world_builder import WorldBuilder

if __name__ == '__main__':
    print(f'Hi MGSD pipeline!')
    start_time = datetime.now()

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
    # scn = 1                                             # scn - scenarios number
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
        # ['intersection0', 6, 12, 19, 'static'],       # world name, number of plans, plans length, number of intersections
        # ['intersection1', 6, 12, 18, 'static'],
        # ['tcircle0', 6, 12, 78, 'static'],
        # ['intersection', 12, 12, 70, 'static'],
        ['intersection', 6, 12, 30, 'static'],
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
    sns = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]                                          # sn - simulations number
    scn = 10                                            # scn - scenarios number
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
        ['ochiai', {}],
        ['tarantula', {}],
        ['barinelavi', {'mfcp': 'pone'}],               # mfcp - method for calculating priors
        # ['barinelavi', {'mfcp': 'pstatic'}],
        ['barinelavi', {'mfcp': 'pintersections1'}],
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
                        for s in range(scn):
                            success = scenario_builder.build_scenario(wn, an, fan, fp, sn, s, 'generated')
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
                        print(f'sn: {spectra_name}')
                        print(f"sp: {f'../worlds/{scenario_folder}/{outcome_folder}/{spectra_folder}'}")
                        print(f'dpcm: {dpcm[0]}')
                        print(f'dpcm_args: {dpcm[1]}')
                        success = diagnoser.diagnose(spectra_name,
                                                     f'../worlds/{scenario_folder}/{outcome_folder}/{spectra_folder}',
                                                     dpcm[0],  # barinel_amir
                                                     dpcm[1],  # method_for_calculating_priors - priors_one
                                                     'generated')
                        if success:
                            created_results_count += 1
                        spectra_json = json.load(
                            open(f'../worlds/{scenario_folder}/{outcome_folder}/{spectra_folder}/{spectra_name}.json'))
                        print(f'Conflict matrix:')
                        for i, row in enumerate(spectra_json['conflict_matrix']):
                            print(f'{row}')
                        print(f'spectra and error vector:')
                        for i, row in enumerate(spectra_json['spectra_matrix']):
                            print(f'{row} | {spectra_json["error_vector"][i]}')
                        print('')
    print(f'created_results_count: {created_results_count}')

    print(f'final:')
    print(f'created_worlds_count: {created_worlds_count}')
    print(f'created_scenarios_count: {created_scenarios_count}')
    print(f'created_outcomes_count: {created_outcomes_count}')
    print(f'created_spectra_count: {created_spectra_count}')
    print(f'created_results_count: {created_results_count}')

    print(f'collecting results to excel...')
    # prepare the data
    all_json_paths = []
    worlds_folders = next(os.walk(f'../worlds'))[1]
    for wf in worlds_folders:
        scenarios_folders = next(os.walk(f'../worlds/{wf}'))[1]
        for scf in scenarios_folders:
            outcomes_folders = next(os.walk(f'../worlds/{wf}/{scf}'))[1]
            for of in outcomes_folders:
                spectras_folders = next(os.walk(f'../worlds/{wf}/{scf}/{of}'))[1]
                for spf in spectras_folders:
                    results_files = next(os.walk(f'../worlds/{wf}/{scf}/{of}/{spf}'))[2]
                    valid = 1
                    for rf in results_files:
                        js = json.load(open(f'../worlds/{wf}/{scf}/{of}/{spf}/{rf}'))
                        if js['diagnoses'] == '-':
                            valid = 0
                    for rf in results_files:
                        all_json_paths.append([f'../worlds/{wf}/{scf}/{of}/{spf}/{rf}', valid])
    data = []
    invalid_results_num = 0
    valid_results_num = 0
    for jp in all_json_paths:
        result_json = json.load(open(f'{jp[0]}'))
        result_row = []
        result_row.append(result_json['spectra']['outcome']['scenario']['world']['board']['board_name'])
        result_row.append(result_json['spectra']['outcome']['scenario']['world']['board']['board_width'])
        result_row.append(result_json['spectra']['outcome']['scenario']['world']['board']['board_height'])
        result_row.append('\r\n'.join(list(map(lambda arr: str(arr), result_json['spectra']['outcome']['scenario']['world']['board']['board_critical_areas']))))
        result_row.append(int(result_json['spectra']['outcome']['scenario']['world']['plan']['size']))
        result_row.append(int(result_json['spectra']['outcome']['scenario']['world']['plan']['length']))
        result_row.append(int(result_json['spectra']['outcome']['scenario']['world']['plan']['intersections']))
        result_row.append(result_json['spectra']['outcome']['scenario']['parameters']['agents_number'])
        result_row.append(result_json['spectra']['outcome']['scenario']['parameters']['faulty_agents_number'])
        result_row.append(result_json['spectra']['outcome']['scenario']['parameters']['fault_probability'])
        result_row.append(result_json['spectra']['outcome']['scenario']['parameters']['simulations_number'])
        result_row.append(result_json['spectra']['outcome']['scenario']['parameters']['scenario_number'])
        result_row.append(result_json['spectra']['outcome']['parameters']['facm'])
        result_row.append(result_json['spectra']['outcome']['parameters']['facmargs'])
        result_row.append(result_json['spectra']['parameters']['ssm'])
        result_row.append(result_json['spectra']['parameters']['ssmargs'])
        result_row.append(result_json['spectra']['parameters']['asm'])
        result_row.append(result_json['spectra']['parameters']['asmargs'])
        result_row.append(result_json['spectra']['parameters']['evasfm'])
        result_row.append(result_json['spectra']['parameters']['evasfmargs'])
        result_row.append(result_json['parameters']['dpcm'])
        result_row.append(result_json['parameters']['dpcmargs'])
        result_row.append('\r\n'.join(list(map(lambda arr: str(arr), result_json['spectra']['conflict_matrix']))))
        result_row.append('\r\n'.join(list(map(lambda arr: str(arr), result_json['spectra']['spectra_matrix']))))
        result_row.append('\r\n'.join(list(map(lambda num: str(num), result_json['spectra']['error_vector']))))
        result_row.append('\r\n'.join(list(map(lambda dic: str(dic), result_json['diagnoses']))))
        result_row.append(str([a['agent_num'] for a in result_json['spectra']['outcome']['scenario']['agents'] if a['agent_is_faulty']]))
        result_row.append(result_json['metrics']['wasted_effort'])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 10.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 20.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 30.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 40.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 50.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 60.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 70.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 80.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 90.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_precision'][math.ceil(len(result_json['metrics']['weighted_precision']) * 99.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 10.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 20.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 30.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 40.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 50.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 60.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 70.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 80.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 90.0 / 100)-1])
        result_row.append(result_json['metrics']['weighted_recall'][math.ceil(len(result_json['metrics']['weighted_recall']) * 99.0 / 100)-1])
        result_row.append(jp[1])
        data.append(result_row)
        if jp[1] == 1:
            valid_results_num += 1
        else:
            invalid_results_num += 1
    columns = [
        {'header': 'board_name'},
        {'header': 'board_width'},
        {'header': 'board_height'},
        {'header': 'board_critical_areas'},
        {'header': 'plan_size'},
        {'header': 'plan_length'},
        {'header': 'intersections_number'},
        {'header': 'agents_number'},
        {'header': 'faulty_agents_number'},
        {'header': 'fault_probability'},
        {'header': 'simulations_number'},
        {'header': 'scenario_number'},
        {'header': 'facm'},
        {'header': 'facmargs'},
        {'header': 'ssm'},
        {'header': 'ssmargs'},
        {'header': 'asm'},
        {'header': 'asmargs'},
        {'header': 'evasfm'},
        {'header': 'evasfmargs'},
        {'header': 'dpcm'},
        {'header': 'dpcmargs'},
        {'header': 'conflict_matrix'},
        {'header': 'spectra_matrix'},
        {'header': 'error_vector'},
        {'header': 'diagnoses_probabilities'},
        {'header': 'oracle'},
        {'header': 'wasted_effort'},
        {'header': 'weighted_precision_10'},
        {'header': 'weighted_precision_20'},
        {'header': 'weighted_precision_30'},
        {'header': 'weighted_precision_40'},
        {'header': 'weighted_precision_50'},
        {'header': 'weighted_precision_60'},
        {'header': 'weighted_precision_70'},
        {'header': 'weighted_precision_80'},
        {'header': 'weighted_precision_90'},
        {'header': 'weighted_precision_100'},
        {'header': 'weighted_recall_10'},
        {'header': 'weighted_recall_20'},
        {'header': 'weighted_recall_30'},
        {'header': 'weighted_recall_40'},
        {'header': 'weighted_recall_50'},
        {'header': 'weighted_recall_60'},
        {'header': 'weighted_recall_70'},
        {'header': 'weighted_recall_80'},
        {'header': 'weighted_recall_90'},
        {'header': 'weighted_recall_100'},
        {'header': 'valid'},
    ]

    # write the data to xlsx file
    workbook = xlsxwriter.Workbook('../results.xlsx')
    worksheet = workbook.add_worksheet('results')
    worksheet.add_table(0, 0, len(data), len(columns)-1, {'data': data, 'columns': columns})
    workbook.close()
    print(f'{valid_results_num}/{valid_results_num + invalid_results_num} results collected')

    end_time = datetime.now()
    delta = end_time - start_time
    print(f'time to finish: {delta}')

    print(f'Bye MGSD pipeline!')
