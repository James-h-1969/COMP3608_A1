# get nums needs to handle more then 4   
import functions

def main(grid):
    grid = grid.split(",")
    for row in grid:
       print(row)
    print()
    print(f"Evaluation of the above grid: {functions.eval(grid)}")


main(".......,.......,.......,....y..,..ryryr,..yyrrr")


