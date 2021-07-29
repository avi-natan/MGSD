import json
import os
import shutil
import random

import statics
from agent import Agent


class Simulator(object):

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

    def generate_outcome(self,
                         scenario_name,
                         scenario_path,
                         fault_and_conflict_method,
                         fault_and_conflict_method_args,
                         outcome_type):
        """
        Takes a scenario and runs the number of simulations specified in it, in order to generate an outcome. an
        outcome is an object defined by an array of simulations, that each of them contains a fault table and an
        actual execution.

        The resulting outcome will be encoded into a json object in the folder "<scenario_path>" under the name
        "outcome_facm_<fault_and_conflict_method>_facmargs_<fault_and_conflict_method_args>.json"
        and a folder named
        "outcome_facm_<fault_and_conflict_method>_facmargs_<fault_and_conflict_method_args>_spectras" will be created.

        :param scenario_name: the name of the scenario, without the .json extension
        :param scenario_path: the relative path to the folder containing the scenario
        :param fault_and_conflict_method: name of the fault method when running the simulation
        :param fault_and_conflict_method_args: supporting arguments for the above method
        :param outcome_type: whether the outcome should be static or generated. specified by the datum [static,
        generated].
        in case of static, this function will load the static information about the agents defined for the
        specified scenario name.
        in case of generated, this function will use the provided methods to generate an outcome.
        :return: boolean indicator whether the generation succeeded
        """
        sc_name = scenario_name
        sc_path = scenario_path
        facm = fault_and_conflict_method
        facm_args = fault_and_conflict_method_args
        oc_type = outcome_type

        # 2nd order methods' arguments dicts as strings
        facm_args_string = '#'
        if facm_args == {}:
            facm_args_string += '#'
        else:
            for k, v in facm_args.items():
                facm_args_string += f'{str(k)}#{str(v)}#'

        # check that a outcome doesnt already exist
        outfile_path = f'{sc_path}/{sc_name}_outcomes/outcome_facm_{facm}_facmargs_{facm_args_string}.json'
        outdir_path = f'{sc_path}/{sc_name}_outcomes/outcome_facm_{facm}_facmargs_{facm_args_string}_spectras'
        if os.path.exists(outfile_path) and os.path.exists(outdir_path):
            print(f'outcome json {outfile_path[:-5]} exists, skipping...')
            return False

        # run the simulations and generate outcomes
        outcome_json = None
        if oc_type == 'static':
            outcome_json = self.static_outcome(sc_name, sc_path, facm, facm_args)
            pass
        elif oc_type == 'generated':
            outcome_json = self.generated_outcome(sc_name, sc_path, facm, facm_args, facm_args_string)
            # if outcome_json is None:
            #     print(f'found collisions, deleting scenario {sc_path}/{sc_name} outcomes folder and json file...')
            #     os.remove(f'{sc_path}/{sc_name}.json')
            #     shutil.rmtree(f'{sc_path}/{sc_name}_outcomes')
            #     raise Exception('found collisions')
            # pass
            while outcome_json is None:
                file1 = open(f"../number_of_collisions.txt", "a")
                file1.write(f"{sc_path}/{sc_name}.json\n")
                file1.close()
                s_json = json.load(open(f'{sc_path}/{sc_name}.json'))
                # Generate agents
                agents_json = []
                for i in range(int(s_json['parameters']['agents_number'])):
                    agent = {
                        "agent_num": i,
                        "agent_name": f"a{i}",
                        "agent_is_faulty": False,
                        "agent_fail_prob": 0.0
                    }
                    agents_json.append(agent)
                # randomly shuffle the list and add faults to the first <fan> agents
                random.shuffle(agents_json)
                for i in range(int(s_json['parameters']['faulty_agents_number'])):
                    agents_json[i]['agent_is_faulty'] = True
                    agents_json[i]['agent_fail_prob'] = float(s_json['parameters']['fault_probability'])
                # return list to its original order
                agents_json.sort(key=lambda a: a['agent_num'])
                s_json['agents'] = agents_json
                os.remove(f'{sc_path}/{sc_name}.json')
                with open(f'{sc_path}/{sc_name}.json', 'w') as outfile:
                    json.dump(s_json, outfile)
                outcome_json = self.generated_outcome(sc_name, sc_path, facm, facm_args, facm_args_string)
        else:
            raise Exception(f'unexpected outcome type: "{oc_type}"')

        # write outcome to disk
        if outcome_json is not None:
            print(f'sc_name: {sc_name}')
            print(f'sc_path: {sc_path}')
            print(f'facm: {facm}')
            print(f'facm_args: {facm_args}')
            print(f'oc_type: {oc_type}')
            facm_args_string = '#'
            if facm_args == {}:
                facm_args_string += '#'
            else:
                for k, v in facm_args.items():
                    facm_args_string += f'{str(k)}#{str(v)}#'
            # outfile_path = f'{sc_path}/{sc_name}_outcomes/outcome_facm_{facm}_facmargs_{facm_args_string}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(outcome_json, outfile)
            # outdir_path = f'{sc_path}/{sc_name}_outcomes/outcome_facm_{facm}_facmargs_{facm_args_string}_spectras'
            if not os.path.exists(outdir_path):
                os.mkdir(outdir_path)
            else:
                shutil.rmtree(outdir_path)
                os.mkdir(outdir_path)
            return True
        else:
            facm_args_string = '#'
            if facm_args == {}:
                facm_args_string += '#'
            else:
                for k, v in facm_args.items():
                    facm_args_string += f'{str(k)}#{str(v)}#'
            print(f'No valid outcome generated for outcome_facm_{facm}_facmargs_{facm_args_string}.json, skipping...')
            return False

    def static_outcome(self, sc_name, sc_path, facm, facm_args):
        static_sc_path = f'{self.static_worlds_relative_path[:9]}/{sc_path[3:]}'
        scenario_static_outcomes_contents = next(os.walk(f'{static_sc_path}/{sc_name}_outcomes'))
        scenario_static_outcomes_filenames = scenario_static_outcomes_contents[2]
        facm_args_string = '#'
        if facm_args == {}:
            facm_args_string += '#'
        else:
            for k, v in facm_args.items():
                facm_args_string += f'{str(k)}#{str(v)}#'
        scenario_static_outcome_filename = f'outcome_facm_{facm}_facmargs_{facm_args_string}.json'
        if scenario_static_outcome_filename not in scenario_static_outcomes_filenames:
            outcome_json = None
        else:
            outcome_json = json.load(open(
                f'{static_sc_path}/{sc_name}_outcomes/{scenario_static_outcome_filename}'))
        return outcome_json

    def generated_outcome(self, sc_name, sc_path, facm, facm_args, facm_args_string):
        scenario_json = json.load(open(f'{sc_path}/{sc_name}.json'))
        # Extract agents
        agents = []
        for i, a in enumerate(scenario_json['agents']):
            a_num = a['agent_num']
            a_name = a['agent_name']
            a_is_faulty = a['agent_is_faulty']
            a_fail_prob = a['agent_fail_prob']
            agent = Agent(num=a_num, name=a_name, is_faulty=a_is_faulty, fail_prob=a_fail_prob)
            agents.append(agent)

        # Extract plan
        plan = scenario_json['world']['plan']['individual_plans']

        # Use function from statics to generate simulations
        simulations_json = []
        for i in range(scenario_json['simulations_number']):
            fault_table, actual_execution = statics.methods[facm](agents, plan, facm_args)
            if fault_table is None and actual_execution is None:
                return None
            simulation = {
                "name": f"s{i}",
                "fault_table": fault_table,
                "actual_execution": actual_execution
            }
            simulations_json.append(simulation)

        outcome_json = {
            "outcome_name": f"{scenario_json['scenario_name']}_outcome_facm_{facm}_facmargs_{facm_args_string}",
            "parameters": {
                "scenario_name": f"{scenario_json['scenario_name']}",
                "facm": f"{facm}",
                "facmargs": f"{facm_args_string}",
                "outcome_type": "generated"
            },
            "scenario": scenario_json,
            "simulations": simulations_json
        }
        return outcome_json
