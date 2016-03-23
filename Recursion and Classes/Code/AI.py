from Gamestate import *

Grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

x_moves = raw_input("Welcome, TicTacMan/Woman! >:( Do you want to go first? (Y or N): ")

zeros_move = True if (x_moves == 'N' or x_moves == 'n') else False

state = None

first_move = True

while (first_move or (not game_end(state.grid))):
    if (first_move):
        if (not zeros_move):
            i = int(raw_input("Enter X in row __: "))
            j = int(raw_input("Enter X in col __: "))
            while (i < 0 or i > 2):
                i = int(raw_input("Row should be between 0 and 2: "))
            while (j < 0 or j > 2):
                j = int(raw_input("Col should be between 0 and 2: "))
            Grid[i][j] = 'X'
            print("\nYou: ")
        else:
            Grid[0][0] = '0'
            print("\nEarth's Mightiest Zeros: ")
        state = Gamestate(Grid, not zeros_move, 1)
        state.make_states()                                         # Generate the game tree.
        state.calculate_value()                                     # Compute each state's value.
        first_move = False
    else:     
        if (not zeros_move):
            i = int(raw_input("Enter X in row __: "))
            j = int(raw_input("Enter X in col __: "))
            while (i < 0 or i > 2):
                i = int(raw_input("Row should be between 0 and 2: "))
            while (j < 0 or j > 2):
                j = int(raw_input("Col should be between 0 and 2: "))
            while (isCross(state.grid, i, j) or isZero(state.grid, i, j)):
                print "Please enter unoccupied coordinates"
                i = int(raw_input("Enter X in row __: "))
                j = int(raw_input("Enter X in col __: "))
            for new_state in state.states:
                if (new_state.grid[i][j] == 'X'):
                    state = new_state
                    break
            print("\nYou: ")
        else:
            state = state.states[0]
            print("\nEarth's Mightiest Zeros: ")
    printToConsole(state.grid)
    zeros_move = not zeros_move
        
print("\n\nGame over:"),
if (ttp_lost(state.grid)):
    print("The Earth's Mightiest Zeros win!")
elif (zeros_lost(state.grid)):
    print("TicTacMan/Woman wins!")
else:
    print("Draw.")
