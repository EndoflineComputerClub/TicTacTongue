"""
This code will help you understand the workings of TicTacTongue. 
You'll write your own strategy (algorithm), and play against it. 

Make sure you read the syntax and the readme file before starting here.

Remember: The instructions - your team - is called Earth's Mightiest Zeros! 
It will be important later (when you realize just how awesome Marvel is).

Reading code can be a little dry - but don't give up! Read this file, please. 

"""

# NOTE: The words 'line' and 'instruction' have been used interchangeably, as,
# mostly, in a program, there is one instruction per line (roughly). 
# May or may not be true for individual lines. Sometimes, two or even three 
# instructions can be on one line. But we'll assume there's just one per line.

# A function (or a method) is a set of instructions. Now, why do we use 
# functions? A very common example is this - say you want to do something that 
# takes a couple of instructions (say 10). And you want to do it many times, 
# at different places in your code. 

# Now, if you make a function of those instructions, instead of 
# writing those same (or similar) 10 lines everywhere in your code, you can 
# write the 10 lines once, and CALL the function of those 10 lines everywhere.

# Calling a function takes only one line, so, if you needed that code in 20 
# places, instead of 200 lines, you use only 30. This makes reading and 
# maintaining code much easier and better.  


# We're setting up an empty 3x3 grid. The game shall be played here.

Grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  

# Basically, we created 3 rows, each row containing 3 empty boxes. And then,
# we stacked those rows upon one-another. Remember, numbering of rows as well as
# columns starts from 0. 


def crossesInRowZero():
    """This function returns the number of Xs in row zero (0).""" 
    count = 0                           # This will count the number of X's in the row.
    index = 0                           # This is the column index in row 0. 
    while (index < 3):                  # While loop starts.   <----------<---   
        if (Grid[0][index] == 'X'):     # If there's an X at (0, index) ...   ^
            count = count + 1           # ... increase count by 1.             ^
        else:                           # If there isn't an X at (0, index) .. ^
            pass                        # .. do nothing.                       ^ 
        index = index + 1               # Either way, now look at the next box ^
    #    Follow this arrow for the next iteration.  ---->----------->---------^ 
    
    # We've looked at all boxes in row 0. Now index = 3. We're out of the loop.
    return count                                                 # We are done!
    
    
def crossesInRowOne():
    """This function returns the number of Xs in row one (1)."""     
    # Everything is similar to the previous function (crossesInRowZero). 
    count = 0
    index = 0
    while (index < 3):
        if (Grid[1][index] == 'X'):
            count = count + 1
        else:
            pass
        index = index + 1          
    return count


def crossesInRowTwo():
    """This function returns the number of Xs in row two (2)."""     
    # Everything is similar to the crossesInRowZero and crossesInRowOne. 
    count = 0
    index = 0
    while (index < 3):
        if (Grid[2][index] == 'X'):
            count = count + 1
        else:
            pass
        index = index + 1          
    return count        

# The previous three functions (the only three so far, actually) simply gave us
# the number of Xs in their respective rows. To do such a simple task, we had 
# to write THREE nearly identical functions! Obviously, programming is not so 
# boring (if it was, nobody would be doing it). Can you think of a trick? 

# What if I can TELL the function which row it should look in? 
# This is a very important concept called PASSING AN ARGUMENT to a function.
# An argument is a piece of information, like an integer, that we give to an 
# entity, like a function, which helps the function perform. Here's an example.


def crossesInRow(k):
    """This function returns the number of Xs in row 'k'."""
    # k is an integer in the set {0, 1, 2}. So, depending on k, we can get
    # the number of Xs in rows 0, 1, and 2. Here's how.
    
    while (k > 2):      # To keep trouble-makers at bay. Not important for now.
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (Grid[k][index] == 'X'): # We're looking at row 'k', which can be ..
            count = count + 1       # .. any row, really. We chose the 'k'.   
        else:
            pass
        index = index + 1          
    return count 

# It is important that you understand how crossesInRowK works, because, we'll
# use it from now on. Let's use it to calculate threat in a row. This also 
# demonstrates how a function can also call, and be called by, another function.          
     
def threatPresent(k):  
    """This function will return True if there is a threat in row k."""
    nX = crossesInRow(k)
    if (nX >= 2):
        return True;
    else:
        return False;

# Now, we can use our knowledge so far to detect if we're under threat or not.

def boardFacesThreat():
    """This function will return True if there is a threat on board."""
    if (threatPresent(0) or threatPresent(1) or threatPresent(2)):
         return True
    else:
        return False        

# Basically, we say that if either row 0 or row 1 or row 2 have a threat, then
# we're under threat. 

# ---------------------------------------------------------------------------

# At this point, please try writing your own function to count the number of 
# crosses in a column. The function should be called crossesInColK, and it 
# should take in an argument that tells it which column to check. 

# Easy challenge - Try making a function for each diagonal too. Our versions:

def crossesInCol(k):
    """This function will return the number of Xs in column k."""
    while (k > 2):      
        k = int(raw_input("Please enter a value in {0, 1, 2}: "))  
    count = 0
    index = 0
    while (index < 3):
        if (Grid[index][k] == 'X'): 
            count = count + 1      
        else:
            pass
        index = index + 1          
    return count 
    

def crossesInDiag1():   # The Top-Left -> Bottom-Right diagonal (main diagonal).
    """This function will return the number of Xs in the main diagonal."""
    count = 0
    index = 0
    while (index < 3):
        if (Grid[index][index] == 'X'):
            count = count + 1
        else:
            pass
        index = index + 1
    return count
    
def crossesInDiag2():   # The other diagonal.
    """This function will return the number of Xs in the other diagonal."""
    count = 0
    i = 0
    while (i < 3):
        if (Grid[i][2-i] == 'X'): # What if we replace Grid[i][2-i] with Grid[2-i][i]?
            count = count + 1
        else:
            pass
        i = i + 1
    return count
    
# Based on all you've done so far, can you write a function to see if you lost?   

def lost():
    """This function will return True if we have lost the game."""
    i = 0
    while (i < 3):
        if (crossesInRow(i) == 3):
            return True
        elif (crossesInCol(i) == 3):                          # Else, If {...}
            return True
        else:
            pass
        i += 1
    if (crossesInDiag1 == 3 or crossesInDiag2 == 3):
        return True
    else:
        return False
    
# Phew. These were all, umm, 'checker' methods. Now let's actually make something
# to play. Let's make a function that can put a 0 on the Grid, if we give it 
# the coordinates. This is an instance of a function that takes in multiple 
# arguments. Remember that in Tic-Tac-Tongue, this function was called 'put'.

def put(x, y):
    """Simply puts a '0' at position (x, y) on the Grid."""
    while (x > 2): 
        x = int(raw_input("Please enter an 'x' in {0, 1, 2}: "))
    while (y > 2):    
        y = int(raw_input("Please enter a 'y' in {0, 1, 2}: "))
    # Simplest. Function. Ever. Probably even unnecessary.    
    Grid[x][y] = '0'
    # But we're doing it because we want to implement the TicTacTongue language. 

# The other function mentioned in the syntax was isCross. Also very simple.
# See how it was all so simple? We're nice like that. ;)

def isCross(x, y):
    """This function returns True if there is an X at (x, y)."""
    while (x > 2): 
        x = int(raw_input("Please enter an 'x' in {0, 1, 2}: "))
    while (y > 2):    
        y = int(raw_input("Please enter a 'y' in {0, 1, 2}: "))
    #Also the Simplest. Function. Ever.    
    return (Grid[x][y] == 'X')


# This should be very easy -> implement all the methods once again, but using 
# isCross. 
    
# Now, you have used if, while, isCross and put. So, did you use TicTacTongue,
# or Python? Haha. Well, rest assured, you actually used Python. TicTacTongue, 
# can conceptually be a language, but, it really is a very trivial library, 
# written in Python. 

# A library is basically a set of functions (and other stuff) that extend the 
# functionality of a language. You write a library so that if you ever have to 
# use that code again, you don't have to re-write it. And you can share it with
# others, who won't have to write it from scratch.

# After this, head to Library.py! 
