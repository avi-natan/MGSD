import consts
import statics
from board import Board
from agent import Agent

from typing import List, Dict
from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


class Simulation(object):
    object_id = 0

    def __init__(self,
                 name: str = None,
                 board: Board = None,
                 plans: List[List[Tuple[int, int]]] = None,
                 agents: List[Agent] = None) -> None:
        if name is None:
            name = 'Anonymous_Simulation_' + str(Simulation.object_id)
        if board is None:
            board = Board()
        if plans is None:
            plans = [[(j, i) for i in range(board.width)] for j in range(board.height)]
        if agents is None:
            agents = [Agent() for _ in range(len(plans))]

        self.id = Simulation.object_id
        self.name = name
        self.board = board
        self.plans = plans
        self.agents = agents
        self.delay_table = None
        self.outcome = None
        Simulation.object_id += 1

    def simulate(self, fault_and_conflict_method: str, facm_args: Dict) -> None:
        assert self.board is not None, 'can not simulate without board'
        assert self.agents is not None, 'can not simulate without agents'
        assert self.agents != [], 'can not simulate without agents'
        assert self.plans is not None, 'can not simulate without plans'
        assert self.plans != [], 'can not simulate without plans'

        # # Dummy outcome
        # self.outcome = consts.traffic_circle_custom_plan1_outcomes[self.id]

        # # Real outcome - considering the agents plans and whether they are faulty
        self.delay_table, self.outcome = statics.methods[fault_and_conflict_method](self.agents, self.plans, facm_args)

    def visualize(self, mode: str = 'grid', what: str = 'plans') -> None:
        if what == 'outcome':
            matrix = self.outcome
        else:
            matrix = self.plans
        board = np.zeros((self.board.width, self.board.height))
        for ca in self.board.critical_areas:
            board[ca[0][0]:ca[1][0], ca[0][1]: ca[1][1]] = 1
        plt.figure()
        cmap = colors.ListedColormap(['white', 'red'])
        plt.imshow(board, interpolation='none', vmin=0, vmax=1, aspect='equal', cmap=cmap)

        ax = plt.gca()

        # Major ticks
        ax.set_xticks(np.arange(0, self.board.width, 1))
        ax.set_yticks(np.arange(0, self.board.height, 1))

        # Labels for major ticks
        ax.set_xticklabels(np.arange(0, self.board.width, 1))
        ax.set_yticklabels(np.arange(0, self.board.height, 1))

        # Minor ticks
        ax.set_xticks(np.arange(-.5, self.board.width, 1), minor=True)
        ax.set_yticks(np.arange(-.5, self.board.height, 1), minor=True)

        # Gridlines based on minor ticks
        if mode == 'net':
            ax.grid(which='major', color='black', linestyle='-', linewidth=2, zorder=0)
        elif mode == 'grid':
            ax.grid(which='minor', color='black', linestyle='-', linewidth=2, zorder=0)
        else:
            raise Exception("mode needs to be either 'grid' or 'net'")

        ax.xaxis.tick_top()
        for ai, a in enumerate(self.agents):
            for i in range(len(matrix[ai][:-2])):
                plt.arrow(matrix[ai][i][0], matrix[ai][i][1],
                          matrix[ai][i + 1][0] - matrix[ai][i][0],
                          matrix[ai][i + 1][1] - matrix[ai][i][1],
                          width=0.5 - (0.5 / len(self.agents)) * (a.id % len(self.agents)), color=a.color,
                          head_length=0, head_width=0, zorder=3 + a.id % len(self.agents))
            plt.arrow(matrix[ai][-2][0], matrix[ai][-2][1],
                      matrix[ai][-1][0] - matrix[ai][-2][0],
                      matrix[ai][-1][1] - matrix[ai][-2][1],
                      width=0.5 - (0.5 / len(self.agents)) * (a.id % len(self.agents)), color=a.color,
                      head_width=0.5, head_length=0.5, zorder=3 + a.id % len(self.agents))

        plt.show()

    def summary(self) -> None:
        critical_areas_string = ""
        for ca in self.board.critical_areas:
            critical_areas_string += '\t\t' + str(ca) + '\n# '

        plans_string = '\t[\n#'
        for plan in self.plans:
            plans_string += '\t [ '
            i = 0
            for p in plan:
                plans_string += str(p) + ' '
                i += 1
                if i % 5 == 0:
                    plans_string += '\n# \t   '
            if plans_string[-7:] == '\n# \t   ':
                plans_string = plans_string[:-7] + ']\n#'
            else:
                plans_string += ']\n#'
        plans_string += '\t]\n#'

        agents_string = '\t[\n'
        for agent in self.agents:
            agents_string += f'#\t [\n#\t  ID: {agent.id}\n'
            agents_string += f'#\t  Name: {agent.name}\n'
            agents_string += f'#\t  Color: {agent.color}\n'
            agents_string += f'#\t  Faulty: {agent.is_faulty}\n'
            agents_string += f'#\t  Fail Probability: {agent.fail_prob}\n#\t '
            agents_string += ']\n'
        agents_string += '#\t]\n#'

        print(f"""
#######################################################
#                 Simulation Summary
# 
# ID: {self.id}
# Name: {self.name}
# 
# Board:
#   ID: {self.board.id}
#   Name: {self.board.name}
#   Width: {self.board.width}
#   Height: {self.board.height}
#   Critical areas:
# {critical_areas_string}
# Plans:
# {plans_string}
# Agents:
# {agents_string}
#######################################################
        """)

    def generate_outcome(self) -> List[List[Tuple[int, int]]]:
        # # TODO: implement
        pass
