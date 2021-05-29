import statics
from simulation import Simulation

from typing import List, Tuple, Callable, Dict


class MGSD(object):
    def __init__(self):
        self.simulations_to_run: List[Simulation] = []
        self.error_vector: List[int] = []
        self.spectra: List[List[int]] = []
        self.diagnoses: List[List[int]] = []
        self.probabilities: List[float] = []

    def run_algorithm(self, config_filename: str = None):
        if config_filename is None:
            print('No input file specified, running algorithm with default simulations')
            self.simulations_to_run = statics.get_hardcoded_simulations()
        else:
            self.simulations_to_run = statics.get_from_filename(config_filename)

        for i, s in enumerate(self.simulations_to_run):
            s.summary()

        for i, s in enumerate(self.simulations_to_run):
            s.simulate(debug_num=i)

        self.calculate_error_vector_spectra('percentage_free_ca',
                                            {'threshold': 0.85},
                                            'reach_final_res',
                                            {},
                                            'agent_pass_fail_contribution',
                                            {'invert_for_success': True})
        self.calculate_diagnoses_and_probabilities(method=statics.calculate_diagnoses_and_probabilities_ochiai)
        self.print_and_visualize_output()
        print('fin')

    def calculate_error_vector_spectra(
            self,
            simulation_success_method: str,
            ssm_args: Dict,
            agent_success_method: str,
            asm_args: Dict,
            error_vector_and_spectra_fill_method: str,
            evsfm_args: Dict):
        """

        :param simulation_success_method: name of the function that will determine a simulation success/fail
        :param ssm_args: supporting arguments for the above function
        :param agent_success_method: name of the function that will determine the agents success/fail
        :param asm_args: supporting arguments for the above function
        :param error_vector_and_spectra_fill_method: name of the function that will determine how to populate the
               spectra
        :param evsfm_args: supporting arguments for the above function
        :return:
        """
        print('Calculating spectra and error vector...')
        self.error_vector, self.spectra = statics.methods[error_vector_and_spectra_fill_method](
            self.simulations_to_run,
            simulation_success_method,
            ssm_args,
            agent_success_method,
            asm_args,
            evsfm_args
        )
        print('Spectra and error vector calculated.\n')

    def calculate_diagnoses_and_probabilities(self, method: Callable[[List[List[int]], List[int], Dict],
                                                                     Tuple[List[List[int]], List[float]]] = None):
        print('Calculating diagnoses and probabilities...')
        if method is None:
            self.diagnoses, self.probabilities = \
                statics.calculate_diagnoses_and_probabilities_ochiai(self.spectra, self.error_vector, {})
        else:
            self.diagnoses, self.probabilities = \
                method(self.spectra, self.error_vector, {})

        print('Diagnoses and probabilities calculated.\n')

    def print_and_visualize_output(self) -> None:
        print('\nPrinting and visualizing:')
        print('========================')
        print('Spectra and Error vector:')
        for j in range(len(self.spectra)):
            for i in range(len(self.spectra[0])):
                print(f'{self.spectra[j][i]} ', end='')
            print(f'| {self.error_vector[j]}')
        print(f'Diagnoses and probabilities:')
        for i, d in enumerate(self.diagnoses):
            print(f'{d}, {self.probabilities[i]}')
        print('')
        for i, s in enumerate(self.simulations_to_run):
            s.visualize(what='plans')
            s.visualize(what='outcome')
