# Code by Erik Sweet and Bill Basener

import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm


class Maze:
    """Generates a maze."""
    def __init__(self, rows, cols):
        self.num_rows = rows
        self.num_cols = cols
        self.Array = np.zeros((self.num_rows, self.num_cols, 5), dtype=np.uint8)

        r = 0
        c = 0
        history = [(r, c)]

        while history:
            self.Array[r, c, 4] = 1
            check = []
            if c > 0 and self.Array[r, c - 1, 4] == 0:
                check.append('L')
            if r > 0 and self.Array[r - 1, c, 4] == 0:
                check.append('U')
            if c < self.num_cols-1 and self.Array[r, c + 1, 4] == 0:
                check.append('R')
            if r < self.num_rows-1 and self.Array[r + 1, c, 4] == 0:
                check.append('D')

            if len(check):
                history.append([r, c])
                move_direction = random.choice(check)
                if move_direction == 'L':
                    self.Array[r, c, 0] = 1
                    c = c-1
                    self.Array[r, c, 2] = 1
                if move_direction == 'U':
                    self.Array[r, c, 1] = 1
                    r = r - 1
                    self.Array[r, c, 3] = 1
                if move_direction == 'R':
                    self.Array[r, c, 2] = 1
                    c = c + 1
                    self.Array[r, c, 0] = 1
                if move_direction == 'D':
                    self.Array[r, c, 3] = 1
                    r = r + 1
                    self.Array[r, c, 1] = 1
            else:  # If there are no valid cells to move to.
                # retrace one step back in history if no move is possible
                r, c = history.pop()

    def show_image(self):
        image = np.zeros((self.num_rows*10, self.num_cols*10), dtype=np.uint8)
        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                cell_data = self.Array[row, col]
                for i in range(10 * row + 1, 10 * row + 9):
                    image[i, range(10 * col + 1, 10 * col + 9)] = 255
                    if cell_data[0] == 1:
                        image[range(10 * row + 1, 10 * row + 9), 10 * col] = 255
                    if cell_data[1] == 1:
                        image[10 * row, range(10 * col + 1, 10 * col + 9)] = 255
                    if cell_data[2] == 1:
                        image[range(10 * row + 1, 10 * row + 9), 10 * col + 9] = 255
                    if cell_data[3] == 1:
                        image[10 * row + 9, range(10 * col + 1, 10 * col + 9)] = 255

        plt.imshow(image, cmap=cm.Greys_r, interpolation='none')
        plt.show()
