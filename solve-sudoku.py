str = '....18.6....3...5..6.....4.....5...86....3....79.4.2...4....3..5....2.16.236.....'

arr = list(str)

print(arr)
'''

...|.18|.6.
...|3..|.5.
.6.|...|.4.

-----------

...|.5.|..8
6..|..3|...
.79|.4.|2..

-----------

.4.|...|3..
5..|..2|.16
.23|6..|...

input :
....18.6....3...5..6.....4.....5...86....3....79.4.2...4....3..5....2.16.236.....

output :
295418763714369852368725941431257698652893174879146235946581327587932416123674589

'''

'''
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty cell means the board is solved
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Make tentative assignment
            
            if solve_sudoku(board):
                return True  # Return true if the board is solved
            
            board[row][col] = 0  # Undo assignment (backtrack)
    
    return False  # Trigger backtracking

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, row, col, num):
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

# Initial board
board = [
    [0, 0, 0, 0, 1, 8, 0, 6, 0],
    [0, 0, 0, 3, 0, 0, 0, 5, 0],
    [0, 6, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 8, 6],
    [0, 0, 0, 3, 0, 0, 0, 0, 0],
    [7, 9, 0, 4, 0, 2, 0, 0, 0],
    [4, 0, 0, 0, 0, 3, 0, 5, 0],
    [0, 2, 3, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0]
]

if solve_sudoku(board):
    for row in board:
        print(row)
else:
    print("No solution exists")

'''