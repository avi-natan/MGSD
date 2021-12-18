import json
import os
import random
import shutil
import math

import statics


class ScenarioBuilder(object):

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

    def build_scenario(self,
                       world_name,
                       agents_number,
                       faulty_agents_number,
                       fault_probability,
                       simulations_number,
                       scenario_number,
                       scenario_type):
        """
        Builds a scenario using the arguments. A scenario object is composed of a world and a group
        of agents, where some of them are faulty and have a positive fault probability, as well as a number
        that states how many simulations are to be run. "The workers that do the job, and how many times"

        The resulting scenario will be encoded into a json object in the folder
        "worlds/<world_name>_scenarios" folder under the name
        "scenario_an_<agents_number>_fan_<faulty_agents_number>_fp_<fault_probability>_sn_<simulations_number>.json"
        and a folder named
        "scenario_an_<agents_number>_fan_<faulty_agents_number>_fp_<fault_probability>_sn_<simulations_number>_outcomes"
        will be created.

        :param world_name: the name of the world to use (worlds folder must have a json file
        with the name of this argument. this function throws exception if such folder is
        not found.
        :param agents_number: the number of agents given to execute the plan in the given world. it
        must not exceed the size of the plan on the world. this method will raise an exception in that case
        :param faulty_agents_number: the number of faulty agents
        :param fault_probability: the probability of faulty agents to experience fault in every single timestep
        :param simulations_number: the number of simulations in this scenario
        :param scenario_number: number of scenario
        :param scenario_type: whether the scenario should be static, generated, or from a third party
        module. specified by the datum [static, generated].
        in case of static, this function will load the static information about the agents defined for the
        specified world name inside the board's folder, that matches the size, length, and number of
        intersections for the board, as well as the number of agents, faulty agents,
        and fault probabilities.
        in case of generated, the function will generate a random information about the agents according to the
        specifications.
        :return: boolean indicator whether the generation succeeded
        """
        # get the agents of the simulation ready
        wn = str(world_name)
        an = str(agents_number)
        fan = str(faulty_agents_number)
        fp = str(fault_probability)
        sn = str(simulations_number)
        scn = scenario_number

        # check that a scenario doesnt already exist
        outfile_path = f'../worlds/{wn}_scenarios/scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}.json'
        outdir_path = f'../worlds/{wn}_scenarios/scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}_outcomes'
        if os.path.exists(outfile_path) and os.path.exists(outdir_path):
            print(f'scenario json {outfile_path[:-5]} exists, skipping...')
            return False

        scenario_json = None
        if scenario_type == 'static':
            scenario_json = self.static_scenario(wn, an, fan, fp, sn, scn)
        elif scenario_type == 'generated':
            scenario_json = self.generated_scenario(wn, an, fan, fp, sn, scn)
            pass
        else:
            raise Exception(f'unexpected scenario type: "{scenario_type}"')

        # write the scenario to disk
        if scenario_json is not None:
            print(f'world_name: {wn}')
            print(f'agents_number: {agents_number}')
            print(f'faulty_agents_number: {faulty_agents_number}')
            print(f'fault_probability: {fault_probability}')
            print(f'simulations_number: {simulations_number}')
            print(f'scenario_number: {scn}')
            print(f'scenario_type: {scenario_type}')

            # # visualize scenario
            # if simulations_number == 10 and scenario_number == 0:
            #     world_json = scenario_json['world']
            #     plan = world_json['plan']['individual_plans']
            #     board = world_json['board']
            #     statics.visualize(plan, board)

            # outfile_path = f'../worlds/{wn}_scenarios/scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}.json'
            with open(outfile_path, 'w') as outfile:
                json.dump(scenario_json, outfile)

            # outdir_path = f'../worlds/{wn}_scenarios/scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}_outcomes'
            if not os.path.exists(outdir_path):
                os.mkdir(outdir_path)
            else:
                shutil.rmtree(outdir_path)
                os.mkdir(outdir_path)
            return True
        else:
            print(f'No valid scenario generated for '
                  f'scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}.json, skipping...')
            return False

    def static_scenario(self, wn, an, fan, fp, sn, scn):
        static_scenarios_contents = \
            next(os.walk(f'{self.static_worlds_relative_path}/{wn}_scenarios'))
        world_static_scenarios_filenames = static_scenarios_contents[2]
        world_static_scenario_filename = f'scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}.json'
        if world_static_scenario_filename not in world_static_scenarios_filenames:
            scenario_json = None
        else:
            scenario_json = json.load(open(
                f'{self.static_worlds_relative_path}/{wn}_scenarios/{world_static_scenario_filename}'))
        return scenario_json

    def generated_scenario(self, wn, an, fan, fp, sn, scn):
        world_json = json.load(open(f'{self.worlds_relative_path}/{wn}.json'))

        # # Update critical areas
        # print(9)
        # plan = world_json['plan']['individual_plans']
        # updated_critical_areas = []
        #
        # percentage_plan_to_crit = 1 - (float(fp) * 3.0 / 4.0)
        # plan_length = world_json['parameters']['plan_length']
        # last_crit_index = math.floor(plan_length * percentage_plan_to_crit)
        #
        # last_positions = [p[i] for i in range(last_crit_index, plan_length) for p in plan]
        # for i in range(int(an)):
        #     for index in range(last_crit_index+1):
        #         if [plan[i][index][0], plan[i][index][1]] not in last_positions:
        #             critical_area = [[plan[i][index][0], plan[i][index][1]], [plan[i][index][0]+1, plan[i][index][1]+1]]
        #             updated_critical_areas.append(critical_area)
        #
        #
        # world_json['board']['board_critical_areas'] = updated_critical_areas

        # Generate agents
        agents_json = []
        for i in range(int(an)):
            agent = {
                "agent_num": i,
                "agent_name": f"a{i}",
                "agent_is_faulty": False,
                "agent_fail_prob": 0.0
            }
            agents_json.append(agent)
        # randomly shuffle the list and add faults to the first <fan> agents
        random.shuffle(agents_json)
        for i in range(int(fan)):
            agents_json[i]['agent_is_faulty'] = True
            agents_json[i]['agent_fail_prob'] = float(fp)
        # return list to its original order
        agents_json.sort(key=lambda a: a['agent_num'])

        # build the scenario json
        scenario_json = {
            "scenario_name": f"{world_json['world_name']}_scenario_an_{an}_fan_{fan}_fp_{fp}_sn_{sn}_scn_{scn}",
            "parameters": {
                "world_name": f"{world_json['world_name']}",
                "agents_number": int(an),
                "faulty_agents_number": int(fan),
                "fault_probability": float(fp),
                "simulations_number": int(sn),
                "scenario_number": scn,
                "scenario_type": "generated"
            },
            "world": world_json,
            "agents": agents_json,
            "simulations_number": int(sn)
        }
        return scenario_json
