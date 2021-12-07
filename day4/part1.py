
with open("input1.txt") as file:
    winning_nums = [int(num)
                    for num in file.readline().rstrip("\n").split(",")]
    boards = []
    while file.readline():
        board = []
        for i in range(5):
            board.extend([int(x) for x in file.readline().rstrip(
                "\n").split(" ") if x != ''])
        boards.append(board)


def is_winner(board):
    # checking rows for a winner
    start = 0
    for i in range(5):
        if board[start] + board[start+1] + board[start+2] + board[start+3] + board[start+4] == 500:
            return True
        start += 5

    # checking columns for a winner
    start = 0
    for i in range(5):
        if board[start] + board[start+5] + board[start+10] + board[start+15]+board[start+20] == 500:
            return True
        start += 1

    return False  # No winner


win = False
i = 0
while win == False and i < len(winning_nums):
    number = winning_nums[i]
    for board in boards:
        for j in range(len(board)):
            if board[j] == number:
                board[j] = 100

    for board in boards:
        if is_winner(board):
            total = sum([x for x in board if x != 100])
            score = total * number
            print(score)

            win = True
    i += 1
