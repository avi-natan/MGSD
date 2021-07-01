import consts
import statics
from simulation import Simulation

from typing import List, Dict


class MGSD(object):
    def __init__(self,
                 fault_and_conflict_method: str,
                 facm_args: Dict,
                 simulation_success_method: str,
                 ssm_args: Dict,
                 agent_success_method: str,
                 asm_args: Dict,
                 error_vector_and_spectra_fill_method: str,
                 evsfm_args: Dict,
                 diagnoses_and_probabilities_calculation_method: str,
                 dpcm_args: Dict,
                 evaluation_method: str,
                 em_args: Dict) -> None:
        """
        Initializes the Multi Game SFL based Diagnosis (MGSD) Algorithm, with the following
        custom calculation methods

        :param fault_and_conflict_method: name of the fault method when running the simulation
        :param facm_args: supporting arguments for the above function
        :param simulation_success_method: name of the function that will determine a simulation success/fail
        :param ssm_args: supporting arguments for the above function
        :param agent_success_method: name of the function that will determine the agents success/fail
        :param asm_args: supporting arguments for the above function
        :param error_vector_and_spectra_fill_method: name of the function that will determine how to populate the
               spectra
        :param evsfm_args: supporting arguments for the above function
        :param diagnoses_and_probabilities_calculation_method: the method for calculating diagnoses and probabilities
        :param dpcm_args: supporting arguments for the above function
        :param evaluation_method: the method for evaluating the algorithm
        :param em_args: supporting arguments for the above function
        :return: Nothing
        """
        self.fault_and_conflict_method = fault_and_conflict_method
        self.facm_args = facm_args
        self.simulation_success_method = simulation_success_method
        self.ssm_args = ssm_args
        self.agent_success_method = agent_success_method
        self.asm_args = asm_args
        self.error_vector_and_spectra_fill_method = error_vector_and_spectra_fill_method
        self.evsfm_args = evsfm_args
        self.diagnoses_and_probabilities_calculation_method = diagnoses_and_probabilities_calculation_method
        self.dpcm_args = dpcm_args
        self.evaluation_method = evaluation_method
        self.em_args = em_args
        self.simulations_to_run: List[Simulation] = []
        self.error_vector: List[int] = []
        self.spectra: List[List[int]] = []
        self.diagnoses: List[List[int]] = []
        self.probabilities: List[float] = []
        self.evaluation_results: Dict = {}

    def run_algorithm(self, config_filename: str = None) -> None:
        """
        Runs the algorithm for simulations specified in an input filename.
        In absence of such filename, the algorithm loads a custom made simulations.

        :param config_filename: Specifies the simulations to run
        :return: Nothing
        """
        if config_filename is None:
            print('No input file specified, running algorithm with default simulations')
            self.simulations_to_run = statics.get_hardcoded_simulations()
            # for i, s in enumerate(self.simulations_to_run):
            #     s.summary()
            # no simulating. the outcome is already included
        else:
            self.simulations_to_run = statics.get_from_filename(config_filename)
            # for i, s in enumerate(self.simulations_to_run):
            #     s.summary()
            for i, s in enumerate(self.simulations_to_run):
                s.simulate(self.fault_and_conflict_method, self.facm_args)

        for i, s in enumerate(self.simulations_to_run):
            print(f'[mgsd::run_algorithm] Simulation name: {s.name}')
            statics.print_matrix('plan', s.plans)
            statics.print_matrix('delay_table', s.delay_table)
            statics.print_matrix('outcome', s.outcome)
            print('')

        print(f'faulty agents: {list(map(lambda ag: [ag.name, ag.fail_prob], filter(lambda agent: agent.is_faulty, self.simulations_to_run[0].agents)))}')
        print('')

        self.calculate_error_vector_spectra()
        self.print_error_vector_spectra()
        self.calculate_diagnoses_and_probabilities()
        self.print_diagnoses_and_probabilities()
        self.evaluate_algorithm()
        self.print_evaluation_results()
        # self.visualize_output()
        print('fin')

    def calculate_error_vector_spectra(self):
        print('Calculating spectra and error vector...')
        self.error_vector, self.spectra = statics.methods[self.error_vector_and_spectra_fill_method](
            self.simulations_to_run,
            self.simulation_success_method,
            self.ssm_args,
            self.agent_success_method,
            self.asm_args,
            self.evsfm_args
        )
        print('Spectra and error vector calculated.\n')

    def calculate_diagnoses_and_probabilities(self):
        print('Calculating diagnoses and probabilities...')
        self.diagnoses, self.probabilities = \
            statics.methods[self.diagnoses_and_probabilities_calculation_method](self.spectra,
                                                                                 self.error_vector,
                                                                                 self.dpcm_args,
                                                                                 self.simulations_to_run)
        print('Diagnoses and probabilities calculated.\n')

    def evaluate_algorithm(self):
        print('Evaluating algorithm...')
        self.evaluation_results = statics.methods[self.evaluation_method](self.em_args)
        print('Algorithm evaluated.\n')

    def print_error_vector_spectra(self) -> None:
        print('Printing spectra and error vector:')
        for j in range(len(self.spectra)):
            for i in range(len(self.spectra[0])):
                print(f'{self.spectra[j][i]} ', end='')
            print(f'| {self.error_vector[j]}')
        print('\n')

    def print_diagnoses_and_probabilities(self) -> None:
        print('Printing diagnoses and probabilities:')
        for i, d in enumerate(self.diagnoses):
            print(f'{d}, {self.probabilities[i]}')
        print('\n')

    def print_evaluation_results(self) -> None:
        print(f'Printing evaluation results:')
        print(self.evaluation_results)
        print('\n')

    def visualize_output(self) -> None:
        for i, s in enumerate(self.simulations_to_run):
            s.visualize(what='plans')
            s.visualize(what='outcome')
