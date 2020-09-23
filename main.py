#Proyecto QWirkle

#imports
import pygame
import random
import math
from pygame.locals import *

pygame.init()
#PUNTAJE
p1 = 0
p2 = 0
p3 = 0

#TABLERO COLORES
coloresTablero=[[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]
#TABLERO SIGNOS
signosTablero=[[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]

#VARIABLES PARA GENERADOR DE FICHAS ----------------------------------------------------
#TABLERO DE FICHAS
#FILAS
#0 = AZUL -> 1 = CELESTE -> 2 = VERDE -> 3 = AMARILLO -> 4 = NARANJA -> 5 = ROJO
#COLUMNAS
#0 = CRUZ -> 1 = ASTERIZCO -> 2 = CUADRADO -> 3 = ROMBO -> 4 = EQUIS -> 5 = CIRCULO
fichas = [[1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6],
            [1,2,3,4,5,6]]
#FICHAS YA USADAS O EN POSECION DE LOS JUGADORES
fichasUsadas = []
#VARIABLES GLOBALES DE LOS DECKS DE CADA JUGADOR
deckP1 = []
deckP2 = []
deckP3 = []
#---------------------------------------------------------------------------------------
#VENTANA GUI
ventana = pygame.display.set_mode((720, 720))
#
#SELECTOR DE FICHAS DE CADA JUGADOR--------------------------------------------------------
#E: No tiene
#S: No tiene
#D: Selecciona cada uno de los decks de los jugaores
def seleccionadorDeFichas():
    global deckP2
    global deckP1
    global deckP3
    deckP1 = seleccionadorDeFichasAux()
    deckP2 = seleccionadorDeFichasAux()
    deckP3 = seleccionadorDeFichasAux()
    print(deckP1)

#Selector Auxiliar
#E: Una lista de
#S: No tiene
#D: Selecciona las fichas del deck
def seleccionadorDeFichasAux():
    deck = []
    global fichasUsadas
    #Contador que crea el deck del player (6)
    contador = 0
    #Loop hasta completar 6 fichas
    while (contador != 6):
        #Randoms
        i = random.randint(0,5)
        j = random.randint(0,5)
        #Verifica si la ficha ya fue utilizada, si no la agrega al deck
        if fichas[i][j] != 0 and fichaFinder([i,j]) != 3:
            deck.append([i,j])
            fichasUsadas.append([i,j])
            contador = contador + 1


#AUXILIAR PARA ENCONTAR SI UNA FICHA YA FUE USADA
#E: Una lista
#S: Un int
#D: Verifica la cantidad de veces que se ha usado una ficha
def fichaFinder(lista):
    i = 0
    cont = 0
    if fichasUsadas == []:
        return 0
    while i < len(fichasUsadas):
        if lista == fichasUsadas[i]:
            cont += 1
        i += 1
    return cont
#---------------------------------------------------------------------------------------

#JUEGO
#E: No tiene
#S: No tiene
#D: Proceso del juego

def juego():
    # Selecciona los decks de los jugadores al azar
    seleccionadorDeFichas()
    global p1
    global p2
    global p3
    global coloresTablero
    global signosTablero
    game = True
    #Turno del primer jugador
    turno = 1
    #Asina fichas
    seleccionadorDeFichas()
    while game:
        print("Colores:")
        mostrar(coloresTablero)
        print("Signos:")
        mostrar(signosTablero)
        if turno == 1:
            print("Turno de: " ,turno)
            print(deckP1)
            ficha = int(input("Ficha: "))
            i = int(input("Columna: "))
            j = int(input("Fila: "))
            if signosTablero[i][j] == 0 and coloresTablero == 0:
                #Agregar validaciones
                coloresTablero[i][j] = ficha[j]
                signosTablero[i][j] = ficha[i]
            else:
                turno = 1

        elif turno == 2:
            print(deckP2)
            ficha = int(input("Ficha [0,5]: "))
            i = int(input("Columna: "))
            j = int(input("Fila: "))

            if signosTablero[i][j] == 0 and coloresTablero == 0:
                # Agregar validaciones
                coloresTablero[i][j] = ficha[j]
                signosTablero[i][j] = ficha[i]
            else:
                turno = 2

        elif turno == 3:
            print(deckP3)
            ficha = int(input("Ficha: "))
            i = int(input("Columna: "))
            j = int(input("Fila: "))
            if signosTablero[i][j] == 0 and coloresTablero == 0:
                # Agregar validaciones
                coloresTablero[i][j] = ficha[j]
                signosTablero[i][j] = ficha[i]
            else:
                turno = 3


# E: Una matriz
# S: No tiene
# D: Imprime el tablero

def mostrar(tablero):
    # tablero = tablero[::-1]
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=' ')
        print()
    print()

#juego()
seleccionadorDeFichas()





