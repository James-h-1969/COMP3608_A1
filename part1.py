# get nums needs to handle more then 4   
import functions

MAX_DEPTH = 2
COLUMNS = 7
ROWS = 6

class Node():
    def __init__(self, board_state, depth, column, color):
        self.board_state = board_state
        self.depth = depth
        self.val = 0
        self.column = column
        self.children = []
        self.color = color

    def set_val(self):
        self.val = functions.eval(self.board_state)

    def get_children(self):
        for j in range(COLUMNS):
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
            new_color = "r" if self.color == "y" else "r"
            newNode = Node(new_board_state, self.depth + 1, j, new_color)
            self.children.append(newNode)        

def minmax(node: Node):   
    if node.depth == MAX_DEPTH:
        node.set_val()
        return (node.column, node.val, 1)
    
    node.get_children()

    finding_max = (node.depth % 2 == 0)
    
    counter = 0
    if len(node.children) > 0:
        final_val = float("-inf") if finding_max else float("inf")
        final_col = 0
        for child in node.children:
            curr_col, curr_val, n_children = minmax(child)
            counter += n_children
            if finding_max and curr_val > final_val:
                final_val = curr_val
                final_col = curr_col
            elif not finding_max and curr_val < final_val:
                final_val = curr_val
                final_col = curr_col
    else:
        node.set_val()
        return (node.column, node.val, 1)

    return (final_col, final_val, counter)


def main(grid, colour):
    grid = grid.split(",")
    grid.reverse()
    p = "r" if colour == "red" else "y"
    initial_node = Node(grid, 0, 0, p)
    col, val, count = minmax(initial_node)
    print(col)
    print(count+1)


main(".ryyrry,.rryry.,..y.r..,..y....,.......,.......", "red")


