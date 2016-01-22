def initBoard(n):
    plateau = []
    for i in range(0, n):
        plateau.append([])
        for j in range(0, n):
            plateau[i].append(0)
    return plateau

def affichePlateau(plateau):
    n = len(plateau)
    print ""
    for i in range(0, n):
        for j in range(0, n):
            print "\t",plateau[i][j],
        print ""