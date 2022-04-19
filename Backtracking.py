import time

grid = [[ 5 , 3 , 0 , 0 , 7 , 0 , 0 , 0 , 0 ],
    [ 6 , 0 , 0 , 1 , 9 , 5 , 0 , 0 , 0 ],
    [ 0 , 9 , 8 , 0 , 0 , 0 , 0 , 6 , 0 ],
    [ 8 , 0 , 0 , 0 , 6 , 0 , 0 , 0 , 3 ],
    [ 4 , 0 , 0 , 8 , 0 , 3 , 0 , 0 , 1 ],
    [ 7 , 0 , 0 , 0 , 2 , 0 , 0 , 0 , 6 ],
    [ 0 , 6 , 0 , 0 , 0 , 0 , 2 , 8 , 0 ],
    [ 0 , 0 , 0 , 4 , 1 , 9 , 0 , 0 , 5 ],
    [ 0 , 0 , 0 , 0 , 8 , 0 , 0 , 7 , 9 ],]

# drawing the grid
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print()
            print('- - - - - - - - - - - - ')
        else:    
            print()
        for j in range(len(board)):
            if j % 3 == 0 or  j == 9:
                print('| ', end='')
                
            print(board[i][j],'', end='')
    print()
    print('- - - - - - - - - - - - ')

print_board(grid)

# check if the board is complete
def complete(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ' 0':
                return False
        return True

def valid(position_x, position_y, number):

    for fileira in range(9):
        # pegar todos os numeros da fileira e tirar eles de cogitação como opção pra aquele lugar
        value = grid[fileira][position_y] 
        if number == value:
            return False
    
    for coluna in range(9):
        # pegar todos os numeros da fileira e tirar eles de cogitação como opção pra aquele lugar
        value = grid[position_x][coluna] 
        if number == value:
            return False

    # pegar todos os numeros do quadrado e tirar eles do array possible
    quadrant = [int(position_x/3), int(position_y/3)]
    for fileira in range(quadrant[0] * 3, quadrant[0] * 3 + 3):
        for coluna in range(quadrant[1] * 3, quadrant[1] * 3 + 3):
            value = grid[fileira][coluna] 
        if number == value:
            return False
    return True

def solve():
    for row in range(len(grid)):
        for col in range(len(grid[row])):            
            if grid[row][col] == 0:
                # looping through all possible values
                for number in range(1,10):
                    if valid(row,col,number):
                        grid[row][col] = number
                        # if its valid put it in the grid and call solve with the modified grid
                        if not solve():
                        # if solve return false we make the previous location = 0 and try another possibility
                            grid[row][col] = 0
                return False
    print_board(grid)

# main
solve()
