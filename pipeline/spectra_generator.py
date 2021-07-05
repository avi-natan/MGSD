import json
import os
import shutil

import statics


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
                         evasfm_args):
        """
        Takes an outcome and generates a spectra according to the specified methods. a spectra is an object defined
        by a matrix of ones and zeros (individual agents success indicators) and vector of ones and zeros (an error
        vector, indicating the outcomes success).

        The resulting spectra will be encoded into a json object in the folder "<outcome_path>" under the name
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
        :return: boolean indicator whether the generation succeeded
        """
        on = outcome_name
        op = outcome_path
        ssm = simulation_success_method
        ssm_args = ssm_args
        asm = agent_success_method
        asm_args = asm_args
        evasfm = error_vector_and_spectra_fill_method
        evasfm_args = evasfm_args

        # TODO:
        # simulations_to_run = []
        # error_vector, spectra = statics.methods[error_vector_and_spectra_fill_method](
        #     simulations_to_run,
        #     simulation_success_method,
        #     ssm_args,
        #     agent_success_method,
        #     asm_args,
        #     evasfm_args
        # )
        spectra_json = {}

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
            outfile_path = f'{op}/{on}_spectras/spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}' \
                           f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs_{evasfm_args_string}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(spectra_json, outfile)
            outdir_path = f'{op}/{on}_spectras/spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}' \
                          f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs_{evasfm_args_string}_diagnoses'
            if not os.path.exists(outdir_path):
                os.mkdir(outdir_path)
            else:
                shutil.rmtree(outdir_path)
                os.mkdir(outdir_path)
            return True
        else:
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
            print(f'No valid outcome generated for spectra_ssm_{ssm}_ssmargs_{ssm_args_string}_asm_{asm}'
                  f'_asmargs_{asm_args_string}_evasfm_{evasfm}_evasfmargs_{evasfm_args_string}.json, skipping...')
            return False
