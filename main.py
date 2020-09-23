#Proyecto QWirkle

#imports
import pygame
import random
import math
from pygame.locals import *

pygame.init()

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
#1 = CRUZ -> 2 = ASTERIZCO -> 3 = CUADRADO -> 4 = ROMBO -> 5 = EQUIS -> 6 = CIRCULO
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
    deckP1 = seleccionadorDeFichasAux(deckP1)
    deckP2 = seleccionadorDeFichasAux(deckP2)
    deckP3 = seleccionadorDeFichasAux(deckP3)
    print(fichasUsadas)
#Selector Auxiliar
#E: Una lista de
#S: No tiene
#D: Selecciona las fichas del deck
def seleccionadorDeFichasAux(deck):
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
    global coloresTablero
    global signosTablero
    #Selecciona los decks de los jugadores al azar
    seleccionadorDeFichas()
    game = True
    #Turno del primer jugador
    turno = 1







