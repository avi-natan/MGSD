import json
import os
import shutil

import statics
import utils
from agent import Agent
from board import Board
from plan import Plan
from simulation import Simulation


class SpectraGenerator(object):

    def __init__(self, boards_relative_path, static_worlds_relative_path, worlds_relative_path):
        if not os.path.isdir(boards_relative_path):
            raise Exception('boards relative path not found')
        if not os.path.isdir(static_worlds_relative_path):
            raise Exception('static worlds relative path not found')
        if not os.path.isdir(worlds_relative_path):
            raise Exception('worlds relative path not found')
        self.boards_relative_path = boards_relative_path
        self.boards_relative_path_contents = next(os.walk(self.boards_relative_path))
        self.static_worlds_relative_path = static_worlds_relative_path
        self.static_worlds_relative_path_contents = next(os.walk(self.static_worlds_relative_path))
        self.worlds_relative_path = worlds_relative_path
        self.worlds_relative_path_contents = next(os.walk(self.worlds_relative_path))

    def generate_spectra(self,
                         outcome_name,
                         outcome_path,
                         simulation_success_method,
                         ssm_args,
                         agent_success_method,
                         asm_args,
                         error_vector_and_spectra_fill_method,
                         evasfm_args,
                         spectra_type):
        """
        Takes an outcome and generates a spectra according to the specified methods. a spectra is an object defined
        by a matrix of ones and zeros (individual agents success indicators) and vector of ones and zeros (an error
        vector, indicating the outcomes success).

        The resulting spectra will be encoded into a json object in the folder "<outcome_path>_spectras" under the name
        "spectra_ssm_<simulation_success_method>_ssmargs_<ssm_args>_asm_<agent_success_method>
        _asmargs_<asm_args>_evasfm_<error_vector_and_spectra_fill_method>_evasfmargs_<evasfm_args>.json"
        and a folder named
        "spectra_ssm_<simulation_success_method>_ssmargs_<ssm_args>_asm_<agent_success_method>
        _asmargs_<asm_args>_evasfm_<error_vector_and_spectra_fill_method>_evasfmargs_<evasfm_args>_diagnoses"
        will be created.

        :param outcome_name: the name of the outcome, without the .json extension
        :param outcome_path: the relative path to the folder containing the outcome
        :param simulation_success_method: name of the method that will determine a simulation success/fail
        :param ssm_args: supporting arguments for the above method
        :param agent_success_method: name of the method that will determine the agents success/fail
        :param asm_args: supporting arguments for the above method
        :param error_vector_and_spectra_fill_method: name of the method that will determine how to populate the spectra
        :param evasfm_args: supporting arguments for the above method
        :param spectra_type: whether the spectra should be static or generated. specified by the datum [static,
        generated].
        in case of static, this function will load a statically defined spectra.
        in case of generated, this function will use the provided methods to generate a spectra.
        :return: boolean indicator whether the generation succeeded
        """
        # shorter arguments
        on = outcome_name
        op = outcome_path
        ssm = simulation_success_method
        ssm_args = ssm_args
        asm = agent_success_method
        asm_args = asm_args
        evasfm = error_vector_and_spectra_fill_method
        evasfm_args = evasfm_args
        sp_type = spectra_type

        # 2nd order methods' arguments dicts as strings
        ssm_args_string = '#'
        if ssm_args == {}:
            ssm_args_string += '#'
        else:
            for k, v in ssm_args.items():
                ssm_args_string += f'{str(k)}#{str(v)}#'
        asm_args_string = '#'
        if asm_args == {}:
            asm_args_string += '#'
        else:
            for k, v in asm_args.items():
                asm_args_string += f'{str(k)}#{str(v)}#'
        evasfm_args_string = '#'
        if evasfm_args == {}:
            evasfm_args_string += '#'
        else:
            for k, v in evasfm_args.items():
                evasfm_args_string += f'{str(k)}#{str(v)}#'

        # check that a spectra doesnt already exist
        spectra_short_name = utils.spectra_names_dict[f'spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}'
                                                      f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs'
                                                      f'_{evasfm_args_string}']
        outfile_path = f'{op}/{on}_spectras/{spectra_short_name}.json'
        outdir_path = f'{op}/{on}_spectras/{spectra_short_name}_results'
        if os.path.exists(outfile_path) and os.path.exists(outdir_path):
            print(f'spectra json {outfile_path[:-5]} exists, skipping...')
            return False

        # static or generated generation
        spectra_json = None
        if sp_type == 'static':
            spectra_json = self.static_spectra(on, op, ssm, ssm_args, ssm_args_string, asm, asm_args,
                                               asm_args_string, evasfm, evasfm_args, evasfm_args_string)
            pass
        elif sp_type == 'generated':
            spectra_json = self.generated_spectra(on, op, ssm, ssm_args, ssm_args_string, asm, asm_args,
                                                  asm_args_string, evasfm, evasfm_args, evasfm_args_string)
        else:
            raise Exception(f'unexpected outcome type: "{sp_type}"')

        # write spectra to disk
        if spectra_json is not None:
            print(f'on: {on}')
            print(f'op: {op}')
            print(f'ssm: {ssm}')
            print(f'ssm_args: {ssm_args}')
            print(f'asm: {asm}')
            print(f'asm_args: {asm_args}')
            print(f'evasfm: {evasfm}')
            print(f'evasfm_args: {evasfm_args}')

            # spectra_short_name = utils.spectra_names_dict[f'spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}'
            #                                               f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs'
            #                                               f'_{evasfm_args_string}']
            # outfile_path = f'{op}/{on}_spectras/{spectra_short_name}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(spectra_json, outfile)
            # outdir_path = f'{op}/{on}_spectras/{spectra_short_name}_results'
            if not os.path.exists(outdir_path):
                os.mkdir(outdir_path)
            else:
                shutil.rmtree(outdir_path)
                os.mkdir(outdir_path)
            return True
        else:
            print(f'No valid spectra generated for spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}'
                  f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs_{evasfm_args_string}.json, skipping...')
            return False

    def static_spectra(self, on, op, ssm, ssm_args, ssm_args_string, asm, asm_args,
                       asm_args_string, evasfm, evasfm_args, evasfm_args_string):
        static_o_path = f'{self.static_worlds_relative_path[:9]}/{op[3:]}'
        outcome_static_spectras_contents = next(os.walk(f'{static_o_path}/{on}_spectras'))
        outcome_static_spectras_filenames = outcome_static_spectras_contents[2]
        spectra_short_name = utils.spectra_names_dict[f'spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}'
                                                      f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs'
                                                      f'_{evasfm_args_string}']
        outcome_static_spectra_filename = f'{spectra_short_name}.json'
        if outcome_static_spectra_filename not in outcome_static_spectras_filenames:
            scenario_json = None
        else:
            scenario_json = json.load(open(
                f'{static_o_path}/{on}_spectras/{outcome_static_spectra_filename}'))
        return scenario_json

    def generated_spectra(self, on, op, ssm, ssm_args, ssm_args_string, asm, asm_args,
                          asm_args_string, evasfm, evasfm_args, evasfm_args_string):
        # Create the simulations objects
        simulations_to_run = []
        outcome_json = json.load(open(f'{op}/{on}.json'))
        # board
        b_name = outcome_json['scenario']['world']['board']['board_name']
        b_width = outcome_json['scenario']['world']['board']['board_width']
        b_height = outcome_json['scenario']['world']['board']['board_height']
        b_critical_areas = outcome_json['scenario']['world']['board']['board_critical_areas']
        b_obstacles = outcome_json['scenario']['world']['board']['board_obstacles']
        board = Board(b_name, b_width, b_height, b_critical_areas, b_obstacles)
        # plan
        p_size = outcome_json['scenario']['world']['plan']['size']
        p_length = outcome_json['scenario']['world']['plan']['length']
        p_intersections = outcome_json['scenario']['world']['plan']['intersections']
        p_individual_plans = outcome_json['scenario']['world']['plan']['individual_plans']
        plan = Plan(p_size, p_length, p_intersections, p_individual_plans)
        # agents
        agents = []
        for i, a in enumerate(outcome_json['scenario']['agents']):
            a_num = a['agent_num']
            a_name = a['agent_name']
            a_is_faulty = a['agent_is_faulty']
            a_fail_prob = a['agent_fail_prob']
            agent = Agent(num=a_num, name=a_name, is_faulty=a_is_faulty, fail_prob=a_fail_prob)
            agents.append(agent)

        for i, sim in enumerate(outcome_json['simulations']):
            s_name = sim['name']
            s_board = board
            s_plan = plan.individual_plans  # TODO: refactor simulation later to use Plan object
            s_agents = agents
            s_fault_table = sim['fault_table']
            s_actual_execution = sim['actual_execution']
            simulation = Simulation(name=s_name, board=s_board, plans=s_plan, agents=s_agents)
            simulation.delay_table = s_fault_table
            simulation.outcome = s_actual_execution
            simulations_to_run.append(simulation)

        # count agent conflicts from actual executions and put it into matrix like the spectra
        conflict_matrix = statics.count_actual_execution_conflicts(outcome_json)

        # generate the error vector and the spectra
        error_vector, spectra_matrix = statics.methods[evasfm](
            simulations_to_run,
            ssm,
            ssm_args,
            asm,
            asm_args,
            evasfm_args
        )
        spectra_json = {
            "spectra_name": f"{outcome_json['outcome_name']}_spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}"
                            f"_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs_{evasfm_args_string}",
            "parameters": {
                "outcome_name": f"{outcome_json['outcome_name']}",
                "ssm": f"{ssm}",
                "ssmargs": f"{ssm_args_string}",
                "asm": f"{asm}",
                "asmargs": f"{asm_args_string}",
                "evasfm": f"{evasfm}",
                "evasfmargs": f"{evasfm_args_string}",
                "spectra_type": "generated"
            },
            "outcome": outcome_json,
            "conflict_matrix": conflict_matrix,
            "spectra_matrix": spectra_matrix,
            "error_vector": error_vector
        }
        return spectra_json
