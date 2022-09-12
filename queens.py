n = int(input("N: "))
n_queens = 0
tab = [[0 for i in range(n)] for j in range(n)]
best_queen = 0

count = 0


def print_board():
    for i in range(n):
        for j in range(n):
            print(tab[i][j], end=' ')
        print()


def queen_count():
    count = 0 
    for i in range(n):
        for j in range(n):
            if tab[i][j] == "Q":
                count+=1
    return count


def check_diagonal( i,j):
    counter = 1
    while ((i + counter) <= n - 1 and (j + counter) <= n - 1):
        if tab[i + counter][j + counter] == "Q":
            return False
        counter += 1
    counter = 1

    while ((i - counter) >= 0 and (j - counter) >= 0):
        if tab[i - counter][j - counter] == "Q":
            return False
        counter += 1
    counter = 1

    while ((i + counter) <= n-1 and (j - counter) >= 0):
        if tab[i + counter][j - counter] == "Q":
            return False
        counter += 1
    counter = 1

    while ((i - counter) >= 0 and (j + counter) <= n-1):
        if tab[i - counter][j+counter] == "Q":
            return False
        counter += 1
    return True
    
    
def check_horizontal( i,j):
    for x in range(n):
        if tab[i][x] == "Q" and x != j:
            return False
    return True


def check_vertical( i,j):
    for x in range(n):
        if tab[x][j] == "Q" and x != i:
            return False
    return True


# check for available positions in the row
def is_valid(i):
    pos = []
    for x in range(n):
        if check_horizontal(i,x):
            if check_vertical(i,x):
                if check_diagonal(i,x):
                    pos.append([i,x])
    
    return pos

# recursive function
def add_queen(i,j):
    global best_queen
    global count
    # escape condition
    if i > n-1:
        n_queens = queen_count()
        if n_queens >= best_queen:
            count += 1
            best_queen = n_queens
            
        return False

    possivel = is_valid(i)
    # if there are possibilities in the row 
    # add a queen to the first possible spot
    if len(possivel) > 0:
        for x in possivel:
            tab[x[0]][x[1]] = "Q"
            if not add_queen(i+1, x[1]):
                tab[x[0]][x[1]] = 0

add_queen(0,0)
print(count)