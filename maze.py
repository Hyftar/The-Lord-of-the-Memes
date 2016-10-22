import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from noise import pnoise3
from PIL import Image


class Cell:
    def __init__(self):
        self.left = False
        self.up = False
        self.right = False
        self.down = False
        self.visited = False
        self.content = ''


class Maze:
    """Generates a maze. Each position contains 5 booleans,
    the first 4 are if there's a door on the left, top right and bottom and the
    last coordinate is if the coordinate was visited during the search."""
    def __init__(self, rows, cols):
        self.height = rows
        self.width = cols
        self.seed = random.random()  # seed is needed to get random mazes
        self.array = np.zeros((self.height, self.width, 5),
                              dtype=np.uint8)
        r = 0
        c = 0
        history = [(r, c)]

        while history:
            self.array[r, c, 4] = 1
            check = []
            if c > 0 and self.array[r, c - 1, 4] == 0:
                check.append('L')
            if r > 0 and self.array[r - 1, c, 4] == 0:
                check.append('U')
            if c < self.width - 1 and self.array[r, c + 1, 4] == 0:
                check.append('R')
            if r < self.height - 1 and self.array[r + 1, c, 4] == 0:
                check.append('D')

            if len(check):
                history.append([r, c])
                move_direction = random.choice(check)
                if move_direction == 'L':
                    self.array[r, c, 0] = 1
                    c = c - 1
                    self.array[r, c, 2] = 1
                if move_direction == 'U':
                    self.array[r, c, 1] = 1
                    r = r - 1
                    self.array[r, c, 3] = 1
                if move_direction == 'R':
                    self.array[r, c, 2] = 1
                    c = c + 1
                    self.array[r, c, 0] = 1
                if move_direction == 'D':
                    self.array[r, c, 3] = 1
                    r = r + 1
                    self.array[r, c, 1] = 1
            else:
                r, c = history.pop()

        entrance_loc = random.randrange(self.width)
        exit_loc = random.randrange(self.width)
        self.array[0, entrance_loc][1] = 1
        self.array[self.height - 1, exit_loc][3] = 1

    # Currently only generates a png of the maze population
    # Each pixel represents a cell on the maze
    def populate(self):
        w, h = self.width, self.height
        data = np.zeros((h, w, 3), dtype=np.uint8)
        level = np.zeros((h, w, 3), dtype=np.uint8)
        octaves = 80  # A bit random
        freq = ((w + h) / 2) / octaves * 5
        for x in range(w):
            for y in range(h):
                # we use the 3rd dimension as our maze's seed (bit of a hack)
                color = pnoise3(x / freq, y / freq, self.seed, octaves=octaves)
                color = abs(color)  # Color could be used to determine room lvl
                if color < 0.08:
                    room = random.randrange(10000)
                    if room < 2000:  # Event (?)
                        data[y, x] = [255, 0, 255]
                    elif room > 9700:  # Shop (?)
                        data[y, x] = [0, 0, 255]
                    else:  # Puzzle (?)
                        data[y, x] = [255, 255, 0]
                else:
                    data[y, x] = [255, 0, 0]

        img = Image.fromarray(data, 'RGB')
        img.save('my.png')

        # Reset visited states
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.Array[row, col][4] = 0

    def show_image(self):
        image = np.zeros((self.height * 10, self.width * 10),
                         dtype=np.uint8)
        for row in range(0, self.height):
            for col in range(0, self.width):
                cell_data = self.array[row, col]
                for i in range(10 * row + 1, 10 * row + 9):
                    image[i, range(10 * col + 1, 10 * col + 9)] = 255
                    if cell_data[0] == 1:
                        image[range(10 * row + 1, 10 * row + 9),
                              10 * col] = 255
                    if cell_data[1] == 1:
                        image[10 * row, range(10 * col + 1,
                                              10 * col + 9)] = 255
                    if cell_data[2] == 1:
                        image[range(10 * row + 1, 10 * row + 9),
                              10 * col + 9] = 255
                    if cell_data[3] == 1:
                        image[10 * row + 9, range(10 * col + 1,
                                                  10 * col + 9)] = 255

        plt.imshow(image, cmap=cm.Greys_r, interpolation='none')
        plt.show()
