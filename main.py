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

#Contador de Fichas
cont = 108
#TABLERO COLORES
# TABLERO COLORES
coloresTablero = [[8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8]]
# TABLERO SIGNOS
signosTablero = [[8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8]]

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
    print(deckP1)
    cont = cont - 18

#Selector Auxiliar
#E: Una lista de
#S: No tiene
#D: Selecciona las fichas del deck
def seleccionadorDeFichasAux():
    global fichasUsadas
    # Contador que crea el deck del player (6)
    deck = []
    #Contador que crea el deck del player (6)
    contador = 0
    # Loop hasta completar 6 fichas
    while contador != 6:
        # Randoms
        #SIGNO
        i = random.randint(0, 5)
        #COLOR
        j = random.randint(0, 5)
        # Verifica si la ficha ya fue utilizada, si no la agrega al deck
        if fichas[i][j] != 0 and fichaFinder([j, i]) != 3:
            deck.append([j, i])
            fichasUsadas.append([j, i])
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
#AGREGA FICHAS A DECK
#E:  Lista (deck)
#S:  Lista
#D: Agrega nueva cartas al deck del jugador despues del turno
def agregaNuevasFichas(deck):
    global cont
    while len(deck) != 6:
        # Randoms
        i = random.randint(0, 5)
        j = random.randint(0, 5)
        # Verifica si la ficha ya fue utilizada, si no la agrega al deck
        if fichas[j][i] != 0 and fichaFinder([j, i]) != 3:
            deck.append([j, i]) #Agrega al deck
            fichasUsadas.append([j, i]) #Agrega las fichas seleccionadas a la lista de fichas usadas
            cont = cont - 1
    return deck

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
    #Decks
    global deckP2
    global deckP1
    global deckP3
    game = True
    # Turno del primer jugador
    turno = 1
    # Asina fichas
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

            #VERIFICA SI EL TABLERO ESTA VACAIO
            if isBoardEmpty(coloresTablero) and isBoardEmpty(signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                #ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP1.pop(index)

            #VALIDACIONES DE LA JUGADA
            elif verificarJugadaValidaColor(ficha,[i,j],coloresTablero,signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP1.pop(index)

            #PREGUNTA SI YA QUIERE ACABAR EL TURNO
            print(deckP1)
            finish = int(input("Desea terminar turno(0,1): "))
            if  finish == 1:
                deckP1 = agregaNuevasFichas(deckP1) #AGREGA FICHAS AL DECK
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

            # VERIFICA SI EL TABLERO ESTA VACAIO
            if isBoardEmpty(coloresTablero) and isBoardEmpty(signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP2.pop(index)

            # VALIDACIONES DE LA JUGADA
            elif verificarJugadaValidaColor(ficha, [i, j], coloresTablero, signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP2.pop(index)

            # PREGUNTA SI YA QUIERE ACABAR EL TURNO
            print(deckP2)
            #PREGUNTA SI YA TERMINO
            finish = int(input("Desea terminar turno(0,1): "))
            if finish == 1:
                deckP2 = agregaNuevasFichas(deckP2)  # AGREGA FICHAS AL DECK
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

            # VERIFICA SI EL TABLERO ESTA VACAIO
            if isBoardEmpty(coloresTablero) and isBoardEmpty(signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[1]
                signosTablero[i][j] = ficha[0]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP3.pop(index)

            # VALIDACIONES DE LA JUGADA
            elif verificarJugadaValidaColor(ficha, [i, j], coloresTablero, signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[0]
                signosTablero[i][j] = ficha[1]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP3.pop(index)

            # PREGUNTA SI YA QUIERE ACABAR EL TURNO
            print(deckP3)
            finish = int(input("Desea terminar turno(0,1): "))
            if finish == 1:
                deckP3 = agregaNuevasFichas(deckP3)  # AGREGA FICHAS AL DECK
                turno = 1
        #VERIFICA QUE YA NO HAYAN FICHAS DISPONIBLES
        if deckP1 == deckP2 == deckP3 == []:
            break

#E: Una matriz
#S: Un booleano
#D: Verifica si el tablero esta vacio
def isBoardEmpty(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 0:
                return False
    return True

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

#E: Dos matrices dos listas
#S: Booleano
#D: Verifica la fichas por color
def verificarJugadaValidaColor(ficha, posicion, matrizColores, matrizSignos):

    i = posicion[0]
    j = posicion[1]
    aux1 = i
    aux2 = j

    # Comparar en todas direcciones si el color es el mismo
    # Cada if equivale a un direccion

    # Comparaciones segun color igual
    if matrizColores[i + 1][j] != 8:  # Comparacion hacia abajo
        aux1 += 1
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar color
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:  # Comparar simbolo
                return False

            else:
                aux1 += 1
        aux1 = i

    if matrizColores[i - 1][j] != 8:  # Comparacion hacia arriba

        aux1 -= 1
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar arriba de la pos
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:
                return False

            else:
                aux1 -= 1
        aux1 = i

    if matrizColores[i][j + 1] != 8:  # Comparacion hacia la derecha
        aux2 += 1
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar derecha de la pos
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:
                return False

            else:
                aux2 += 1
        aux2 = j

    if matrizColores[i][j - 1] != 8:  # Comparacion hacia izquierda
        aux2 -= 1
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar izquierda de la pos
                return False

            if matrizSignos[aux1][aux2] == ficha[0]:
                return False

            else:
                aux2 -= 1

        aux2 = j

    # Si llega hasta aqui significa que es valida la jugada
    return True




juego()




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
print()
#print(buscarPosicionesValidas(signosTablero))
#print(verificarJugadaValidaColor([4, 2], [1, 2], coloresTablero, signosTablero))
