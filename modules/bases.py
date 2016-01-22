
def initBoard(n):
    board = []
    for i in range(0, n):
        board.append([])
        for j in range(0, n):
            board[i].append(0)
    return board


def display(board):
    n = len(board)
    print ""
    for i in range(0, n):
        for j in range(0, n):
            print "\t",board[i][j],
        print ""