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
#Contador de Fichas
cont = 108
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
#SELECTOR DE FICHAS DE CADA JUGADOR--------------------------------------------------------
#E: No tiene
#S: No tiene
#D: Selecciona cada uno de los decks de los jugaores
def seleccionadorDeFichas():
    global deckP2
    global deckP1
    global deckP3
    global cont
    deckP1 = seleccionadorDeFichasAux()
    deckP2 = seleccionadorDeFichasAux()
    deckP3 = seleccionadorDeFichasAux()
    cont = cont - 18
#Selector Auxiliar
#E: Una lista de
#S: No tiene
#D: Selecciona las fichas del deck
def seleccionadorDeFichasAux():
    global fichasUsadas
    deck = []
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

    return deck
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
    #PUNTAJES
    global p1
    global p2
    global p3
    #TABLEROS
    global coloresTablero
    global signosTablero
    # Turno del primer jugador
    turno = 1
    #Selecciona los decks de los jugadores al azar
    seleccionadorDeFichas()
    game = True
    while game:
        #PRINTS DE TABLEROS
        print("Colores:")
        mostrar(coloresTablero)
        print("Signos:")
        mostrar(signosTablero)
        print("Cantidad de Fichas: ",cont)

        if turno == 1:

            #PRINTS SIN IMPORTANCIA
            print("Turno de: " ,turno)
            print(deckP1)
            #ESCOGE LA FICHA DEL DECK DEL JUGADOR. EL INDEX ES LA POSICION DE LA FICHA EN EL DECK
            index = int(input("Ficha[0,5]: "))
            ficha = deckP1[index]
            print(ficha)
            #POSICION DONDE LA QUIERE COLOCAR EN LA MATRIZ
            i = int(input("Columna: "))
            j = int(input("Fila: "))
            #VERIFICA SI LA POSICION ESTA VACIA
            if signosTablero[i][j] == 0 and coloresTablero[i][j] == 0:
                #Agregar validaciones
                #PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP1.pop(index)
                turno = 2


        elif turno == 2:
            # PRINTS SIN IMPORTANCIA
            print("Turno de: ", turno)
            print(deckP2)
            # ESCOGE LA FICHA DEL DECK DEL JUGADOR. EL INDEX ES LA POSICION DE LA FICHA EN EL DECK
            index = int(input("Ficha[0,5]: "))
            ficha = deckP2[index]
            print(ficha)
            # POSICION DONDE LA QUIERE COLOCAR EN LA MATRIZ
            i = int(input("Columna: "))
            j = int(input("Fila: "))
            # VERIFICA SI LA POSICION ESTA VACIA
            if signosTablero[i][j] == 0 and coloresTablero[i][j] == 0:
                # Agregar validaciones
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP2.pop(index)
                turno = 3


        elif turno == 3:
            # PRINTS SIN IMPORTANCIA
            print("Turno de: ", turno)
            print(deckP3)
            # ESCOGE LA FICHA DEL DECK DEL JUGADOR. EL INDEX ES LA POSICION DE LA FICHA EN EL DECK
            index = int(input("Ficha[0,5]: "))
            ficha = deckP3[index]
            print(ficha)
            # POSICION DONDE LA QUIERE COLOCAR EN LA MATRIZ
            i = int(input("Columna: "))
            j = int(input("Fila: "))
            # VERIFICA SI LA POSICION ESTA VACIA
            if signosTablero[i][j] == 0 and coloresTablero[i][j] == 0:
                # Agregar validaciones
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                turno = 1
                #ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP3.pop(index)
#VALIDACIONES DE LAS JUGADAS
#E: Turno (INT), i (fila de la jugada), j (columna de la jugada)
#S:
def jugadas(turno,i,j):
    puntos = 0

#PRINT DEL TABLERO
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






juego()





