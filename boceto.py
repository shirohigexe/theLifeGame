#importe de librerias
import pygame
import numpy as np
import time

#creacion de ventana
pygame.init()
#ancho y alto de la ventana
width, height = 1000, 1000

screen = pygame.display.set_mode((height, width))
#color del fondo
backgraund = 25, 25, 25

screen.fill(backgraund)

#creacion de celdas
Cx, Cy = 50, 50
#dimencion de las celdas 
dimCW = width / Cx
dimCH = height / Cy

#estado de celdas, vivas = 1 o muertas = 0
gameState = np.zeros((Cx,Cy))

#control de la ejecucion del juego
pauseExcet = False

#ejemplos

gameState[5,3]=1
gameState[5,4]=1
gameState[5,5]=1

gameState[21,21]=1
gameState[22,22]=1
gameState[22,23]=1
gameState[21,23]=1
gameState[20,23]=1

#bucle de ejecucion
while True:

    newGameState = np.copy(gameState)

    screen.fill(backgraund)
    time.sleep(0.1)

    #registramos los eventos ocurridos en el teclado
    evento = pygame.event.get()

    for event in evento:
        if event.type == pygame.QUIT:
            pygame.quit()
        #detectamos si se preciona una tecla 
        if event.type == pygame.KEYDOWN:
            pauseExcet = not pauseExcet
        


    for y in range(0,Cx):
        for x in range(0,Cy):
            if not pauseExcet:
                #calculamos el numero de vecinos cercanos
                n_neigh = gameState[(x-1)%Cx,(y-1)%Cy] + \
                        gameState[(x)%Cx,(y-1)%Cy] + \
                        gameState[(x+1)%Cx,(y-1)%Cy] + \
                        gameState[(x-1)%Cx,(y)%Cy] + \
                        gameState[(x+1)%Cx,(y)%Cy] + \
                        gameState[(x-1)%Cx,(y+1)%Cy] + \
                        gameState[(x)%Cx,(y+1)%Cy] + \
                        gameState[(x+1)%Cx,(y+1)%Cy]


                #reglas del juego
                #regla 1:una celda muerta con exactamente 3 vecinas vivas, "revive".
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y] = 1

                #regla 2:una celda viva con menos de 2 o mas de 3 vecinas vivas, "muere"
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh >3):
                    newGameState[x,y] = 0


            #creamos poligono de cada celda a dibujar
            poly = [((x)*dimCW, y*dimCH),
                    ((x+1)*dimCW, y*dimCH),
                    ((x+1)*dimCW, (y+1)*dimCH),
                    ((x)*dimCW, (y+1)*dimCH)]


            #dibujamos ña celda para cada par x e y
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen,(128,128,128),poly,1)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)

    #actualizamos el estado del juego
    gameState = np.copy(newGameState)


    #actualizacino de la ventana
    pygame.display.flip()