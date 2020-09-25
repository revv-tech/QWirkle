# Proyecto QWirkle

# imports
import pygame
import random
import math
from pygame.locals import *

pygame.init()
# PUNTAJE
p1 = 0
p2 = 0
p3 = 0

# TABLERO COLORES
coloresTablero = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]
# TABLERO SIGNOS
signosTablero = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

# VARIABLES PARA GENERADOR DE FICHAS ----------------------------------------------------
# TABLERO DE FICHAS
# FILAS
# 0 = AZUL -> 1 = CELESTE -> 2 = VERDE -> 3 = AMARILLO -> 4 = NARANJA -> 5 = ROJO
# COLUMNAS
# 0 = CRUZ -> 1 = ASTERIZCO -> 2 = CUADRADO -> 3 = ROMBO -> 4 = EQUIS -> 5 = CIRCULO
fichas = [[1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6],
          [1, 2, 3, 4, 5, 6]]
# FICHAS YA USADAS O EN POSECION DE LOS JUGADORES
fichasUsadas = []
# VARIABLES GLOBALES DE LOS DECKS DE CADA JUGADOR
deckP1 = []
deckP2 = []
deckP3 = []
# ---------------------------------------------------------------------------------------
# VENTANA GUI
ventana = pygame.display.set_mode((720, 720))


#
# SELECTOR DE FICHAS DE CADA JUGADOR--------------------------------------------------------
# E: No tiene
# S: No tiene
# D: Selecciona cada uno de los decks de los jugaores
def seleccionadorDeFichas():
    global deckP2
    global deckP1
    global deckP3
    deckP1 = seleccionadorDeFichasAux()
    deckP2 = seleccionadorDeFichasAux()
    deckP3 = seleccionadorDeFichasAux()
    print(deckP1)


# Selector Auxiliar
# E: Una lista de
# S: No tiene
# D: Selecciona las fichas del deck
def seleccionadorDeFichasAux():
    deck = []
    global fichasUsadas
    # Contador que crea el deck del player (6)
    contador = 0
    # Loop hasta completar 6 fichas
    while contador != 6:
        # Randoms
        i = random.randint(0, 5)
        j = random.randint(0, 5)
        # Verifica si la ficha ya fue utilizada, si no la agrega al deck
        if fichas[i][j] != 0 and fichaFinder([i, j]) != 3:
            deck.append([i, j])
            fichasUsadas.append([i, j])
            contador = contador + 1


# AUXILIAR PARA ENCONTAR SI UNA FICHA YA FUE USADA
# E: Una lista
# S: Un int
# D: Verifica la cantidad de veces que se ha usado una ficha
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


# ---------------------------------------------------------------------------------------

# JUEGO
# E: No tiene
# S: No tiene
# D: Proceso del juego

def juego():
    # Selecciona los decks de los jugadores al azar
    seleccionadorDeFichas()
    global p1
    global p2
    global p3
    global coloresTablero
    global signosTablero
    game = True
    # Turno del primer jugador
    turno = 1
    # Asina fichas
    seleccionadorDeFichas()
    while game:
        print("Colores:")
        mostrar(coloresTablero)
        print("Signos:")
        mostrar(signosTablero)
        if turno == 1:
            print("Turno de: ", turno)
            print(deckP1)
            ficha = int(input("Ficha: "))
            i = int(input("Columna: "))
            j = int(input("Fila: "))
            if signosTablero[i][j] == 0 and coloresTablero == 0:
                # Agregar validaciones
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


def buscarSoluciones(matrizColores, matrizSignos, deck, posicion, soluciones=[]):
    print("Hola mundo")


# E: Una matriz
# S: Una lista de posiciones
# D: Recibe la matriz del tablero y retorna
#    todas las posiciones donde se puede colocar una ficha
def buscarPosicionesValidas(matrizSignos):
    posiciones = []

    for i in range(0, len(matrizSignos) - 1):

        for j in range(0, len(matrizSignos[0]) - 1):

            if matrizSignos[i][j] == 0:  # Verifica que no haya una ficha ahi

                # Pregunta por las posiciones adyacentes a la ficha para saber si hay fichas en las cuales apoyarse
                if matrizSignos[i - 1][j] != 0 or matrizSignos[i + 1][j] != 0 or matrizSignos[i][j - 1] != 0 or \
                        matrizSignos[i][j + 1] != 0:
                    posiciones += [[i, j]]

    return posiciones


def verificarJugadaValidaColor(ficha, posicion, matrizColores, matrizSignos):

    i = posicion[0]
    j = posicion[1]
    aux1 = i
    aux2 = j

    # Comparar en todas direcciones si el color es el mismo
    # Cada if equivale a un direccion

    # Comparaciones segun color igual
    if matrizColores[i + 1][j] != 0:  # Comparacion hacia abajo
        aux1 += 1
        while matrizColores[aux1][aux2] != 0:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar color
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:  # Comparar simbolo
                return False

            else:
                aux1 += 1
        aux1 = i

    if matrizColores[i - 1][j] != 0:  # Comparacion hacia arriba
        aux1 -= 1
        while matrizColores[aux1][aux2] != 0:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar arriba de la pos
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:
                return False

            else:
                aux1 -= 1
        aux1 = i

    if matrizColores[i][j + 1] != 0:  # Comparacion hacia la derecha
        aux2 += 1
        while matrizColores[aux1][aux2] != 0:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar derecha de la pos
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:
                return False

            else:
                aux2 += 1
        aux2 = j

    if matrizColores[i][j - 1] != 0:  # Comparacion hacia izquierda
        aux2 -= 1
        while matrizColores[aux1][aux2] != 0:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar izquierda de la pos
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:
                return False

            else:
                aux2 -= 1
        aux2 = j

    # Si llega hasta aqui significa que es valida la jugada
    return True


# juego()
# seleccionadorDeFichas()


# TABLERO COLORES
coloresTablero = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]
# TABLERO SIGNOS
signosTablero = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 2, 3, 0, 0],
                 [0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 3, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

print(buscarPosicionesValidas(signosTablero))
print(verificarJugadaValidaColor([4, 2], [1, 2], coloresTablero, signosTablero))
