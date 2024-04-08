import sys
import threading
import time


def game_over(grid, p):
    # check 4 in a row in rows
    for row in range(len(grid)):
      in_a_row = 0
      for col in range(len(grid[0])):
        if grid[row][col] == p:
          in_a_row += 1
        else:
          in_a_row = 0
        if in_a_row == 4:
          return True
      
    for col in range(len(grid[0])):
      in_a_col = 0
      for row in range(len(grid)):
        if grid[row][col] == p:
          in_a_col += 1
        else:
          in_a_col = 0
        if in_a_col == 4:
          return True
      
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
                current_in_diag = 0
            if current_in_diag == 4:
              return True
            i += 1
            j += 1

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
                current_in_diag = 0
            if current_in_diag == 4:
              return True
            i += 1
            j -= 1
        if j0 + 1 < len(grid[0]):
            j0 += 1
        else:
            i0 += 1   
            
    return False

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
    other_p = "r" if p == "y" else "y"
    # check rows
    for row in grid:
        current_in_a_row = 0
        for i in range(len(row)):
            if row[i] == p:
                current_in_a_row += 1
                start = row[i-1] if i -1 > 0 else other_p
            else:
                if current_in_a_row > 4:
                    current_in_a_row = 4
                if str(current_in_a_row) in nums.keys() and (row[i] != other_p or start != other_p):
                    nums[str(current_in_a_row)] += 1
                current_in_a_row = 0
        if current_in_a_row > 4:
            current_in_a_row = 4
        if str(current_in_a_row) in nums.keys():
            nums[str(current_in_a_row)] += 1

  # check columns
    for i in range(len(grid[0])):
        current_in_a_column = 0
        for j in range(len(grid)-1, 0, -1):
            char = grid[j][i] # iterate through each row of the column
            if char == p:
                current_in_a_column += 1
            else:
                if current_in_a_column > 4:
                    current_in_a_row = 4
                if str(current_in_a_column) in nums.keys() and char != other_p:
                    nums[str(current_in_a_column)] += 1
                current_in_a_column = 0
        if current_in_a_column > 4:
            current_in_a_column = 4
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
                if current_in_diag > 4:
                    current_in_diag = 4
                if str(current_in_diag) in nums.keys():
                    nums[str(current_in_diag)] += 1
                current_in_diag = 0
            i += 1
            j += 1
        if current_in_diag > 4:
            current_in_diag = 4
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
                if current_in_diag > 4:
                    current_in_diag = 4
                if str(current_in_diag) in nums.keys():
                    nums[str(current_in_diag)] += 1
                current_in_diag = 0
            i += 1
            j -= 1
        if current_in_diag > 4:
            current_in_diag = 4
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

def eval(grid, p):
    other_p = "r" if p == "y" else "y"
    if (game_over(grid, p)):
        return 10_000
    if (game_over(grid, other_p)):
        return -10_000
    return score(grid, p) - score(grid, other_p)
  
# get nums needs to handle more then 4   
COLUMNS = 7
ROWS = 6

COLUMN_ORDER = [3,2,4,1,5,0,6]

class Node():
    def __init__(self, board_state, depth, column, color):
        self.board_state = board_state
        self.depth = depth
        self.val = 0
        self.column = column
        self.children = []
        self.color = color

    def set_val(self, colour):
        self.val = eval(self.board_state, colour)

    def get_children(self, colour):
        for c in range(COLUMNS):
            j = COLUMN_ORDER[c]
            if self.board_state[0][j] != ".":
                continue
            i = 1
            collision = False
            while i  < ROWS and not collision:
                collision = self.board_state[i][j] != "."
                i += 1
            i -= 2 if collision else 1
            new_board_state = self.board_state.copy()
            new_board_state[i] = new_board_state[i][:j] + self.color + new_board_state[i][j+1:]
            new_color = self.get_opp_colour()
            newNode = Node(new_board_state, self.depth + 1, j, new_color)
            self.children.append(newNode)   

    def get_opp_colour(self):
        return "y" if self.color == "r" else "r"

def minmax(node: Node, alpha, beta, max_depth, colour):   
    g_over = game_over(node.board_state, node.get_opp_colour())
    if node.depth == max_depth or g_over:
        node.set_val(colour)
        if g_over:  
            amount = -10_000 if colour == node.get_opp_colour() else 10_000
        else:
            amount = node.val
        return (node.column, amount, 1)
    
    node.get_children(colour)

    finding_max = (node.depth % 2 == 0)
    
    counter = 0
    if len(node.children) > 0:
        final_val =-1 * sys.maxsize if finding_max else sys.maxsize
        final_col = 0
        for child in node.children:
            curr_col, curr_val, n_children = minmax(child, alpha, beta, max_depth, colour)
            counter += n_children
            if finding_max and curr_val > final_val:
                final_val = curr_val
                final_col = curr_col
            elif not finding_max and curr_val < final_val:
                final_val = curr_val
                final_col = curr_col

            if finding_max:
                alpha = max([alpha, curr_val])
                if beta <= alpha:
                    break
            else:
                beta = min([beta, curr_val])
                if beta <= alpha:
                    break
                
    else:
        node.set_val(colour)
        return (node.column, node.val, 1)
    

    return (final_col, final_val, counter+1)
  
def connect_four_final(grid, colour, depth):
    grid = grid.split(",")
    grid.reverse()
    p = "r" if colour == "red" else "y"
    initial_node = Node(grid, 0, 0, p)
    col, val, count = minmax(initial_node, -1 * sys.maxsize, sys.maxsize, depth, p)
    return f"{col}\n{count}"

def connect_four_ab_timed(grid, colour, depth):
    # Function to run connect_four_ab with a time limit of 1 second
    def run_with_timeout():
        # Run the original function and store the result
        result = connect_four_final(grid, colour, depth)
        # Store the result in a global variable
        global result_data
        result_data = result

    # Initialize a threading object with the target function
    thread = threading.Thread(target=run_with_timeout)
    # Start the thread
    thread.start()
    # Join the thread with a timeout of 1 second
    thread.join(timeout=1)

    # Check if the thread is still alive (meaning it hasn't finished within 1 second)
    if thread.is_alive():
        return "Timeout occurred: The function took longer than 1 second to execute."
    else:
        # Return the result obtained from the function
        return result_data

if __name__ == '__main__':
    # Example function call below, you can add your own to test the connect_four_mm function
    print(connect_four_final("r...y..,r......,r......,.......,.......,.......", "yellow", 6))