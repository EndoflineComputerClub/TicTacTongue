"""The Earth's Mightiest Zeros (Zeros) vs The TicTacFoe (TTF)!"""

from Gamestate import *

Grid = [[' ', ' ', ' '],                      # Set up an empty grid for the game.
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

x_moves = raw_input("Welcome, TicTacFoe! >:| Do you want to go first? (Y or N): ")

zeros_move = True if (x_moves == 'N' or x_moves == 'n') else False      # A boolean variable, depending on TTF's response.

state = None                                                            # Declare a variable which will represent the game's state. 

first_move = True                                                       # Boolean to store whether it is the first move or not. 

while (first_move or (not game_end(state.grid))):                       # The 'state' will only actually be a Gamestate object/instance after the first move, ...
                                                                        # ... so the while loop condition included a pre-check for that case.

    if (first_move):                                                        # If it's the first move ...                                                          
        if (not zeros_move):                                                    # ... and it's the TTF's move ...
            i = int(raw_input("Enter X in row __: "))                               # ... prompt the TTF for the coordinates of their move.
            j = int(raw_input("Enter X in col __: "))
            while (i < 0 or i > 2):                                                 # If the row number is not in {0, 1, 2} ...
                i = int(raw_input("Row should be between 0 and 2: "))               # ... prompt them again.
            while (j < 0 or j > 2):                                                 # Do the same for column number.
                j = int(raw_input("Col should be between 0 and 2: "))
            Grid[i][j] = 'X'                                                        # Put an 'X' on the grid, once you have valid coordinates.
            print("\nYou: ")                                                        # Tell the TicTacFoe that the next grid they see will show their move.
        else:                                                                       # ... otherwise if it's our (Zeros') move ...
            Grid[0][0] = '0'                                                        # ... play a default move of putting a '0' in the first row, first column.
            print("\nEarth's Mightiest Zeros: ")                                    # This default move is a significant optimization, will be covered in the document.

        state = Gamestate(Grid, not zeros_move)                                 # Now, make a Gamestate object that represents the current grid, and call it 'state'.
        
        state.make_states()                                                     # Generate the game's tree.
        state.calculate_value()                                                 # Compute each state's value.
        first_move = False                                                      # And it's no longer the first move, hence.
        
    else:                                                                   # For every move after the first one ...
        if (not zeros_move):                                                    # ... if it's the TTF's move ...
            i = int(raw_input("Enter X in row __: "))                               # ... prompt the TTF for the coordinates of their move.
            j = int(raw_input("Enter X in col __: "))
            while (i < 0 or i > 2):                                                 # If the row number is not in {0, 1, 2} ...
                i = int(raw_input("Row should be between 0 and 2: "))               # ... prompt them again.
            while (j < 0 or j > 2):                                                 # Do the same for column number.
                j = int(raw_input("Col should be between 0 and 2: "))
            while (isCross(state.grid, i, j) or isZero(state.grid, i, j)):          # Now since this is not the first move, the board may not be empty, and ...
                print "Please enter unoccupied coordinates"                         # ... we need to check that the coordinates TTF is trying to play on are empty.
                i = int(raw_input("Enter X in row __: "))                           # Prompt them again.
                j = int(raw_input("Enter X in col __: "))                       
            for new_state in state.states:                                          # Now, the current state must have many child states, and one of those will ...
                if (new_state.grid[i][j] == 'X'):                                   # ... correspond to the move that TTF wants to play. Look for that state ...
                    state = new_state                                               # ... and make it the current state.
                    break                                                           # Once we've found that state, we can stop looking through the children.
            print("\nYou: ")
        else:                                                                   # Otherwise if it's our move, recall that the child states is sorted in decreasing ...
            state = state.states[0]                                                 # ... order of value. So, make the first state (with the max value) the current.
            print("\nEarth's Mightiest Zeros: ")                                     
    printToConsole(state.grid)                                              # Now, after every move (first or the rest), we will print the grid to the console.
    zeros_move = not zeros_move                                             # Switch the boolean turn indicator.
        
print("\n\nGame over:"),                                            # The fact that we're out of the while loop means that `not (game_end(state.grid))` is false, or...
if (ttf_lost(state.grid)):                                          # ... game_end(state.grid) is true i.e. we've reached the end of the game. So, if the TTF lost ... 
    print("The Earth's Mightiest Zeros win!")                       # ... declare our victory! :D 
elif (zeros_lost(state.grid)):                                      # Otherwise ...
    print("TicTacMan/Woman wins!")                                  # ... declare theirs.
else:
    print("Draw.")                                                  # Else, it's a draw. 
