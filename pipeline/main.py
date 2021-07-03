import os

from pipeline.simulation_builder import SimulationBuilder
from pipeline.world_builder import WorldBuilder

if __name__ == '__main__':
    print(f'Hi MGSD pipeline!')

    # important - to run static pipeline, insert 'static' in every argument that allows it

    world_builder = WorldBuilder('../boards')

    # create various worlds
    world_builder.build_world('board_intersection0', 6, 12, 19, 'static')
    world_builder.build_world('board_intersection1', 6, 12, 18, 'static')
    world_builder.build_world('board_tcircle0', 6, 12, 78, 'static')

    # create simulations
    worlds_contents = next(os.walk('../worlds'))
    world_names = list(map(lambda fn: fn[:-5], worlds_contents[2]))
    simulation_builder = SimulationBuilder('../boards')
    created_simulations_count = 0
    # iterate over the different worlds
    for wn in world_names:
        max_agent_size = int(wn.split('_')[6])
        # iterate over the agent numbers
        for an in range(3, max_agent_size+1):
            # iterate over the faulty agent numbers
            for fan in range(1, an):
                # iterate over the fault probabilities
                for fp in [0.05, 0.1, 0.2, 0.3]:
                    # iterate over the number of simulations
                    for sn in range(10):
                        simulation_builder.build_simulation(wn, an, fan, fp, sn)
                        created_simulations_count += 1
    print(f'created_simulations_count: {created_simulations_count}')

    print(9)

    # run simulations and generate outcomes

    # run MGSD to generate diagnoses
