from Gamestate import *

Grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

state = Gamestate(Grid, True, 1)

state.make_states()

state.calculate_value()

for st in state.states:
    printToConsole(st.grid),
    print("Value: "),
    print(st.value)

