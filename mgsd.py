import statics
from simulation import Simulation

from typing import List

class MGSD(object):
    def __init__(self):
        self.simulations_to_run: List[Simulation] = []
        self.error_vector: List[int] = []
        self.barinel_table: List[List[int]] = []
        self.diagnoses: List[List[int]] = []

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

        self.calculate_barinel_table_and_vector()
        self.calculate_diagnoses()
        # # TODO: rank the diagnoses
        self.print_and_visualize_output()
        print('fin')

    def calculate_barinel_table_and_vector(self):
        for i, s in enumerate(self.simulations_to_run):
            if s.simulation_pass:
                self.error_vector.append(0)
                self.barinel_table.append([])
                for j, _ in enumerate(s.outcome):
                    if s.agent_pass[j]:
                        self.barinel_table[i].append(1)  # Original
                        # self.barinel_table[i].append(0)  # Alternative
                    else:
                        self.barinel_table[i].append(0)  # Original
                        # self.barinel_table[i].append(1)  # Alternative
            else:
                self.error_vector.append(1)
                self.barinel_table.append([])
                for j, _ in enumerate(s.outcome):
                    if s.agent_pass[j]:
                        self.barinel_table[i].append(0)
                    else:
                        self.barinel_table[i].append(1)

    def print_and_visualize_output(self) -> None:
        for i, s in enumerate(self.simulations_to_run):
            print(f'Percentage free critical areas in {s.name}: {s.percentage_free}')
            s.visualize(what='plans')
            s.visualize(what='outcome')

        print('Barinel table:')
        for j in range(len(self.barinel_table)):
            for i in range(len(self.barinel_table[0])):
                print(f'{self.barinel_table[j][i]} ', end='')
            print('')
        print(f'Error vector:')
        for i in self.error_vector:
            print(f'{i}')
        print(f'Diagnoses:')
        for i in self.diagnoses:
            print(f'{i}')
        print('')

    def calculate_diagnoses(self) -> None:
        conflicts = []
        for i in range(len(self.error_vector)):
            if self.error_vector[i] == 1:
                c = []
                for j in range(len(self.barinel_table[i])):
                    if self.barinel_table[i][j] == 1:
                        c.append(j)
                conflicts.append(c)
        self.diagnoses: List[List[int]] = statics.conflict_directed_search(conflicts=conflicts)
