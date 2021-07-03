import os
import json
import shutil


class WorldBuilder(object):

    def __init__(self, boards_relative_path):
        """
        initiates world builder object with the relative path of the various boards.
        raises exception if it could not find the path.

        :param boards_relative_path: relative path of the various boards
        """
        if not os.path.isdir(boards_relative_path):
            raise Exception('boards relative path not found')
        self.boards_relative_path = boards_relative_path

    def build_world(self,
                    board_name,
                    plan_size,
                    plan_length,
                    intersections_number,
                    plan_type):
        """
        Builds a world using the arguments. A world is an entity that has a board with critical
        areas, and a plan (in terms of size (number of individual plans) and length (lengths
        of those plans)). "A world and a job to do in it."

        The resulting world will be encoded into a json object in the folder 'worlds' by the
        name "world_<board_name>_<plan_type>_plan_s_<plan_size>_l_<plan_length>_i_<intersections_number>.json"
        and a folder named
        "world_<board_name>_<plan_type>_plan_s_<plan_size>_l_<plan_length>_i_<intersections_number>_simulations"
        will be created.

        :param board_name: the name of the board to use (boards folder must have a folder
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
        :param plan_type: whether the plan should be static, generated, or from a third party
        module. specified by the datum [static, generated, third_party]. in case of static, this
        function will load the static plan defined for the specified board name inside the
        board's folder, that matches the size, length, and number of intersections.
        in case of generated, the function will generate a random plan according to the
        specifications. in case of third party plan, the function will send the plan specifications
        to the third party module and get from there the desired plan.
        :return:
        """

        boards_relative_path_contents = next(os.walk(self.boards_relative_path))
        list_of_boards_filenames = boards_relative_path_contents[2]

        # Get the board of the world ready
        if (board_name + '.json') not in list_of_boards_filenames:
            raise Exception(f'board name "{board_name}" is not defined in the boards folder')
        board_json = json.load(open(f'{self.boards_relative_path}/{board_name}.json'))

        # get the plan of the world ready
        s = str(plan_size)
        l = str(plan_length)
        i = str(intersections_number)
        plan_json = []
        if plan_type == 'static':
            plan_json = self.static_plan(boards_relative_path_contents, board_name, s, l, i)
        elif plan_type == 'generated':
            # TODO: implement
            pass
        elif plan_type == 'third_party':
            # TODO: implement
            pass
        else:
            raise Exception(f'unexpected plan type: "{plan_type}"')

        # construct the world and write it to disk
        world_json = {
            'board': board_json,
            'plan': plan_json
        }
        with open(f'../worlds/world_{board_name}_{plan_type}_plan_s_{s}_l_{l}_i_{i}.json', 'w') as outfile:
            json.dump(world_json, outfile)
        if not os.path.exists(f'../worlds/world_{board_name}_{plan_type}_plan_s_{s}_l_{l}_i_{i}_simulations'):
            os.mkdir(f'../worlds/world_{board_name}_{plan_type}_plan_s_{s}_l_{l}_i_{i}_simulations')
        else:
            shutil.rmtree(f'../worlds/world_{board_name}_{plan_type}_plan_s_{s}_l_{l}_i_{i}_simulations')
            os.mkdir(f'../worlds/world_{board_name}_{plan_type}_plan_s_{s}_l_{l}_i_{i}_simulations')

        print(9)

    def static_plan(self,
                    boards_relative_path_contents,
                    board_name,
                    s,
                    l,
                    i):
        list_of_boards_static_plan_directories = boards_relative_path_contents[1]
        if f'{board_name}_static_plans' not in list_of_boards_static_plan_directories:
            raise Exception(f'board "{board_name}" has no static plans')
        b_n = board_name
        plan_filename = f'{b_n}_static_plan_s_{s}_l_{l}_i_{i}.json'
        list_of_desired_board_static_plans = \
            next(os.walk(f'{self.boards_relative_path}/{board_name}_static_plans'))[2]
        if plan_filename not in list_of_desired_board_static_plans:
            raise Exception(f'desired static plan {plan_filename} not found for board {board_name}')

        plan_json = json.load(open(f'{self.boards_relative_path}/{board_name}_static_plans/{plan_filename}'))
        plan_json = {
            'size': s,
            'length': l,
            'intersections': i,
            'individual_plans': plan_json
        }
        return plan_json
