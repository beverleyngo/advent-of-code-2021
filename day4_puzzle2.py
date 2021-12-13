# Get the number and board data
with open('day4_input.txt', 'r') as f:
    num_data, *board_data = f.read().split('\n\n')

# Create a nested list of boards, with each board being a list of lists
def create_boards(num_data, board_data):
    nums = [int(i) for i in num_data.split(',')]
    boards = []
    for board in board_data:
        boards.append([[int(i) for i in row.split()] for row in board.split('\n')])
    return nums, boards

# Initialise the board
nums, boards = create_boards(num_data, board_data)

# Keep track of already-won boards, and calculate the score for the final board
boards_already_won = []
def calculate_last_board(board, n):
    boardsum = 0
    if boards.index(board) not in boards_already_won:
        boards_already_won.append(boards.index(board))
    if len(boards_already_won) == len(boards):
        for board in board:
            for i in board:
                if isinstance(i, int):
                    boardsum += i
        print(boardsum * nums[n])
        exit()

# Function to check for 'row bingo win' for a board
def checkwin_row(board, n):
    for row in board:
        if row.count('X') == 5:
            calculate_last_board(board, n)
            break

# Function to check for 'column bingo win' for a board
def checkwin_col(board, n):
    for i in range(5):
        if list(zip(*board))[i].count('X') == 5:  
            calculate_last_board(board, n)
            break

# Loop through numbers and check for bingo for each board
for n in range(len(nums)):
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[i][j] == nums[n]:
                    board[i][j] = 'X'
        checkwin_row(board, n)
        checkwin_col(board, n)