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
        self.array = []
        for i in range(self.width * self.height):
            self.array.append(Cell())

        self.entrance_loc = random.randrange(self.width)
        self.exit_loc = random.randrange(self.width)

        r = 0
        c = 0
        history = [(r, c)]

        while history:
            self.cell(c, r).visited = True
            check = []
            if c > 0 and not self.cell(c - 1, r).visited:
                check.append('L')
            if r > 0 and not self.cell(c, r - 1).visited:
                check.append('U')
            if c < self.width - 1 and not self.cell(c + 1, r).visited:
                check.append('R')
            if r < self.height - 1 and not self.cell(c, r + 1).visited:
                check.append('D')

            if len(check):
                history.append([r, c])
                move_direction = random.choice(check)
                if move_direction == 'L':
                    self.cell(c, r).left = True
                    c = c - 1
                    self.cell(c, r).right = True
                if move_direction == 'U':
                    self.cell(c, r).up = True
                    r = r - 1
                    self.cell(c, r).down = True
                if move_direction == 'R':
                    self.cell(c, r).right = True
                    c = c + 1
                    self.cell(c, r).left = True
                if move_direction == 'D':
                    self.cell(c, r).down = True
                    r = r + 1
                    self.cell(c, r).up = True
            else:
                r, c = history.pop()

        # Reset visited states
        for row in range(self.width):
            for col in range(self.height):
                self.cell(col, row).visited = False

        self.cell(self.entrance_loc, 0).up = True
        self.cell(self.exit_loc, self.height - 1).down = True

    def cell(self, x, y):
        return self.array[(x % self.width) + (y % self.height) * self.width]

    # Currently only generates a png of the maze population
    # Each pixel represents a cell on the maze
    def populate(self):
        w, h = self.width, self.height
        data = np.zeros((h, w, 3), dtype=np.uint8)
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
                        self.cell(x, y).content = 'event'
                        data[y, x] = [255, 0, 255]
                    elif room > 9700:  # Shop (?)
                        self.cell(x, y).content = 'shop'
                        data[y, x] = [0, 0, 255]
                    else:  # Puzzle (?)
                        self.cell(x, y).content = 'puzzle'
                        data[y, x] = [255, 255, 0]
                else:
                    self.cell(x, y).content = 'monsters'
                    data[y, x] = [255, 0, 0]

        img = Image.fromarray(data, 'RGB')
        img.save('my.png')

    def show_image(self):
        image = np.zeros((self.height * 10, self.width * 10),
                         dtype=np.uint8)
        for row in range(self.height):
            for col in range(self.width):
                cell_data = self.cell(col, row)
                for i in range(10 * row + 1, 10 * row + 9):
                    image[i, range(10 * col + 1, 10 * col + 9)] = 255
                    if cell_data.left:
                        image[range(10 * row + 1, 10 * row + 9),
                              10 * col] = 255
                    if cell_data.up:
                        image[10 * row, range(10 * col + 1,
                                              10 * col + 9)] = 255
                    if cell_data.right:
                        image[range(10 * row + 1, 10 * row + 9),
                              10 * col + 9] = 255
                    if cell_data.down:
                        image[10 * row + 9, range(10 * col + 1,
                                                  10 * col + 9)] = 255

        plt.imshow(image, cmap=cm.Greys_r, interpolation='none')
        plt.show()
