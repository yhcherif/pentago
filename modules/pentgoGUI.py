import pygame, sys, os
from bases import *
from rotations import *
from alignements import *

# Declaration des codes couleurs
RED =   (255,   0,   0)
COLORS = {0 : (160, 160, 160),
1 : (255, 255, 255),
2 : (0,0,0)}

# Declaration des positions et index des quadrants
q= [
    [(50, 50), (0,0)],
    [(50, 210), (3, 0)],
    [(210, 210), (3, 3)],
    [(210, 50), (0,3)]
]

# Assignation des images et coordonnees des fleches de rotation
arrows = {
    1: [
         ["arrow_left_left.png",(10, 96)],["arrow_right_top.png", (96, 10)]
    ],
    2: [
        [ "arrow_left_bottom.png", (96, 360)], ["arrow_right_left.png", (10, 260)]
    ],
    3: [
        ["arrow_left_right.png", (370, 260)],[ "arrow_right_bottom.png", (260, 361)]
    ],
    4: [
        ["arrow_left_top.png", (260, 10)],[ "arrow_right_right.png", (370, 96)]
    ]

}

# Initialisation de pygame et pygame.font
pygame.init()
pygame.font.init()
# Affectation de la police Arial
myfont = pygame.font.Font("modules/arial.ttf", 17)

# Dessiner le plateau du jeu
def dessinerPlateau(liste, surface):
    rafraichirQuardrant([liste[e][0:3] for e in range(0, 3)], surface, 50, 50)
    rafraichirQuardrant([liste[e][0:3] for e in range(3, 6)], surface, 50, 210)
    rafraichirQuardrant([liste[e][3:6] for e in range(0, 3)], surface, 210, 210)
    rafraichirQuardrant([liste[e][3:6] for e in range(3, 6)], surface, 210, 50)

# Dessiner un quadrant du plateau
def rafraichirQuardrant(liste, surface, x, y):
    pygame.draw.rect(surface, RED, (x, y, 150, 150), 0 )
    x += 30
    y +=30
    for i in range(0, len(liste)):
        for j in range(0, len(liste)):
            pygame.draw.circle(surface, COLORS[liste[i][j]] , [x+j*45, y+i*45], 15)

# Poser un pion sur le plateau
def poserUnPion(liste, surface, player):
    dessinerPlayer(surface, player)
    pos = pygame.mouse.get_pos()
    detectCollision(liste, surface, play())

# Indique le joueur dont c'est le tour
def dessinerPlayer(surface, player):
    # Dessine la bordure
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)
    pygame.display.flip()
    string = "Poser un pion "
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (445, 55))
    if player == 1:
        string = "blanc"
    else:
        string = "noir"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (480, 75))

# Detecte si le joueur a clique sur une zone vide
def detectCollision(liste, surface, pos, player):
    for index in range(0, 4):
        # Cordonnee x et y du quadrant selectionne
        x,y = q[index][0]

        # index du quadrant selectionne
        a,b = q[index][1]
        size = len(liste)/2
        # Cordonnees du cursor
        posx, posy = pos
        if (posx > x and posx < (x+150)) and (posy > y and posy < (y+150)):
            for i in range(a, a+size):
                for j in range(b, b+size):
                    i1, j1 = i%3, j%3
                    if (posx >= x+30+j1*45 and posx <=  x+30+j1*45+15 ) and \
                            (posy >= y+30+i1*45 and posy <=  y+30+i1*45+15 ) and \
                                    liste[i][j]==0:
                        liste[i][j]=player
                        rafraichirQuardrant([[liste[h][k] for k in range(b, b+size)] for h in range(a, a+size)],
                                            surface, x, y)
                        tournerCadran(liste, surface)
                        return True
    return False

# Tourner un des quadrants
def tournerCadran(liste, surface):
    pygame.draw.rect(surface, (0, 0, 0), (420, 50, 150, 50), 0)
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)

    pygame.display.flip()
    string = "Faire tourner"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (445, 55))

    string = "un cadran"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (460, 75))

    for key in arrows:
        for path, pos in arrows[key]:
            pygame.draw.rect(surface, (0, 0, 0), (pos[0], pos[1], 20, 20), 0)
            image = pygame.image.load(os.path.join("modules/images/"+path))
            surface.blit(image, pos)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            return checkTurnCadran(liste, surface, pygame.mouse.get_pos())
    return False

# Effectuer la rotation du quadrant
def checkTurnCadran(liste, surface, evt):
    ex,ey = evt
    for key in arrows:
        for i in range(0, len(arrows[key])):
            path, pos = arrows[key][i]
            x,y = pos
            # Detecte le click sur fleche
            if (ex >= x and ex <=  x+30 ) and (ey >= y and ey <=  y+30 ):

                # index du quadrant selectionne
                a,b = q[key-1][1]
                size = len(liste)/2

                # cordonnees sur le plateau du quadrant selectionne
                r,t = q[key-1][0]

                # Effectuer la rotation du quadrant
                rotate(len(liste), liste, key, i)

                # Rafraichir le quadrant selectionne
                rafraichirQuardrant([[liste[h][k] for k in range(b, b+size)] for h in range(a, a+size)], surface, r,t)

                return True
    return False

# Efface les fleches de rotation autour des quadrants
def eraseArrows(surface):
    image = pygame.image.load(os.path.join("modules/images/tourner_cadran.png"))
    imagerect = image.get_rect()

    imagerect.x = 420
    imagerect.y = 50

    pygame.draw.rect(surface, (0, 0, 0), imagerect, 0)
    pygame.display.flip()

    for key in arrows:
        for path, pos in arrows[key]:
            pygame.draw.rect(surface, (0, 0, 0), (pos[0], pos[1], 20, 20), 0)
            image = pygame.image.load(os.path.join("modules/images/"+path))

            rect = image.get_rect()
            rect.x, rect.y = pos

            pygame.draw.rect(surface, (0, 0, 0), rect, 0)
            pygame.display.flip()

# Affiche les options Rejouer et Quitter
def dessinerRejouer(surface, state):
    if state:
        pygame.draw.rect(surface, (255, 255, 255), (420, 300, 150, 30), 2)
        string = "Rejouer"
        label = myfont.render(string, 1, (255,255,0))
        surface.blit(label, (470, 305))

        pygame.draw.rect(surface, (255, 255, 255), (420, 340, 150, 30), 2)
        string = "Quitter"
        label = myfont.render(string, 1, (255,255,0))
        surface.blit(label, (470, 345))
        pygame.display.flip()
    else:
        pygame.draw.rect(surface, (0, 0, 0), (420, 300, 300, 300), 0)


# Afficher le gagnant de la partie
def gagnant(surface, player):
    pygame.draw.rect(surface, (0, 0, 0), (420, 50, 150, 50), 0)
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)

    pygame.display.flip()

    if player == 1:
        string = "Les blancs"
    else:
        string = "Les noirs"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (445, 55))

    string = "Gagnent! "
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (480, 75))

# Declarer un match null
def matchNull(surface):
    pygame.draw.rect(surface, (0, 0, 0), (420, 50, 150, 50), 0)
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)
    pygame.display.flip()
    string = "Match null"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (465, 60))

# Lance la partie
def play():

    board = initBoard(6)
    size = width, height = 620, 440
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pentago Game')
    clock = pygame.time.Clock()
    screen.fill(black)

    player = 1
    canTurn = False
    ended = False
    winner = False
    dd = False
    dessinerRejouer(screen, False)
    rejouerScreen = False

    dessinerPlateau(board, screen)
    dessinerPlayer( screen, player)

    pygame.display.flip()

    while 1:
        clock.tick(10)
        if ended:
            # La partie est terminee

            if not rejouerScreen:
                # L'option n'est pas encore affichee
                dessinerRejouer(screen, ended)
                rejouerScreen = True

            # Ecouter l'evenement de la souris pour rejouer ou quitter
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x,y = pos

                    if (x >= 416 and x <= 600) and (y >= 296 and y <= 330 ):
                        # Rejouer une partie
                        play()

                    if (x >= 416 and x <= 600) and (y >= 340 and y <= 370 ):
                        # Quitter le jeu
                        pygame.quit()
                        sys.exit()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if not canTurn:
                        collision = detectCollision(board, screen, pos, player)
                        if collision:
                            canTurn = True
                    else:
                        state = checkTurnCadran(board, screen, pos)
                        if state:
                            passed = True
                            if align(board, len(board), 5, player):
                                ended = True
                                winner = True

                            else:
                                for row in board:
                                    if 0 in row:
                                        passed = False
                                        break
                                ended = passed
                            # Effacer les fleches du cadran
                            eraseArrows(screen)
                            if ended and not winner:
                                matchNull(screen)
                            elif ended and winner:
                                gagnant(screen, player)
                            else:
                                # Changer de joueur
                                if player == 1:
                                    player = 2
                                else:
                                    player =1
                                # Indiquer le tour du joueur
                                dessinerPlayer(screen, player)
                                # Impossible de tourner un cadran
                                canTurn = False

            if canTurn and not dd:
                dd = True
                tournerCadran(board, screen)
        pygame.display.flip()