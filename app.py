from modules.pentgoGUI import play

# b = initBoard(6)
bo = [
    [2,0,1,2,1,1,0,0],
    [0,1,0,2,2,0,0,1],
    [2,0,0,2,1,0,2,0],
    [2,2,1,0,1,0,1,2],
    [1,1,2,2,1,0,0,2],
    [2,1,2,2,2,1,2,1],
    [0,1,0,2,2,0,2,1],
    [0,0,2,0,1,1,1,2]
]

al = [
    [2,2,1,2,1,0,0,0],
    [1,0,0,1,2,0,1,0],
    [0,2,0,2,2,2,0,2],
    [1,0,0,0,2,2,0,1],
    [0,1,1,0,0,1,2,2],
    [2,1,2,1,1,0,2,2],
    [0,1,0,0,2,0,1,0],
    [0,1,2,0,1,0,1,2]
]

g = [
    [2,2,1,2,1,1],
    [1,0,0,1,2,1],
    [1,2,2,2,2,2],
    [1,2,2,1,2,2],
    [1,1,1,1,1,1],
    [2,1,2,1,1,1],
]

# g = [
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
b = [
    [1,0,0,2],
    [2,1,2,1],
    [2,0,2,1],
    [1,1,1,2]
]
# display( bo )
# display(al)
# print align(al, 8, 4, 1)
# display(rotate(8,bo, 3, True))
# display(clockWise(bo, 8))
# display(reverseClockWise(b, 4))
# kep = [g[e][0:3] for e in range(0, 3)]
# for e in range(0, 3):
#     print g[e][0:3]
# print kep

# pygame.init()
# size = width, height = 620, 440
# black = 0, 0, 0
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption('Pentago Game')
# clock = pygame.time.Clock()
# player = 1
# screen.fill(black)
# dessinerPlateau(g, screen)
# dessinerPlayer( screen, player)
# canTurn = False
# ended = False
# dd = False
# dessinerRejouer(screen, False)
# rejouerScreen = False
# pygame.display.flip()
# while 1:
#     clock.tick(10)
#
#     if ended:
#         if not rejouerScreen:
#             matchNull(screen)
#             dessinerRejouer(screen, ended)
#             rejouerScreen = True
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: sys.exit()
#             if event.type == pygame.MOUSEBUTTONUP:
#                 pos = pygame.mouse.get_pos()
#                 x,y = pos
#                 if (x >= 416 and x <= 600) and (y >= 296 and y <= 330 ):
#                     play()
#                 if (x >= 416 and x <= 600) and (y >= 340 and y <= 370 ):
#                     pygame.quit()
#                     sys.exit()
#     else:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: sys.exit()
#             if event.type == pygame.MOUSEBUTTONUP:
#                 pos = pygame.mouse.get_pos()
#                 if not canTurn:
#                     collision = detectCollision(g, screen, pos, player)
#                     if collision:
#                         canTurn = True
#                         display(g)
#                 else:
#                     state = checkTurnCadran(g, screen, pos)
#                     if state:
#                         passed = True
#                         if align(g, len(g)/2, 5, player):
#                             gagnant(screen, player)
#                         else:
#                             for row in g:
#                                 if 0 in row:
#                                     passed = False
#                                     break
#                             ended = passed
#                         # Changer de joueur
#                         if player == 1:
#                             player = 2
#                         else:
#                             player =1
#
#                         # Effacer les fleches du cadran
#                         eraseArrows(screen)
#
#                         # Indiquer le tour du joueur
#                         dessinerPlayer(screen, player)
#                         # Impossible de tourner un cadran
#                         canTurn = False
#         if canTurn and not dd:
#             dd = True
#             tournerCadran(g, screen)
#
#     pygame.display.flip()

play()