n = int (input("Enter the Value of n: "))

#Initialising the board
board = [[0 for i in range(n)]for i in range(n)]

# #Printing the board
# for row in board :
#     print (row)

#checking for Colomn
def check_colomn(board, row, colomn):
    for i in range(row, -1, -1):
        if board[i][colomn]==1:
            return False
    return True

#For Diagonal
def check_diagonal(board, row, colomn):
    for i, j in zip(range(row, -1, -1),range(colomn, -1, -1)):
        if board[i][j]==1:
            return False
    for i, j in zip(range(row, -1, -1),range(colomn, n)):
        if board[i][j]==1:
            return False
    return True

#backtracking
def nQn(board, row):
    if row==n:
        return True

    for i in range(n):
        if(check_colomn(board, row, i)==True and check_diagonal(board, row, i)==True):
            board[row][i]=1
            if nQn(board, row+1):
                return True
            board[row][i]=0
    return False

nQn(board, 0)

for row in board:
    print(row)
