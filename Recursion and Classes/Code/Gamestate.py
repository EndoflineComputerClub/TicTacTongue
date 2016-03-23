"""Contains the class to represent a gamestate of TicTacToe."""

from ExtendedAPI import *

class Gamestate:
    """The class implementing a state of the game."""
    def __init__(self, grid, zeros_move, depth):
        """Constructor, especially useful for generating states recursively."""
        self.grid = grid
        self.zeros_move = zeros_move
        self.states = []
        self.value = -200 if (zeros_move) else 200
	self.depth = depth					    # Depth of a game.

    def make_states(self):
        """Makes child states of self."""
        if (game_end(self.grid)) : return
        for i in range(3):
            for j in range(3):
                if (self.grid[i][j] == ' '):
                    new_grid = [row[:] for row in self.grid]
                    new_grid[i][j] = '0' if (self.zeros_move) else 'X'
                    new_state = Gamestate(new_grid, not self.zeros_move, self.depth + 1)
                    self.states.append(new_state)
                    new_state.make_states()
       

    def calculate_value(self):
        """Calculates the value of self."""
        if (not self.states):                                        # If self doesn't have any child states (is a leaf) ...
            if (ttp_lost(self.grid)):                                           # ... assign it a value based on who won.
                self.value = 10# + self.depth
            elif (zeros_lost(self.grid)):
                self.value = -10# + self.depth           
            else:
                self.value = 0
        else:
            for state in self.states:
                state.calculate_value()
            if (self.zeros_move):
                for state in self.states:
                    if (state.value > self.value) : self.value = state.value 
            else:
                for state in self.states:
                    if (state.value < self.value) : self.value = state.value
        self.states.sort(lambda a, b: -1 if (a.value > b.value) else (1 if (a.value < b.value) else 0))
