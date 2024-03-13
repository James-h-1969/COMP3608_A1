def basic_get_nums_in_a_row(grid, p):
    """
        get_nums_in_a_row:
            @params: 
                grid: List[str] -> list of row stirings holding the current position
                p: str -> player color as either 'r' or 'y'
            @returns:
                nums: Dict[int] -> dictionary of how many in a row 

    """
    nums = {"2":0, "3":0, "4":0}
    # check rows
    for row in grid:
        current_in_a_row = 0
        for i in range(len(row)):
            if row[i] == p:
                current_in_a_row += 1
            else:
                if str(current_in_a_row) in nums.keys():
                    nums[str(current_in_a_row)] += 1
                current_in_a_row = 0
        if str(current_in_a_row) in nums.keys():
            nums[str(current_in_a_row)] += 1
        current_in_a_row = 0

  # check columns
    for i in range(len(grid[0])):
        current_in_a_column = 0
        for j in range(len(grid)):
            char = grid[j][i] # iterate through each row of the column
            if char == p:
                current_in_a_column += 1
            else:
                if str(current_in_a_column) in nums.keys():
                    nums[str(current_in_a_column)] += 1
                current_in_a_column = 0
        if str(current_in_a_column) in nums.keys():
            nums[str(current_in_a_column)] += 1

  # check diagonals
    AMOUNT_OF_DIAGONALS = 12
    i0, j0 = 5, 0
    for _ in range(AMOUNT_OF_DIAGONALS):
        current_in_diag = 0
        i, j = i0, j0
        while (i < len(grid) and j < len(grid[0])):
            char = grid[i][j]
            if char == p:
                current_in_diag += 1
            else:
                if str(current_in_diag) in nums.keys():
                    nums[str(current_in_diag)] += 1
                current_in_diag = 0
            i += 1
            j += 1
        if str(current_in_diag) in nums.keys():
            nums[str(current_in_diag)] += 1

        if i0 - 1 >= 0:
            i0 -= 1
        else:
            j0 += 1
    i0, j0 = 0, 0
    for _ in range(AMOUNT_OF_DIAGONALS):
        current_in_diag = 0
        i, j = i0, j0
        while (i < len(grid) and j >= 0):
            char = grid[i][j]
            if char == p:
                current_in_diag += 1
            else:
                if str(current_in_diag) in nums.keys():
                    
                    nums[str(current_in_diag)] += 1
                current_in_diag = 0
            i += 1
            j -= 1
        if str(current_in_diag) in nums.keys():
            nums[str(current_in_diag)] += 1
        if j0 + 1 < len(grid[0]):
            j0 += 1
        else:
            i0 += 1          
    return nums

  
def score(grid, p):
    in_a_row = basic_get_nums_in_a_row(grid, p)
    s = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == p:
                s += 1
    s += 10 * in_a_row["2"]
    s += 100 * in_a_row["3"]
    s += 1000 * in_a_row["4"]
    return s

def eval(grid):
    return score(grid, "r") - score(grid, "y")