from typing import List

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

class Board(object):
    object_id = 0

    def __init__(self,
                 name: str = None,
                 width: int = 3,
                 height: int = 3,
                 critical_areas: List[List[List[int]]] = None) -> None:
        if width < 3 or height < 3:
            raise Exception(f'manually input board dimensions must be at least 3X3, received {width}X{height}')
        if name is None:
            name = 'Anonymous_Board_' + str(Board.object_id)
        if critical_areas is None:
            critical_areas = [((1, 1), (2, 2))]

        self.id = Board.object_id
        self.name = name
        self.width = width
        self.height = height
        self.critical_areas = critical_areas
        Board.object_id += 1

    def visualize(self, mode: str = 'grid') -> None:
        board = np.zeros((self.width, self.height))
        for ca in self.critical_areas:
            board[ca[0][0]:ca[1][0], ca[0][1]: ca[1][1]] = 1
        plt.figure()
        cmap = colors.ListedColormap(['white', 'red'])
        plt.imshow(board, interpolation='none', vmin=0, vmax=1, aspect='equal', cmap=cmap)

        ax = plt.gca()

        # Major ticks
        ax.set_xticks(np.arange(0, self.width, 1))
        ax.set_yticks(np.arange(0, self.height, 1))

        # Labels for major ticks
        ax.set_xticklabels(np.arange(0, self.width, 1))
        ax.set_yticklabels(np.arange(0, self.height, 1))

        # Minor ticks
        ax.set_xticks(np.arange(-.5, self.width, 1), minor=True)
        ax.set_yticks(np.arange(-.5, self.height, 1), minor=True)

        # Gridlines based on minor ticks
        if mode == 'net':
            ax.grid(which='major', color='black', linestyle='-', linewidth=2)
        elif mode == 'grid':
            ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
        else:
            raise Exception("mode needs to be either 'grid' or 'net'")

        ax.xaxis.tick_top()
        plt.show()

    def summary(self) -> None:
        critical_areas_string = ""
        for ca in self.critical_areas:
            critical_areas_string += '\t' + str(ca) + '\n# '
        print(f"""
#######################################################
#                    Board Summary
# 
# ID: {self.id}
# Name: {self.name}
# Width: {self.width}
# Height: {self.height}
# 
# Critical areas:
# {critical_areas_string}
#######################################################
        """)
