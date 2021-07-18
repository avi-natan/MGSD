import os
import json
import shutil
from subprocess import Popen, PIPE

import statics


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
        thirdparty].
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
            world_json = self.generated_world(bn, s, l, i)
        elif world_type == 'thirdparty':
            world_json, i = self.third_party_world(bn, s, l, i)
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

    def generated_world(self, bn, s, l, i):
        # For now we dont need to implement this. More important is to implement
        # working with Dor's plans
        world_json = None
        return world_json

    def third_party_world(self, bn, s, l, i):
        # Meir says that the intersections doesnt matter so much.

        # create the instructions file in the 'third party terminal' folder
        instructions_file = open(f'../third party terminal/instructions', 'w')
        instructions_file.write(f'inputs:\n')
        instructions_file.write(f'r: 144\n')
        instructions_file.write(f'a: {s}\n')
        instructions_file.write(f't: {l}\n')
        instructions_file.write(f'i: -1\n')
        instructions_file.write(f'p: -1\n')
        # instructions_file.write('ca: [[[4.4],[8.5]]|[[4.7],[8.8]]|[[4.5],[5.7]]|[[7.5],[8.7]]]\n')  # [ [[4. 4], [8. 5]] | [[4. 7], [8. 8]] | [[4. 5], [5. 7]] | [[7. 5], [8. 7]] ]
        instructions_file.write('ca: [[[3.3],[9.9]]]\n')
        # instructions_file.write(f'fa: [-1]\n')
        instructions_file.write(f'ft: [-1]\n')
        instructions_file.write(f'tpp: \\third party terminal\\cpf-experiment\\mgsd_d0.exe\n')
        instructions_file.write(f'===\n')
        instructions_file.close()

        # call the external program and receive its output
        argument = os.getcwd() + "\\..\\third party terminal\\instructions"
        thirdPartyExecutable = "..\\third party terminal\\cpf-experiment\\mgsd_d0.exe"

        iv_plans = [[[0,0]] * int(l) for _ in range(int(s))]

        has_collisions, collision_time = statics.has_collisions(iv_plans)

        while has_collisions:
            process = Popen([thirdPartyExecutable, argument], stdout=PIPE)
            (output, err) = process.communicate()
            exit_code = process.wait()

            while err is not None:
                print(f'third party program failed, trying again...')
                process = Popen([thirdPartyExecutable, argument], stdout=PIPE)
                (output, err) = process.communicate()
                exit_code = process.wait()

            output_str = output.decode("utf-8")
            print(f'{output_str}')

            # read the generated third party plan and construct the plans matrix
            f = open(f'../third party terminal/thirdPartyPlan')
            f.readline()
            f.readline()
            f.readline()
            line = f.readline()
            ai = 0
            while line != '':
                print(line)
                line_split = line[1:-2].split('|')
                for i, ls in enumerate(line_split):
                    ls_split = ls[1:-1].split(',')
                    iv_plans[ai][i] = [int(ls_split[0]), int(ls_split[1])]
                line = f.readline()
                ai += 1
            f.close()

            has_collisions, collision_time = statics.has_collisions(iv_plans)
            print(f'Collisions:  {has_collisions}, time: {collision_time}')

        # construct the world json
        n_intersections = statics.count_intersections(iv_plans)
        world_name_json = f'world_board_{bn}_plan_s_{s}_l_{l}_i_{n_intersections}'
        parameters_json = {
            "board_name": bn,
            "plan_size": int(s),
            "plan_length": int(l),
            "intersections_number": int(n_intersections),
            "world_type": "thirdparty"
        }
        board_json = {
            "board_name": bn,
            "board_width": 12,
            "board_height": 12,
            "board_critical_areas": [
                [[3, 3], [9, 9]]
            ]
        }
        plan_json = {
            'size': int(s),
            'length': int(l),
            'intersections': int(n_intersections),
            'individual_plans': iv_plans
        }

        world_json = {
            'world_name': world_name_json,
            'parameters': parameters_json,
            'board': board_json,
            'plan': plan_json
        }

        print(9)
        return world_json, str(n_intersections)
