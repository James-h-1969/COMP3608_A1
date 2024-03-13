# get nums needs to handle more then 4   
from functions import eval

def main(grid):
    grid = grid.split(",")
    for row in grid:
       print(row)
    print()
    print(f"Evaluation of the above grid: {eval(grid)}")


main(".......,.......,.......,....y..,..ryryr,..yyrrr")


