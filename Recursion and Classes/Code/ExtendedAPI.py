"""
Firstly, implement ALL the functions from Functions.py using isCross 
(if they need it). After that, you can add pretty much any function you need
here, for Game.py.

"""

# You may need this method:

def printToConsole(Grid):
    """ This method prints the Grid onto the screen."""
    for i in range(0, 3):
        print("   |   |   ")
        print(""),
        for j in range(0, 3):
            if (isCross(Grid, i, j) or isZero(Grid, i, j)):
                print(Grid[i][j]),
            else:
                print(" "),
            if (j < 2):
                print ("|"),
        print("")
        if (not (i == 2)):
            print("___|___|___")
        else:
            print("   |   |   ")
            
# Re-implemented methods.

def put(Grid, x, y):
    Grid[x][y] = '0'
        
def isZero(Grid, x, y):
    """This function returns True if there is a '0' at (x, y)."""
    while (x > 2): 
        x = int(raw_input("Please enter an 'x' in {0, 1, 2}: "))
    while (y > 2):    
        y = int(raw_input("Please enter a 'y' in {0, 1, 2}: "))
    return (Grid[x][y] == '0')

def isCross(Grid, x, y):
    """This function returns True if there is an 'X' at (x, y)."""
    while (x > 2): 
        x = int(raw_input("Please enter an 'x' in {0, 1, 2}: "))
    while (y > 2):    
        y = int(raw_input("Please enter a 'y' in {0, 1, 2}: "))
    return (Grid[x][y] == 'X')


def zerosInRow(Grid, k):
    """This function returns the number of 0s in row 'k'."""
    # k is an integer in the set {0, 1, 2}. So, depending on k, we can get
    # the number of 0s in rows 0, 1, and 2. Here's how.
    
    while (k > 2):      # To keep trouble-makers at bay. Not important for now.
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (isZero(Grid, k, index)): # We're looking at row 'k', which can be ..
            count = count + 1        # .. any row, really. We chose the 'k'.   
        else:
            pass
        index = index + 1          
    return count         

def crossesInRow(Grid, k):
    """This function returns the number of Xs in row 'k'."""
    # k is an integer in the set {0, 1, 2}. So, depending on k, we can get
    # the number of 0s in rows 0, 1, and 2. Here's how.
    
    while (k > 2):      # To keep trouble-makers at bay. Not important for now.
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (isCross(Grid, k, index)): # We're looking at row 'k', which can be ..
            count = count + 1         # .. any row, really. We chose the 'k'.   
        else:
            pass
        index = index + 1          
    return count         

def zerosInCol(Grid, k):
    """This function will return the number of 0s in column k."""
    while (k > 2):      
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (isZero(Grid, index, k)): 
            count = count + 1      
        else:
            pass
        index = index + 1          
    return count

def crossesInCol(Grid, k):
    """This function will return the number of Xs in column k."""
    while (k > 2):      
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (isCross(Grid, index, k)): 
            count = count + 1      
        else:
            pass
        index = index + 1          
    return count 
    

def InDiag1(Grid, char): # Notice the extra argument?
    """This function will return the number of 0s (or Xs) in the main diagonal."""
    count = 0
    index = 0
    while (index < 3):
        if (Grid[index][index] == char):
            count = count + 1
        else:
            pass
        index = index + 1
    return count
            
    
def InDiag2(Grid, char):   
    """This function will return the number of 0s (or Xs) in the other diagonal."""
    count = 0
    i = 0
    while (i < 3):
        if (Grid[i][2-i] == char): 
            count = count + 1
        else:
            pass
        i = i + 1
    return count

def threatInRow(Grid, i):
    return (crossesInRow(Grid, i) > 1 and zerosInRow(Grid, i) == 0)

def threatInCol(Grid, i):
    return (crossesInCol(Grid, i) > 1 and zerosInCol(Grid, i) == 0)

def threatInDiagonal1(Grid):
    return ((InDiag1(Grid, 'X') > 1 and InDiag1(Grid, '0') == 0))

def threatInDiagonal2(Grid):
    return ((InDiag2(Grid, 'X') > 1 and InDiag2(Grid, '0') == 0))

def boardFacesThreat(Grid):
    """ This function will return true if the board is under threat for the Earth's Mightiest Zeros."""
    for i in range(0, 3):
        if (threatInRow(Grid, i)):
            return True
        elif (threatInCol(Grid, i)):
            return True
    if (threatInDiagonal1(Grid) or threatInDiagonal2(Grid)):
        return True
    return False
    
def zeros_lost(Grid):
    """This function will return True if we have lost the game."""
    i = 0
    while (i < 3):
        if (crossesInRow(Grid, i) == 3):
            return True
        elif (crossesInCol(Grid, i) == 3):                          # Else, If {...}
            return True
        else:
            pass
        i += 1
    if (InDiag1(Grid, 'X') == 3 or InDiag2(Grid, 'X') == 3):
        return True
    else:
        return False

def ttp_lost(Grid):
    """This function will return True if we have lost the game."""
    i = 0
    while (i < 3):
        if (zerosInRow(Grid, i) == 3):
            return True
        elif (zerosInCol(Grid, i) == 3):                          # Else, If {...}
            return True
        else:
            pass
        i = i + 1
    if (InDiag1(Grid, '0') == 3 or InDiag2(Grid, '0') == 3):
        return True
    else:
        return False

def draw(Grid):
    """This function returns a draw if the game ends in a draw."""
    if (ttp_lost(Grid) or zeros_lost(Grid)):
        return False
    for i in range(3):
        for j in range(3):
            if (Grid[i][j] != 'X' and Grid[i][j] != '0'):
                return False
    return True

def game_end(Grid):
    """ This function returns True if the game has ended """
    return (draw(Grid) or zeros_lost(Grid) or ttp_lost(Grid))
