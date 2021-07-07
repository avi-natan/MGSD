import json
import os

import statics
from agent import Agent
from board import Board
from plan import Plan
from simulation import Simulation


class Diagnoser(object):

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

    def diagnose(self,
                 spectra_name,
                 spectra_path,
                 diagnoses_and_probabilities_calculation_method,
                 dpcm_args,
                 result_type):
        """
        Takes a spectra and generates a result according to the specified methods. a result is an object defined
        by a list of diagnoses, and metrics for wasted effort, weighted precision and weighted recall. a diagnosis
        is defined as an array of agent numbers and a probability.

        The resulting result will be encoded into a json object in the folder <spectra_path>_results under the name
        <spectra_name>_dpcm_<diagnoses_and_probabilities_calculation_method>_dpcmargs_<dpcm_args>.json
        :param spectra_name: the name of the spectra, without the .json extension
        :param spectra_path: the relative path to the folder containing the spectra
        :param diagnoses_and_probabilities_calculation_method: the method for calculating diagnoses and probabilities
        :param dpcm_args: supporting arguments for the above method
        :param result_type: whether the result should be static or generated. specified by the datum [static,
        generated].
        in case of static, this method will load a statically defined result.
        in case of generated, this method will use the provided methods to generate a result.
        :return: boolean indicator whether the generation succeeded
        """
        # shorter arguments
        sn = spectra_name
        sp = spectra_path
        dpcm = diagnoses_and_probabilities_calculation_method
        dpcm_args = dpcm_args
        r_type = result_type

        # 2nd order methods' arguments dicts as strings
        dpcm_args_string = '#'
        if dpcm_args == {}:
            dpcm_args_string += '#'
        else:
            for k, v in dpcm_args.items():
                dpcm_args_string += f'{str(k)}#{str(v)}#'

        # satic or generated generation
        result_json = None
        if r_type == 'static':
            result_json = self.static_result(sn, sp, dpcm, dpcm_args, dpcm_args_string)
            pass
        elif r_type == 'generated':
            result_json = self.generated_result(sn, sp, dpcm, dpcm_args, dpcm_args_string)
        else:
            raise Exception(f'unexpected outcome type: "{r_type}"')

        # write result to disk
        if result_json is not None:
            print(f'sn: {sn}')
            print(f'sp: {sp}')
            print(f'dpcm: {dpcm}')
            print(f'dpcm_args: {dpcm_args}')

            result_name = f'result_dpcm_{dpcm}_dpcmargs_{dpcm_args_string}'
            outfile_path = f'{sp}/{sn}_results/{result_name}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(result_json, outfile)
            return True
        else:
            print(f'No valid result generated for result_dpcm_{dpcm}_dpcmargs_{dpcm_args_string}.json, skipping...')
            return False

    def static_result(self, sn, sp, dpcm, dpcm_args, dpcm_args_string):
        static_s_path = f'{self.static_worlds_relative_path[:9]}/{sp[3:]}'
        spectra_static_results_contents = next(os.walk(f'{static_s_path}/{sn}_results'))
        spectra_static_results_filenames = spectra_static_results_contents[2]
        spectra_static_result_filename = f'result_dpcm_{dpcm}_dpcmargs_{dpcm_args_string}.json'
        if spectra_static_result_filename not in spectra_static_results_filenames:
            scenario_json = None
        else:
            scenario_json = json.load(open(
                f'{static_s_path}/{sn}_results/{spectra_static_result_filename}'))
        return scenario_json

    def generated_result(self, sn, sp, dpcm, dpcm_args, dpcm_args_string):
        # Create the simulations objects
        simulations_to_run = []
        spectra_json = json.load(open(f'{sp}/{sn}.json'))
        # board
        b_name = spectra_json['outcome']['scenario']['world']['board']['board_name']
        b_width = spectra_json['outcome']['scenario']['world']['board']['board_width']
        b_height = spectra_json['outcome']['scenario']['world']['board']['board_height']
        b_critical_areas = spectra_json['outcome']['scenario']['world']['board']['board_critical_areas']
        board = Board(b_name, b_width, b_height, b_critical_areas)
        # plan
        p_size = spectra_json['outcome']['scenario']['world']['plan']['size']
        p_length = spectra_json['outcome']['scenario']['world']['plan']['length']
        p_intersections = spectra_json['outcome']['scenario']['world']['plan']['intersections']
        p_individual_plans = spectra_json['outcome']['scenario']['world']['plan']['individual_plans']
        plan = Plan(p_size, p_length, p_intersections, p_individual_plans)
        # agents
        agents = []
        for i, a in enumerate(spectra_json['outcome']['scenario']['agents']):
            a_num = a['agent_num']
            a_name = a['agent_name']
            a_is_faulty = a['agent_is_faulty']
            a_fail_prob = a['agent_fail_prob']
            agent = Agent(num=a_num, name=a_name, is_faulty=a_is_faulty, fail_prob=a_fail_prob)
            agents.append(agent)

        for i, sim in enumerate(spectra_json['outcome']['simulations']):
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

        # create the spectra matrix and the error vector
        spectra_matrix = spectra_json['spectra_matrix']
        error_vector = spectra_json['error_vector']

        diagnoses, probabilities = statics.methods[dpcm](spectra_matrix,
                                                         error_vector,
                                                         dpcm_args,
                                                         simulations_to_run)

        # create diagnoses objects
        diagnoses_json = []
        for i in range(len(diagnoses)):
            diagnosis = {
                "diagnosis": diagnoses[i],
                "probability": probabilities[i]
            }
            diagnoses_json.append(diagnosis)

        result_json = {
            "result_name": f"{spectra_json['spectra_name']}_result_dpcm_{dpcm}_dpcmargs_{dpcm_args_string}",
            "result_type": "generated",
            "spectra": spectra_json,
            "diagnoses": diagnoses_json,
            "metrics": {                    # TODO: implement
                "wasted_effort": 420,
                "weighted_precision": 420,
                "weighted_recall": 420
            }
        }
        return result_json
