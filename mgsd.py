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

        self.calculate_spectra_and_error_vector()
        self.calculate_diagnoses_and_probabilities(method=statics.calculate_diagnoses_and_probabilities_ochiai)
        self.print_and_visualize_output()
        print('fin')

    def calculate_spectra_and_error_vector(self):
        for i, s in enumerate(self.simulations_to_run):
            if s.simulation_pass:
                self.error_vector.append(0)
                self.spectra.append([])
                for j, _ in enumerate(s.outcome):
                    if s.agent_pass[j]:
                        self.spectra[i].append(1)  # Original
                        # self.spectra[i].append(0)  # Alternative
                    else:
                        self.spectra[i].append(0)  # Original
                        # self.spectra[i].append(1)  # Alternative
            else:
                self.error_vector.append(1)
                self.spectra.append([])
                for j, _ in enumerate(s.outcome):
                    if s.agent_pass[j]:
                        self.spectra[i].append(0)
                    else:
                        self.spectra[i].append(1)
        print('Spectra and error vector calculated')

    def calculate_diagnoses_and_probabilities(self, method: Callable[[List[List[int]], List[int], Dict],
                                                                     Tuple[List[List[int]], List[float]]] = None):
        if method is None:
            self.diagnoses, self.probabilities = \
                statics.calculate_diagnoses_and_probabilities_ochiai(self.spectra, self.error_vector, {})
        else:
            self.diagnoses, self.probabilities = \
                method(self.spectra, self.error_vector, {})

        print('Diagnoses and probabilities calculated')

    def print_and_visualize_output(self) -> None:
        print('\nPrinting and visualizing:')
        print('========================')
        for i, s in enumerate(self.simulations_to_run):
            print(f'Percentage free critical areas in {s.name}: {s.percentage_free}')
            s.visualize(what='plans')
            s.visualize(what='outcome')

        print('Spectra and Error vector:')
        for j in range(len(self.spectra)):
            for i in range(len(self.spectra[0])):
                print(f'{self.spectra[j][i]} ', end='')
            print(f'| {self.error_vector[j]}')
        print(f'Diagnoses and probabilities:')
        for i, d in enumerate(self.diagnoses):
            print(f'{d}, {self.probabilities[i]}')
        print('')
