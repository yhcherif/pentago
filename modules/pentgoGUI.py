import pygame, sys, os
from bases import *
from rotations import *
from alignements import *
RED =   (255,   0,   0)
COLORS = {0 : (160, 160, 160),
1 : (255, 255, 255),
2 : (0,0,0)}
q= [
    [(50, 50), (0,0)],
    [(50, 210), (3, 0)],
    [(210, 210), (3, 3)],
    [(210, 50), (0,3)]
]

arrows = {
    1: [
        ["arrow_right_top.png", (96, 10)], ["arrow_left_left.png",(10, 96)]
    ],
    2: [
        ["arrow_right_left.png", (10, 260)],[ "arrow_left_bottom.png", (96, 360)]
    ],
    3: [
        ["arrow_left_right.png", (370, 260)],[ "arrow_right_bottom.png", (260, 361)]
    ],
    4: [
        ["arrow_left_top.png", (260, 10)],[ "arrow_right_right.png", (370, 96)]
    ]

}
pygame.init()
pygame.font.init()
myfont = pygame.font.Font("modules/arial.ttf", 17)

def dessinerPlateau(liste, surface):
    rafraichirQuardrant([liste[e][0:3] for e in range(0, 3)], surface, 50, 50)
    rafraichirQuardrant([liste[e][0:3] for e in range(3, 6)], surface, 50, 210)
    rafraichirQuardrant([liste[e][3:6] for e in range(0, 3)], surface, 210, 210)
    rafraichirQuardrant([liste[e][3:6] for e in range(3, 6)], surface, 210, 50)

def rafraichirQuardrant(liste, surface, x, y):
    pygame.draw.rect(surface, RED, (x, y, 150, 150), 0 )
    x += 30
    y +=30
    for i in range(0, len(liste)):
        for j in range(0, len(liste)):
            pygame.draw.circle(surface, COLORS[liste[i][j]] , [x+j*45, y+i*45], 15)


def poserUnPion(liste, surface, player):
    pass

def dessinerPlayer(surface, player):
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

def detectCollision(liste, surface, pos, player):
    print pos
    for index in range(0, 4):
        x,y = q[index][0]
        a,b = q[index][1]
        size = len(liste)/2
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


def tournerCadran(liste, surface):
    pygame.draw.rect(surface, (0, 0, 0), (420, 50, 150, 50), 0)
    # pygame.display.flip()
    # image = pygame.image.load(os.path.join("modules/images/tourner_cadran.png"))
    # imagerect = image.get_rect()
    # surface.blit(image, (420, 50))
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)
    pygame.display.flip()
    #
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

def checkTurnCadran(liste, surface, evt):
    ex,ey = evt
    for key in arrows:
        for i in range(0, len(arrows[key])):
            path, pos = arrows[key][i]
            x,y = pos
            if (ex >= x and ex <=  x+30 ) and (ey >= y and ey <=  y+30 ):
                a,b = q[key-1][1]
                size = len(liste)/2
                r,t = q[key-1][0]
                print "On fait tourner le cadran : ", key, " pour la pos : ",pos
                rotate(len(liste), liste, key, i)
                # rotate(len(liste), [[liste[h][k] for k in range(b, b+size)] for h in range(a, a+size)], key, i)
                rafraichirQuardrant([[liste[h][k] for k in range(b, b+size)] for h in range(a, a+size)], surface, r,t)
                return True
                # print "Apres tourner le cadran"
                # display(liste)
    return False


def eraseArrows(surface):
    image = pygame.image.load(os.path.join("modules/images/tourner_cadran.png"))
    imagerect = image.get_rect()
    imagerect.x = 420
    imagerect.y = 50
    pygame.draw.rect(surface, (0, 0, 0), imagerect, 0)
    pygame.display.flip()
    # surface.blit(image, (420, 50))
    for key in arrows:
        for path, pos in arrows[key]:
            pygame.draw.rect(surface, (0, 0, 0), (pos[0], pos[1], 20, 20), 0)
            image = pygame.image.load(os.path.join("modules/images/"+path))
            rect = image.get_rect()
            rect.x, rect.y = pos
            pygame.draw.rect(surface, (0, 0, 0), rect, 0)
            pygame.display.flip()


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

def gagnant(surface, player):
    pygame.draw.rect(surface, (0, 0, 0), (420, 50, 150, 50), 0)
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)
    # image = pygame.image.load(os.path.join("modules/images/"+images[player][0]))
    # surface.blit(image, images[player][1])
    pygame.display.flip()
    # myfont = pygame.font.Font("modules/arial.ttf", 17)
    #
    if player == 1:
        string = "Les blancs"
    else:
        string = "Les noirs"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (445, 55))
    string = "Gagnent! "
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (480, 75))


def matchNull(surface):
    pygame.draw.rect(surface, (0, 0, 0), (420, 50, 150, 50), 0)
    pygame.draw.rect(surface, (255, 255, 255), (420, 50, 150, 50), 2)
    # image = pygame.image.load(os.path.join("modules/images/"+images[player][0]))
    # surface.blit(image, images[player][1])
    pygame.display.flip()
    # myfont = pygame.font.Font("modules/arial.ttf", 17)
    #
    string = "Match null"
    label = myfont.render(string, 1, (255,255,0))
    surface.blit(label, (465, 60))


def play():

    board = [[0 for j in range(0, 6)] for i in range(0, 6)]
    size = width, height = 620, 440
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pentago Game')
    clock = pygame.time.Clock()
    player = 1
    screen.fill(black)
    dessinerPlateau(board, screen)
    dessinerPlayer( screen, player)
    canTurn = False
    ended = False
    winner = False
    dd = False
    dessinerRejouer(screen, False)
    rejouerScreen = False
    pygame.display.flip()
    while 1:
        clock.tick(10)

        if ended:
            if not rejouerScreen:
                dessinerRejouer(screen, ended)
                rejouerScreen = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    x,y = pos
                    if (x >= 416 and x <= 600) and (y >= 296 and y <= 330 ):
                        play()
                    if (x >= 416 and x <= 600) and (y >= 340 and y <= 370 ):
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
                            display(board)
                    else:
                        state = checkTurnCadran(board, screen, pos)
                        if state:
                            passed = True
                            if align(board, len(board), 2, player):
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