import json
import os
import shutil


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

        # run the simulations and generate outcomes
        outcome_json = None
        if oc_type == 'static':
            outcome_json = self.static_outcome(sc_name, sc_path, facm, facm_args)
            pass
        elif oc_type == 'generated':
            # TODO: implement
            pass
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
            outfile_path = f'{sc_path}/{sc_name}_outcomes/outcome_facm_{facm}_facmargs_{facm_args_string}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(outcome_json, outfile)
            outdir_path = f'{sc_path}/{sc_name}_outcomes/outcome_facm_{facm}_facmargs_{facm_args_string}_spectras'
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
            scenario_json = None
        else:
            scenario_json = json.load(open(
                f'{static_sc_path}/{sc_name}_outcomes/{scenario_static_outcome_filename}'))
        return scenario_json
