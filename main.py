# Getting python constraint, the ./python-constraint-1.1 contains constraint.py file
import sys, math
import time

# Importing constraint
from constraint import *

def solve(size = 9):
    #creates a problem object
    problem = Problem() # FIXME ?? Add recursiveBacktrackingSolver?

    rows = range(size)
    cols = range(size)

    #creates a tuple structure for the board
    board = [(row, col) for row in rows for col in cols]

    # open the file and stores the numbers in a list. Ex: [1,2,9,0,3...]
    file_name = sys.argv[1]
    ints = []
    with open(file_name) as f:
        for line in f:
            ints.extend([int(number) for number in line.split(",")])

    #add our list to the board
    foo = zip(board,ints)
    foo_list = list(foo)

    #adding each cell as a variable
    for coordinate, value in foo_list:
        if value == 0:
            problem.addVariable(coordinate,range(1,10))
        else:
            problem.addVariable(coordinate,[value]) #coordinate is variable we want to add to problem and [value] is the range


    #define each row and column and add constraints to the row/column
    for i in range(9):
        each_row = []
        each_col = []
        for j in range(9):
            each_row.append((i,j))
            each_col.append((j,i))
        problem.addConstraint(AllDifferentConstraint(), each_row)
        problem.addConstraint(AllDifferentConstraint(), each_col)


    #adding constraint for boxes
    for row in range(9):
        index = row//3
        each_box = [(r, c) for r in range(3) for c in range(3)] #creates 3*3 of (row,col) tuple
        each_box.clear()
        for i in range(3):
            for j in range(3):
                each_box.append((i+index*3, j + row%3*3))
        problem.addConstraint(AllDifferentConstraint(), each_box)

    start = time.time()
    solution = problem.getSolution()
    end = time.time()
    print("EXECUTION TIME=", end-start)
    print("\n------+-------+------")
    for row in range(9):
        for col in range(9):
            var = solution[row,col]
            if var == 0:
                print(".", end='')
            else:
                print(var, end='')
            print(" ", end='')
            if col % 3 == 2 and col != 8:
                print("| ", end='')
        print()
        if row % 3 == 2:
            print("------+-------+------")

solve()