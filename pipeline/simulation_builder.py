import os


class SimulationBuilder(object):

    def __init__(self, boards_relative_path):
        if not os.path.isdir(boards_relative_path):
            raise Exception('boards relative path not found')
        self.boards_relative_path = boards_relative_path

    def build_simulation(self,
                         world_name,
                         agents_number,
                         faulty_agents_number,
                         fault_probability,
                         simulation_number):
        print(f'world_name: {world_name}')
        print(f'agents_number: {agents_number}')
        print(f'faulty_agents_number: {faulty_agents_number}')
        print(f'fault_probability: {fault_probability}')
        print(f'simulation_number: {simulation_number}')
