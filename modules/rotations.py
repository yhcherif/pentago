# Roation d'une liste dans le sens des aiguilles d'une montre
def clockWise(board, m):
    rotated = [[0 for x in range(0, m)] for y in range(0, m)]
    limit = m -1
    for i in range(0, m):
        for j in range(0, m):
            rotated[j][ limit - i] = board[i][j]
    return rotated

# Roation d'une liste dans le sens contraire des aiguilles d'une montre
def reverseClockWise(board, m):
    rotated = [[0 for x in range(0, m)] for y in range(0, m)]
    limit = m -1
    for i in range(0, m):
        for j in range(0, m):
            rotated[limit - j][i] = board[i][j]
    return rotated


# Effectue la rotation du quadrant d'une liste selon le sens passe en parametre
def rotate(n, list, quardrant, direction):
    x =0;
    y =0;
    p = n/2
    keys = {1:[0, 0], 2:[p,0], 3:[p,p], 4:[0,p]}
    if quardrant in range(1, 5):
        x,y = keys[quardrant][0], keys[quardrant][1]
        size = n/2
        unrotated = [[0 for t in range(0, size)] for v in range(0, size)]
        a,b = 0,0
        for i in range(x, x+size):
            for j in range(y, y+size):
                unrotated[a][b] = list[i][j]
                b+=1
            a+=1
            b=0
        rotated = None
        if(direction == True):
            rotated = clockWise(unrotated, size)
        else:
            rotated = reverseClockWise(unrotated, size)
        a,b = 0,0
        for i in range(x, x+size):
            for j in range(y, y+size):
                list[i][j] = rotated[a][b]
                b+=1
            a+=1
            b=0
        return list
    else:
        print "il n'existe que 4 quardrant dans ce jeu"