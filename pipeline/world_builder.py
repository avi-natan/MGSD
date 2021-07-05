import os
import json
import shutil


class WorldBuilder(object):

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

    def build_world(self,
                    board_name,
                    plan_size,
                    plan_length,
                    intersections_number,
                    world_type):
        """
        Builds a world using the arguments. A world is an entity that has a board with critical
        areas, and a plan (in terms of size (number of individual plans) and length (lengths
        of those plans)). "A world and a job to do in it."

        The resulting world will be encoded into a json object in the folder 'worlds' by the name
        "world_board_<board_name>_plan_s_<plan_size>_l_<plan_length>_i_<intersections_number>.json"
        and a folder named
        "world_board_<board_name>_plan_s_<plan_size>_l_<plan_length>_i_<intersections_number>_scenarios"
        will be created.

        :param board_name: the name of the board to use (boards folder must have a json file
        with the name of this argument. this function throws exception if such folder is
        not found.
        :param plan_size: the maximal number of agents that can execute this plan. for example,
        length_of_plan = 6 means that at most 6 agents can run this plan, with a static number
        of minimum 2 agents are needed.
        :param plan_length: the number of time steps that this plan needs to be ran.
        :param intersections_number: the number of intersecting individual plans that the plan
        must have. for example if number_of_plans = 10 this means that at 10 points the
        individual plans must meet. it is assumed that one point can serve as a meeting point
        for more than 2 plans. in that case that meeting point will count as more than one
        point.
        :param world_type: whether the world should be static, generated, or from a third party
        module. a world type is defined by the plan it has. specified by the datum [static, generated,
        third_party].
        in case of static, this function will load a predefined world with a static plan.
        in case of generated, the function will generate a world with a random plan according to the
        specifications.
        in case of third party plan, the function will send the plan specifications to the third party
        module and get from there the desired world.
        :return: boolean indicator whether the building succeeded
        """
        # get the plan of the world ready
        bn = str(board_name)
        s = str(plan_size)
        l = str(plan_length)
        i = str(intersections_number)
        world_json = None
        if world_type == 'static':
            world_json = self.static_world(bn, s, l, i)
        elif world_type == 'generated':
            # TODO: implement
            pass
        elif world_type == 'third_party':
            # TODO: implement
            pass
        else:
            raise Exception(f'unexpected world type: "{world_type}"')

        if world_json is not None:
            outfile_path = f'../worlds/world_board_{board_name}_plan_s_{s}_l_{l}_i_{i}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(world_json, outfile)
            outdir_path = f'../worlds/world_board_{board_name}_plan_s_{s}_l_{l}_i_{i}_scenarios'
            if not os.path.exists(outdir_path):
                os.mkdir(outdir_path)
            else:
                shutil.rmtree(outdir_path)
                os.mkdir(outdir_path)
            return True
        else:
            print(f'No valid world generated for '
                  f'world_board_{board_name}_plan_s_{s}_l_{l}_i_{i}.json, skipping...')
            return False

    def static_world(self, bn, s, l, i):
        static_worlds_filenames = next(os.walk(f'{self.static_worlds_relative_path}'))[2]
        static_world_filename = f'world_board_{bn}_plan_s_{s}_l_{l}_i_{i}.json'
        if static_world_filename not in static_worlds_filenames:
            world_json = None
        else:
            world_json = json.load(open(f'{self.static_worlds_relative_path}/{static_world_filename}'))
        return world_json
