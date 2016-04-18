"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_list = list()
    ordered_list = [0]*len(line)
    position = 0
    # ordered_list is beign populated
    for number in line:
        if number != 0:
            ordered_list[position] = number
            position += 1
    # iteration through ordered_list
    index = 0
    if len(line) > 1:
        # comparing the first element to the next element
        while index+1 < len(ordered_list):
            if ordered_list[index] == ordered_list[index+1]:
                result_list.append(ordered_list[index]*2)
                index += 1
            else:
                result_list.append(ordered_list[index])
            index += 1
            # checking the last item
            if index == len(ordered_list)-1:
                result_list.append(ordered_list[index])
        # populating the remaining with 0's
        while len(ordered_list) > len(result_list):
            result_list.append(0)
    else:
        result_list = line

    return result_list

def traverse_grid(base_grid, start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction

    Both start_cell is a tuple(row, col) denoting the
    starting cell

    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    result_grid = list()

    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]

        result_grid.append(base_grid[row][col])

    return result_grid

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid = list()
        self._grid_height = grid_height
        self._grid_width = grid_width
        # calling reset method
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for _ in range(self._grid_width)]
                                for _ in range(self._grid_height)]
        # calling the function to set 2 initial values
        # it can be 2 (90%) or 4 (10%)
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        has_moved = False

        # UP
        if direction == 1:
            new_traversed_grid = list()
            new_converted_grid = list()
            ## we create a traversed grid (with the columns) and merge each new row
            for col in range(self._grid_width):
                traversed_row = traverse_grid(self._grid, (0 , col),
                                      OFFSETS[UP], self._grid_height)
                new_traversed_grid.append((merge(traversed_row)))
            # we traverse back the grid
            for other_col in range(self._grid_height):
                new_converted_grid.append(traverse_grid(new_traversed_grid, (0 , other_col),
                                      OFFSETS[UP], self._grid_width))
            # we set the original grid as the new grid
            self._grid = new_converted_grid
            has_moved = True

        # DOWN
        elif direction == 2:
            new_traversed_grid = list()
            new_converted_grid = list()
            # we create a traversed grid (with the columns) and merge each new row
            for col in range(self._grid_width):
                traversed_row = traverse_grid(self._grid, (self._grid_height -1 , (self._grid_width-1) - col),
                                      OFFSETS[DOWN], self._grid_height)
                new_traversed_grid.append(merge(traversed_row))
            # we traverse back the grid
            for other_col in range(self._grid_height):
                new_converted_grid.append(traverse_grid(new_traversed_grid, (self._grid_width -1 , (self._grid_height-1) - other_col),
                                     OFFSETS[DOWN], self._grid_width))
            # we set the original grid as the new grid
            self._grid = new_converted_grid
            has_moved = True

        # LEFT
        elif direction == 3:
            # we only need no merge each row of the grid
            for row in self._grid:
                self._grid[self._grid.index(row)] = merge(row)
            has_moved = True

        # RIGHT
        else:
            new_traversed_grid = list()
            # we create a traversed grid (with the rows) and merge each new row
            for row in range(self._grid_height):
                traversed_row = traverse_grid(self._grid, (row, self._grid_width - 1),
                                      OFFSETS[RIGHT], self._grid_width)
                new_traversed_grid.append((merge(traversed_row)))
            # we traverse back the grid
            for row in range(self._grid_height):
                self._grid[row] = traverse_grid(new_traversed_grid, (row, self._grid_width - 1),
                                      OFFSETS[RIGHT], self._grid_width)

            has_moved = True

        if has_moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # we create a list of free cells and we count the free cells
        free_cells = list()
        count_free_cells = 0

        # we iterate over the grid to check for free cells
        # if so, we append to the free_cells list and count that
        for row in range(self._grid_height):
            for colum in range(self._grid_width):
                if self.get_tile(row, colum) == 0:
                    free_cells.append((row, colum))
                    count_free_cells += 1

        # if there are free cells we set into one of them
        # the value 2 or 4
        if count_free_cells >= 1:
            random_values_list = [2]*9 + [4]
            random_value = random.choice(random_values_list)
            random_cell = random.choice(free_cells)
            self.set_tile(random_cell[0], random_cell[1], random_value)
        else:
            pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))