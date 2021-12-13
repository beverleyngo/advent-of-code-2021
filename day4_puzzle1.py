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

# Function to calculate the score
def calculate_board(board, n):
    boardsum = 0
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
            calculate_board(board, n)
            break

# Function to check for 'column bingo win' for a board
def checkwin_col(board, n):
    for i in range(5):
        if list(zip(*board))[i].count('X') == 5:  
            calculate_board(board, n)
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