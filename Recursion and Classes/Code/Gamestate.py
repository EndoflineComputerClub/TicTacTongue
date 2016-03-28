"""Contains the class to represent a gamestate of TicTacToe. Note that 'we', are the Earth's Mightiest Zeros."""

from ExtendedAPI import *

class Gamestate:
    """The class implementing a state of the game."""
    def __init__(self, grid, zeros_move):
        """Constructor, especially useful for generating states recursively."""
        
        self.grid = grid                                 # The grid of the gamestate.
        self.zeros_move = zeros_move                     # Whether or not it is the Zeros' turn to move next.
        self.states = []                                 # A list of child states, each corresponding to a legal next move.
        self.value = -200 if (zeros_move) else 200       # The value of a state, as in, how desirable it is for the Zeros (us).

    def make_states(self):
        """Makes child states of self."""

        if (game_end(self.grid)) : return                                   # If the game has ended in the self state, then it has no child states (it is a 'leaf').
        for i in range(3):                                                  # For every (row, column) pair ...
            for j in range(3):                                              # ... look for legal spaces to play in (empty squares).
                if (self.grid[i][j] == ' '):                                # If you find an empty square ...
                    new_grid = [row[:] for row in self.grid]                    # ... make a new grid, which will basically be a copy of self's grid, row by row, ...
                    new_grid[i][j] = '0' if (self.zeros_move) else 'X'          # ... with the empty square filled in, depending on who's turn to move it is.
                    new_state = Gamestate(new_grid, not self.zeros_move)        # This will be the grid for a new child state of self. 
                    self.states.append(new_state)                               # So, it makes sense to append it to the list of child states.
                    new_state.make_states()                                     # Now, (recursively) generate the child states for this particular child state of self. 

       
    def calculate_value(self):
        """Calculates the value of self."""

        if (not self.states):                                               # If self doesn't have any child states (a leaf), assign it a value based on who won.
            
            if (ttf_lost(self.grid)):                                           # Say, if the TicTacFoe lost, then ...
                self.value = 10                                                 # ... let the value of the state be +10, since it's a desirable state for us.
            elif (zeros_lost(self.grid)):                                       # But if we lost, then ...
                self.value = -10                                                # ... let the value of the state be -10, since it's an undesirable state for us.
            else:                                                               # Otherwise, if it's a draw ...
                self.value = 0                                                  # ... give it a value of 0. It's a neutral state.
                
                                                                            # Else (if self is not a leaf and does have child states), it's value will ...
        else:                                                               # ... depend upon the value of its children, as well as who's turn it is.
                                                                            
            for state in self.states:                                           # Therefore, for every child state of self ...    
                state.calculate_value()                                         # ... (recursively) calculate its value..

            if (self.zeros_move):                                               # So if, it is our turn to move ...
                
                for state in self.states:                                           # ... then the value of the current state (self) is simply ...
                    if (state.value > self.value) : self.value = state.value        # ... the maximum value from amongst all it's child states.
              
            else:                                                               # Otherwise, if it is the TicTacFoe's turn to move ... 
                
                for state in self.states:                                           # ... then the value of the current state (self) is simply ...
                    if (state.value < self.value) : self.value = state.value        # ... the minimum value from amongst all it's child states.
             
        self.states.sort(lambda a, b: -1 if (a.value > b.value) else (1 if (a.value < b.value) else 0)) # Sort the child states in descending order of value. 

        # Now the most desirable state for us is the first element in the list of child states.
    
