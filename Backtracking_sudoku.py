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

def complete(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return False
        return True

def possibilities(position_x, position_y):
    
    possibles = [1,2,3,4,5,6,7,8,9]

    for fileira in range(9):
        # pegar todos os numeros da fileira e tirar eles de cogitação como opção pra aquele lugar
        value = grid[fileira][position_y] 
        if value == 0:
            continue
        if value in possibles:
            possibles.remove(int(value))
    
    for coluna in range(9):
        # pegar todos os numeros da fileira e tirar eles de cogitação como opção pra aquele lugar
        value = grid[position_x][coluna] 
        if value == 0:
            continue
        if value in possibles:
            possibles.remove(int(value))

    # pegar todos os numeros do quadrado e tirar eles do array possible
    quadrant = [int(position_x/3), int(position_y/3)]
        
    for fileira in range(quadrant[0] * 3, quadrant[0] * 3 + 3):
        for coluna in range(quadrant[1] * 3, quadrant[1] * 3 + 3):
            value = grid[fileira][coluna] 
            if value == 0:
                continue
            if value in possibles:
                possibles.remove(int(value))

    return possibles

def solve():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 0:
                possibles = possibilities(row,col)
                for number in possibles:
                    grid[row][col] = number
                    if not solve():
                        grid[row][col] = 0
                return False
    print_board(grid)

solve()
