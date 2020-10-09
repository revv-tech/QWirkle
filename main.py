# Proyecto QWirkle

# imports
import pygame
import random
import itertools
from pygame.locals import *
pygame.init()
# PUNTAJE
p1 = 0
p2 = 0
p3 = 0
#ULTIMOS TURNOS
lastP1 = 0
lastP2 = 0
lastP3 = 0
# Contador de Fichas
cont = 108
# E: Dos ints
# S: Una Matriz
# D:Crea una matriz con la cantidad de C y F que se le pase

def generadorMatriz(filas,columnas):
    M = []
    for i in range(columnas):
        columna = [8]*filas
        M.append(columna)

    return M
# TABLERO COLORES
coloresTablero = generadorMatriz(216, 216)
# TABLERO SIGNOS
signosTablero = generadorMatriz(216, 216)
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
# PRINT DEL TABLERO
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
# SELECTOR DE FICHAS DE CADA JUGADOR--------------------------------------------------------
# E: No tiene
# S: No tiene
# D: Selecciona cada uno de los decks de los jugaores
def seleccionadorDeFichas():
    global deckP2
    global deckP1
    global deckP3
    global cont
    deckP1 = seleccionadorDeFichasAux()
    deckP2 = seleccionadorDeFichasAux()
    deckP3 = seleccionadorDeFichasAux()
    #print(deckP1)
    cont = cont - 18
# Selector Auxiliar
# E: Una lista de
# S: No tiene
# D: Selecciona las fichas del deck

def seleccionadorDeFichasAux():
    global fichasUsadas
    # Contador que crea el deck del player (6)
    deck = []
    # Contador que crea el deck del player (6)
    contador = 0
    # Loop hasta completar 6 fichas
    while contador != 6:
        # Randoms
        # SIGNO
        i = random.randint(0, 5)
        # COLOR
        j = random.randint(0, 5)
        # Verifica si la ficha ya fue utilizada, si no la agrega al deck
        if fichas[i][j] != 0 and fichaFinder([j, i]) != 3:
            deck.append([j, i])
            fichasUsadas.append([j, i])
            contador = contador + 1
    return deck


# AUXILIAR PARA ENCONTAR SI UNA FICHA YA FUE USADA
# E: Una lista
# S: Un int
# D: Verifica la cantidad de veces que se ha usado una ficha
def fichaFinder(lista):
    i = 0
    cont = 0
    if not fichasUsadas:
        return 0
    while i < len(fichasUsadas):
        if lista == fichasUsadas[i]:
            cont += 1
        i += 1
    return cont


# AGREGA FICHAS A DECK
# E:  Lista (deck)
# S:  Lista
# D: Agrega nueva cartas al deck del jugador despues del turno
def agregaNuevasFichas(deck):
    global cont
    while len(deck) != 6:
        # Randoms
        i = random.randint(0, 5)
        j = random.randint(0, 5)
        # Verifica si la ficha ya fue utilizada, si no la agrega al deck
        if fichas[j][i] != 0 and fichaFinder([j, i]) != 3:
            deck.append([j, i])  # Agrega al deck
            fichasUsadas.append([j, i])  # Agrega las fichas seleccionadas a la lista de fichas usadas
            cont = cont - 1
    return deck

# ---------------------------------------------------------------------------------------
# JUEGO
# E: No tiene
# S: No tiene
# D: Proceso del juego
def juego():
    # PUNTAJES
    global p1
    global p2
    global p3
    # TABLEROS
    global coloresTablero
    global signosTablero
    # Decks
    global deckP2
    global deckP1
    global deckP3
    # Asina fichas
    # Turno del primer jugador
    turno = 1
    # Selecciona los decks de los jugadores al azar
    seleccionadorDeFichas()
    game = True
    # Almacena las jugadas
    # [[POSICION],[FICHA]]
    listaJugadas = []
    listaPosicionesPlays = []
    while game:

        if turno == 1:
            # PRINTS DE TABLEROS
            print("Signos:")
            mostrar(signosTablero)
            print("Colores:")
            mostrar(coloresTablero)
            print("Cantidad de Fichas: ", cont)
            # PRINTS SIN IMPORTANCIA
            # print("Permutaciones: ",list(itertools.permutations(deckP1)))
            print("Turno de: ", turno)
            print(deckP1)
            # ESCOGE LA FICHA DEL DECK DEL JUGADOR. EL INDEX ES LA POSICION DE LA FICHA EN EL DECK
            index = int(input("Ficha[0,5][Signos,Colores]: "))
            ficha = deckP1[index]
            print(ficha)
            # POSICION DONDE LA QUIERE COLOCAR EN LA MATRIZ
            i = int(input("Fila: "))
            j = int(input("Columna: "))
            # VALIDACIONES DE LA JUGADA
            if verificarJugadaValida(ficha,[i,j],coloresTablero,signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[1]
                signosTablero[i][j] = ficha[0]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP1.pop(index)
                # AGREGA LA JUGADA A LA LISTA DE JUGADAS
                listaJugadas.append([[i, j]]+[ficha])
                listaPosicionesPlays.append([i, j])

            # PREGUNTA SI YA QUIERE ACABAR EL TURNO
            print(deckP1)
            print("JUGADAS[POSICION,FICHA]: ", listaJugadas)
            print("Posiciones: ", listaPosicionesPlays)
            finish = int(input("Desea terminar turno(0,1): "))
            if  finish == 1:
                play = puntuacion(listaJugadas, listaPosicionesPlays)
                print("Tu turno fue de  +", play)
                p1 = p1 + play
                print("P#", turno, " llevas ", p1, " puntos!")
                deckP1 = agregaNuevasFichas(deckP1)  # AGREGA FICHAS AL DECK
                turno = 2
                listaJugadas = []
                listaPosicionesPlays = []

        elif turno == 2:
            # PRINTS DE TABLEROS
            print("Signos:")
            mostrar(signosTablero)
            print("Colores:")
            mostrar(coloresTablero)
            print("Cantidad de Fichas: ", cont)
            # PRINTS SIN IMPORTANCIA
            print("Turno de: ", turno)
            print(deckP2)
            # ESCOGE LA FICHA DEL DECK DEL JUGADOR. EL INDEX ES LA POSICION DE LA FICHA EN EL DECK
            index = int(input("Ficha[0,5][Signos,Colores]: "))
            ficha = deckP2[index]
            print(ficha)
            # POSICION DONDE LA QUIERE COLOCAR EN LA MATRIZ
            i = int(input("Fila: "))
            j = int(input("Columna: "))

            # VALIDACIONES DE LA JUGADA
            if verificarJugadaValida(ficha, [i, j], coloresTablero, signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[1]
                signosTablero[i][j] = ficha[0]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP2.pop(index)
                # AGREGA LA JUGADA A LA LISTA DE JUGADAS
                listaJugadas.append([[i, j]] + [ficha])
                listaPosicionesPlays.append([i, j])

            # PREGUNTA SI YA QUIERE ACABAR EL TURNO
            print(deckP2)
            print("JUGADAS[POSICION,FICHA]: ", listaJugadas)
            print("Posiciones: ", listaPosicionesPlays)
            finish = int(input("Desea terminar turno(0,1): "))
            if finish == 1:
                play = puntuacion(listaJugadas, listaPosicionesPlays)
                print("Tu turno fue de  +", play)
                p2 = p2 + play
                print("P#", turno, " llevas ", p2, " puntos!")
                deckP2 = agregaNuevasFichas(deckP2)  # AGREGA FICHAS AL DECK
                turno = 3
                listaJugadas = []
                listaPosicionesPlays = []

        elif turno == 3:
            # PRINTS DE TABLEROS
            print("Signos:")
            mostrar(signosTablero)
            print("Colores:")
            mostrar(coloresTablero)
            print("Cantidad de Fichas: ", cont)
            # PRINTS SIN IMPORTANCIA
            print("Turno de: ", turno)
            print(deckP3)
            # ESCOGE LA FICHA DEL DECK DEL JUGADOR. EL INDEX ES LA POSICION DE LA FICHA EN EL DECK
            index = int(input("Ficha[0,5][Signos,Colores]: "))
            ficha = deckP3[index]
            print(ficha)
            # POSICION DONDE LA QUIERE COLOCAR EN LA MATRIZ
            i = int(input("Fila: "))
            j = int(input("Columna: "))

            # VALIDACIONES DE LA JUGADA
            if verificarJugadaValida(ficha, [i, j], coloresTablero, signosTablero):
                # PONE LA FICHA EN LOS TABLEROS
                coloresTablero[i][j] = ficha[1]
                signosTablero[i][j] = ficha[0]
                # ELIMINA LA FICHA DEL DECK DEL JUGADOR
                deckP3.pop(index)
                # AGREGA LA JUGADA A LA LISTA DE JUGADAS
                listaJugadas.append([[i, j]] + [ficha])
                listaPosicionesPlays.append([i, j])

            # PREGUNTA SI YA QUIERE ACABAR EL TURNO
            print(deckP3)
            print("JUGADAS[POSICION,FICHA]: ", listaJugadas)
            print("Posiciones: ", listaPosicionesPlays)
            finish = int(input("Desea terminar turno(0,1): "))
            if finish == 1:
                play = puntuacion(listaJugadas, listaPosicionesPlays)
                print("Tu turno fue de  +", play)
                p3 = p3 + play
                print("P#", turno, " llevas ", p3, " puntos!")
                deckP3 = agregaNuevasFichas(deckP3)  # AGREGA FICHAS AL DECK
                listaJugadas = []
                listaPosicionesPlays = []
                turno = 1

        # VERIFICA QUE YA NO HAYAN FICHAS DISPONIBLES
        if deckP1 == deckP2 == deckP3 == []:
            break


# E: Una matriz
# S: Un booleano
# D: Verifica si el tablero esta vacio
def isBoardEmpty(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 8:
                return False
    return True


# Puntuacion
# E: Una listas de listas
# S: Un numero
# D: Revisa la jugada de acuerdo a las fichas y a la posicion en la que la puso.
def puntuacion(jugada,jugadasPos):
    puntos = 0
    # JUGADAS[POSICION,FICHA]
    if not jugada:
        return 0
    if len(jugada) == 1:
        return puntuacionAux(jugada[0],jugadasPos)
    while jugada:
        puntos = puntos + puntuacionAux(jugada[0],jugadasPos)
        jugada = jugada[1:]
    #print(puntos)
    return puntos

# Check Puntuacion
# E: Una lista con la ficha y la posicion y la lista de fichas puestas en el turno
# S: La cantidad de numeros
# D: Suma los puntos de cada jugada
def puntuacionAux(jugada,jugadaPos = []):
    # CAMBIE FICHA [POS,FICHA]
    #print("Puntuacion Aux: ", jugada)
    i = jugada[1][0] #FILAS
    j = jugada[1][1] #COLUMNAS
    ficha = jugada[0] #FICHA
    puntos = 1
    #AXUILIARES
    aux1 = i
    aux2 = j

    # COMPARACION COLUMNA
    #print("DER: ", signosTablero[i][j + 1], coloresTablero[i][j + 1],ficha)
    if coloresTablero[i][j + 1] == ficha[0] or signosTablero[i][j + 1] == ficha[1]:
        #print("#1: Columna Derecha")
        aux2 += 1
        while coloresTablero[i][aux2] == ficha[1] or signosTablero[i][aux2] == ficha[0]:
            if not ([i,aux2] in jugadaPos):
                puntos += 1
            aux2 += 1
        aux2 = j
    #print("IZQ: ", signosTablero[i][j - 1], coloresTablero[i][j - 1],ficha)
    if coloresTablero[i][j - 1] == ficha[1] or signosTablero[i][j - 1] == ficha[0]:
        #print("#2: Columna Izquierda")
        aux2 -= 1
        while coloresTablero[i][aux2] == ficha[1] or signosTablero[i][aux2] == ficha[0]:
            if not ([i, aux2] in jugadaPos):
                puntos += 1
            aux2 -= 1

    # COMPARA FILAS
    #print("ARRIBA: ",signosTablero[i + 1][j],coloresTablero[i + 1][j],ficha)
    if coloresTablero[i + 1][j] == ficha[1] or signosTablero[i + 1][j] == ficha[0]:
        #print("#3: Fila Arriba ")
        aux1 += 1
        while coloresTablero[aux1][j] == ficha[1] or signosTablero[aux1][j] == ficha[0]:
            if not ([aux1, j] in jugadaPos):
                puntos += 1
            aux1 += 1
        aux1 = i

    #print("ABAJO: ", signosTablero[i - 1][j], coloresTablero[i - 1][j],ficha)
    if coloresTablero[i - 1][j] == ficha[1] or signosTablero[i - 1][j] == ficha[0]:
        #print("#4: Fila Abajo")
        aux1 -= 1
        while coloresTablero[aux1][j] == ficha[1] or signosTablero[aux1][j] == ficha[0]:
            if not ([aux1, j] in jugadaPos):
                puntos += 1
            aux1 -= 1
    return puntos


# E: matriz del tablero
# S: Booleano, retorna True si el tablero necesita extenderse hacia arriba
# D: Revisa la tercera fila del tablero (arriba hacia abajo) si encuentra
#    una ficha entonces retorna True, en otro caso retorna False
def revisarTableroArriba(matrizColores):

    for j in range(0, len(matrizColores[2])):  # Revisa la fila 3

        if matrizColores[6][j] != 8:
            return True

    return False


# E: matriz del tablero
# S: Booleano, retorna True si el tablero necesita extenderse hacia abajo
# D: Revisa la tercera fila del tablero (abajo hacia arriba) si encuentra
#    una ficha entonces retorna True, en otro caso retorna False
def revisarTableroAbajo(matrizColores):
    i = len(matrizColores)-6  # Revisa 3 filas arriba de la fila final

    for j in range(0, len(matrizColores[i])):  # Revisa la fila 3

        if matrizColores[i][j] != 8:
            return True

    return False


# E: matriz del tablero
# S: Booleano, retorna True si el tablero necesita extenderse hacia la izquierda
# D: Revisa la tercera fila del tablero (izquierda hacia derecha) si encuentra
#    una ficha entonces retorna True, en otro caso retorna False
def revisarTableroIzquierda(matrizColores):

    for j in range(0, len(matrizColores[0])):  # Revisa la columna 3

        if matrizColores[6][j] != 8:
            return True

    return False


# E: matriz del tablero
# S: Booleano, retorna True si el tablero necesita extenderse hacia la derecha
# D: Revisa la tercera fila del tablero (derecha hacia izquierda) si encuentra
#    una ficha entonces retorna True, en otro caso retorna False
def revisarTableroDerecha(matrizColores):

    j = len(matrizColores[0])-6

    for i in range(0, len(matrizColores)):  # Revisa 3 columnas a la izquierda de la columna final

        if matrizColores[i][j] != 8:
            return True

    return False


def checkExtenderTablero(matrizColores,matrizSignos):

    if revisarTableroArriba(matrizColores):  # True = necesita extenderse hacia arriba

        for i in range(0, 5):  # Le suma 6 filas

            matrizColores = [[8]*len(matrizColores[0])] + matrizColores  # Suma a la izquierda para que queden "arriba"
            matrizSignos = [[8]*len(matrizSignos[0])] + matrizSignos  # Suma a la izquierda para que queden "arriba"

    if revisarTableroAbajo(matrizColores):  # True = necesita extenderse hacia abajo

        for i in range(0, 5):  # Le suma 6 filas

            matrizColores = matrizColores + [[8] * len(matrizColores[0])]  # Suma a la derecha para que queden "abajo"
            matrizSignos = matrizSignos + [[8] * len(matrizSignos[0])]  # Suma a la derecha para que queden "abajo"

    if revisarTableroIzquierda(matrizColores):  # True = necesita extenderse hacia la izquierda

        for i in range(0, len(matrizColores)):

            matrizColores[i] = [8] * 6 + matrizColores[i]  # Suma 6 ceros a cada fila para agregar columnas
            matrizSignos[i] = [8] * 6 + matrizSignos[i]  # Suma 6 ceros a cada fila para agregar columnas

    if revisarTableroDerecha(matrizColores):  # True = necesita extenderse hacia la derecha

        for i in range(0, len(matrizColores)):

            matrizColores[i] += [8] * 6  # Suma 6 ceros a cada fila para agregar columnas
            matrizSignos[i] += [8] * 6  # Suma 6 ceros a cada fila para agregar columnas



# BACKTRACKING
# S: Una lista con el total de jugadas que son posibles en ese momento segun el deck y el tablero con
# el siguiente formato:
# [jugada[fichasPuestas[ficha, posicion]]]
def buscarSoluciones(matrizColores, matrizSignos, deck):

    jugada = []
    jugadas = []
    total = []
    if not deck:

        return []

    else:
        perm = list(itertools.permutations(deck))
        posiciones = buscarPosicionesValidas(matrizSignos)

        for posicion in posiciones:
            for deck_ in perm:

                #buscarSolucionesDerAux(matrizColores, matrizSignos, list(deck_), posicion, jugada)
                #jugadas += [jugada]
                #jugada = []

                buscarSolucionesIzqAux(matrizColores, matrizSignos, list(deck_), posicion, jugada)
                jugadas += [jugada]
                jugada = []

                #buscarSolucionesArribaAux(matrizColores, matrizSignos, list(deck_), posicion, jugada)
                #jugadas += [jugada]
                #jugada = []

                #buscarSolucionesAbajoAux(matrizColores, matrizSignos, list(deck_), posicion, jugada)
                #jugadas += [jugada]
                #jugada = []

            total += jugadas
            jugadas = []

        total = removerRepetidos(total)
        print("TOTAL JUGADAS")
        for jugada in total:

            print(jugada)

        return total


def removerRepetidos(jugadas):

    resultado = []

    for jugada in jugadas:

        if jugada not in resultado:
            if jugada:
                resultado.append(jugada)

    return resultado


def buscarSolucionesDerAux(matrizColores, matrizSignos, deck, posicion, jugada):

    """
    print("======NUEVA RECURSION=======")

    print("MATRIZ SIGNOS")
    mostrar(matrizSignos)
    print("MATRIZ COLORES")
    mostrar(matrizColores)
    print()
    print("DECK")
    print(deck)
    print("POSICION")
    print(posicion)
    print("JUGADA")
    print(jugada)
    """

    i = posicion[0]
    j = posicion[1]

    if deck:
        a = deck[0]  # Ficha que sera jugada

    # Condicion de parada de la recursividad
    if not deck:

        return 1

    # Si la jugada sirve la agrega a la lista "jugada" y hace llamada recursiva
    # en las direcciones laterales adyacentes a la ficha que se puso
    elif verificarJugadaValida(a, posicion, matrizColores, matrizSignos):
        jugada += [[a, posicion]]
        matrizColores[i][j] = a[1]
        matrizSignos[i][j] = a[0]
        deck.remove(deck[0])

        posAdelante = [posicion[0], posicion[1]+1]
        buscarSolucionesDerAux(matrizColores, matrizSignos, deck, posAdelante, jugada)

        matrizColores[i][j] = 8
        matrizSignos[i][j] = 8
        deck = [a] + deck

    else:  # Sigue la recursion pero no agrega la ficha a la jugada
        deck.remove(deck[0])
        buscarSolucionesDerAux(matrizColores, matrizSignos, deck, posicion, jugada)

        deck = [a] + deck


def buscarSolucionesIzqAux(matrizColores, matrizSignos, deck, posicion, jugada):

    """"
    print("======NUEVA RECURSION=======")
    print("MATRIZ SIGNOS")
    mostrar(matrizSignos)
    print("MATRIZ COLORES")
    mostrar(matrizColores)
    print()
    print("DECK")
    print(deck)
    print("POSICION")
    print(posicion)
    print("JUGADA")
    print(jugada)
    """

    i = posicion[0]
    j = posicion[1]

    if deck:
        a = deck[0]  # Ficha que sera jugada

    # Condicion de parada de la recursividad
    if not deck:

        return 1

    # Si la jugada sirve la agrega a la lista "jugada" y hace llamada recursiva
    # en las direcciones laterales adyacentes a la ficha que se puso
    elif verificarJugadaValida(a, posicion, matrizColores, matrizSignos):
        jugada += [[a, posicion]]
        matrizColores[i][j] = a[1]
        matrizSignos[i][j] = a[0]
        deck.remove(deck[0])

        posAdelante = [posicion[0], posicion[1]-1]
        buscarSolucionesIzqAux(matrizColores, matrizSignos, deck, posAdelante, jugada)

        matrizColores[i][j] = 8
        matrizSignos[i][j] = 8
        deck = [a] + deck

    else:  # Sigue la recursion pero no agrega la ficha a la jugada
        deck.remove(deck[0])
        buscarSolucionesIzqAux(matrizColores, matrizSignos, deck, posicion, jugada)

        deck = [a] + deck


def buscarSolucionesArribaAux(matrizColores, matrizSignos, deck, posicion, jugada):

    """
    print("======NUEVA RECURSION=======")
    print("MATRIZ SIGNOS")
    mostrar(matrizSignos)
    print("MATRIZ COLORES")
    mostrar(matrizColores)
    print()
    print("DECK")
    print(deck)
    print("POSICION")
    print(posicion)
    print("JUGADA")
    print(jugada)
    """
    i = posicion[0]
    j = posicion[1]

    if deck:
        a = deck[0]  # Ficha que sera jugada

    # Condicion de parada de la recursividad
    if not deck:

        return 1

    # Si la jugada sirve la agrega a la lista "jugada" y hace llamada recursiva
    # en las direcciones laterales adyacentes a la ficha que se puso
    elif verificarJugadaValida(a, posicion, matrizColores, matrizSignos):
        jugada += [[a, posicion]]
        matrizColores[i][j] = a[1]
        matrizSignos[i][j] = a[0]
        deck.remove(deck[0])

        posAdelante = [posicion[0]+1, posicion[1]]
        buscarSolucionesArribaAux(matrizColores, matrizSignos, deck, posAdelante, jugada)

        matrizColores[i][j] = 8
        matrizSignos[i][j] = 8
        deck = [a] + deck

    else:  # Sigue la recursion pero no agrega la ficha a la jugada
        deck.remove(deck[0])
        buscarSolucionesArribaAux(matrizColores, matrizSignos, deck, posicion, jugada)

        deck = [a] + deck


def buscarSolucionesAbajoAux(matrizColores, matrizSignos, deck, posicion, jugada):

    """
    print("======NUEVA RECURSION=======")
    print("MATRIZ SIGNOS")
    mostrar(matrizSignos)
    print("MATRIZ COLORES")
    mostrar(matrizColores)
    print()
    print("DECK")
    print(deck)
    print("POSICION")
    print(posicion)
    print("JUGADA")
    print(jugada)
    """
    i = posicion[0]
    j = posicion[1]

    if deck:
        a = deck[0]  # Ficha que sera jugada

    # Condicion de parada de la recursividad
    if not deck:

        return 1

    # Si la jugada sirve la agrega a la lista "jugada" y hace llamada recursiva
    # en las direcciones laterales adyacentes a la ficha que se puso
    elif verificarJugadaValida(a, posicion, matrizColores, matrizSignos):
        jugada += [[a, posicion]]
        matrizColores[i][j] = a[1]
        matrizSignos[i][j] = a[0]
        deck.remove(deck[0])

        posAdelante = [posicion[0]-1, posicion[1]]
        buscarSolucionesAbajoAux(matrizColores, matrizSignos, deck, posAdelante, jugada)

        matrizColores[i][j] = 8
        matrizSignos[i][j] = 8
        deck = [a] + deck

    else:  # Sigue la recursion pero no agrega la ficha a la jugada
        deck.remove(deck[0])
        buscarSolucionesAbajoAux(matrizColores, matrizSignos, deck, posicion, jugada)

        deck = [a] + deck


# E: Una matriz
# S: Una lista de posiciones
# D: Recibe la matriz del tablero y retorna
#    todas las posiciones donde se puede colocar una ficha
def buscarPosicionesValidas(matrizSignos):

    posiciones = []

    for i in range(0, len(matrizSignos) - 1):

        for j in range(0, len(matrizSignos[0]) - 1):

            if matrizSignos[i][j] == 8:  # Verifica que no haya una ficha ahi

                # Pregunta por las posiciones adyacentes a la ficha para saber si hay fichas en las cuales apoyarse
                if matrizSignos[i - 1][j] != 8 or matrizSignos[i + 1][j] != 8 or matrizSignos[i][j - 1] != 8 or matrizSignos[i][j + 1] != 8:
                    posiciones += [[i, j]]

    if not posiciones:
        return [[len(matrizSignos)//2, len(matrizSignos[0])//2]]

    return posiciones



def buscarQwirkleParcial():

    1+1

# E: ficha = [simbolo, color], posicion = [i, j], dos matrices del tablero
# S: booleano. True si es valido poner la ficha en la poscion dada, False en caso contrario
# D: Recibe una ficha, una posicion donde se quiere poner la ficha y las matrices del tablero
#    este algortimo deteremina si se forma una jugada "igual simbolo diferente color"
def verificarJugadaValida(ficha, posicion, matrizColores, matrizSignos):

    i = posicion[0]
    j = posicion[1]
    aux1 = i
    aux2 = j
    simboloArriba = True
    colorArriba = True
    simboloAbajo = True
    colorAbajo = True
    simboloIzquierda = True
    colorIzquierda = True
    simboloDerecha = True
    colorDerecha = True

    # Si es diferente de 8 significa que ya esa posicion esta ocupada
    # por lo tanto no es valido poner una ficha ahi
    if matrizSignos[i][j] != 8:

        return False

    # Parche excepcion hacia arriba
    # print(len(matrizSignos),len(matrizSignos[0]))
    # print(i+1,j)

    if matrizSignos[i+1][j] != 8:

        if matrizSignos[i+1][j] == matrizSignos[i+2][j] and matrizSignos[i+1][j] != ficha[0]:

            return False

    # Parche excpecion derecha
    if matrizSignos[i][j+1] != 8:
        if matrizSignos[i][j+1] == matrizSignos[i][j+2] and matrizSignos[i][j+1] != ficha[0]:

            return False

    # Parche excpecion izquierda
    if matrizSignos[i][j-1] != 8:
        if matrizSignos[i][j-1] == matrizSignos[i][j-2] and matrizSignos[i][j-1] != ficha[0]:

            return False

    # Parche excpecion abajo
    if matrizSignos[i-1][j] != 8:
        if matrizSignos[i-1][j] == matrizSignos[i-2][j] and matrizSignos[i-1][j] != ficha[0]:

            return False

    if posicion[0] >= len(matrizSignos) or posicion[1] >= len(matrizSignos[0]):

        return False

    # Comparar en todas direcciones si el simbolo es el mismo
    # Cada if equivale a un direccion

    # Comparaciones segun simbolo igual
    if matrizColores[i + 1][j] != 8:  # Comparacion hacia abajo
        aux1 += 1
        # Jugada de colores
        while matrizColores[aux1][aux2] != 8:  # Mientras no sea un espacio vacio va a comparar

            if matrizColores[aux1][aux2] == ficha[1]:  # Comparar color igual
                colorAbajo = False
                break

            if matrizSignos[aux1][aux2] != ficha[0]:  # Comparar simbolo diferente
                colorAbajo = False
                break

            else:
                aux1 += 1

        aux1 = i
        aux1 += 1
        # Jugada de simbolos
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar color diferente
                simboloAbajo = False
                break

            if matrizSignos[aux1][aux2] == ficha[0]:  # Comparar simbolo igual
                simboloAbajo = False
                break

            else:
                aux1 += 1

        aux1 = i

    if matrizColores[i - 1][j] != 8:  # Comparacion hacia arriba
        aux1 -= 1
        # Jugada de colores
        while matrizColores[aux1][aux2] != 8:  # Mientras no sea un espacio vacio va a comparar

            if matrizColores[aux1][aux2] == ficha[1]:  # Comparar color igual
                colorArriba = False
                break

            if matrizSignos[aux1][aux2] != ficha[0]:  # Comparar simbolo diferente
                colorArriba = False
                break

            else:
                aux1 -= 1

        aux1 = i
        aux1 -= 1
        # Jugada de simbolos
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar color diferente
                simboloArriba = False
                break

            if matrizSignos[aux1][aux2] == ficha[0]:  # Comparar simbolo igual
                simboloArriba = False
                break

            else:
                aux1 -= 1
        aux1 = i

    if matrizColores[i][j + 1] != 8:  # Comparacion hacia la derecha

        aux2 += 1
        # Jugada de colores
        while matrizColores[aux1][aux2] != 8:  # Mientras no sea un espacio vacio va a comparar

            if matrizColores[aux1][aux2] == ficha[1]:  # Comparar color igual
                colorDerecha = False
                break

            if matrizSignos[aux1][aux2] != ficha[0]:  # Comparar simbolo diferente
                colorDerecha = False
                break

            else:
                aux2 += 1

        aux2 = j
        aux2 += 1
        # Jugada de simbolos
        while matrizColores[aux1][aux2] != 8:  # Mientras no se un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar color diferente
                simboloDerecha = False
                break

            if matrizSignos[aux1][aux2] == ficha[0]:  # Comparar simbolo igual
                simboloDerecha = False
                break

            else:
                aux2 += 1
        aux2 = j

    if matrizColores[i][j - 1] != 8:  # Comparacion hacia abajo

        aux2 -= 1
        # Jugada de colores
        while matrizColores[aux1][aux2] != 8:  # Mientras no sea un espacio vacio va a comparar

            if matrizColores[aux1][aux2] == ficha[1]:  # Comparar color igual
                colorIzquierda = False
                break

            if matrizSignos[aux1][aux2] != ficha[0]:  # Comparar simbolo diferente
                colorIzquierda = False
                break

            else:
                aux2 -= 1

        aux2 = j
        aux2 -= 1
        # Jugada de simbolos
        while matrizColores[aux1][aux2] != 8:  # Mientras no sea un espacio vacio va a comparar

            if matrizColores[aux1][aux2] != ficha[1]:  # Comparar color diferente
                simboloIzquierda = False
                break

            if matrizSignos[aux1][aux2] == ficha[0]:  # Comparar simbolo igual
                simboloIzquierda = False
                break

            else:
                aux2 -= 1

    # print("CA:", colorArriba, " or ", "SA:", simboloArriba, " and ", "CD:", colorDerecha, " or ", "SD:", simboloDerecha, " and ", "CI:", colorIzquierda, " or ", "SI:", simboloIzquierda, " and ", "CAB:", colorAbajo, " or ", "SAB:", simboloAbajo)
    if (colorArriba or simboloArriba) and (colorDerecha or simboloDerecha) and (colorAbajo or simboloAbajo) and (colorIzquierda or simboloIzquierda):

        return True

    else:
        return False

# PERMUTACIONES DEL DECK

# juego()
# puntuacionAux(play)
# seleccionadorDeFichas()

# =================== PRUEBAS PARA EL BACKTRACKING ===================================

# TABLERO SIGNOS

signosTablero = [[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [0, 1, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]

                 # 0  1  2  3  4  5  6  7  8  9 10 11 12
coloresTablero =[[8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]

mano = [[0, 0]]


# print(buscarPosicionesValidas(signosTablero))
# print(verificarJugadaValida([1, 0], [1, 0], coloresTablero, signosTablero))
#print(buscarPosicionesValidas(signosTablero))
buscarSoluciones(coloresTablero, signosTablero, mano)


# GUI
# IMAGENES
# BK
bg = pygame.image.load('bg.png')
# VACIO
vacio = pygame.image.load("vacio.png")


# Crea la ventana
qwirkle = pygame.display.set_mode((1080,720))
# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Nombre de la ventana
pygame.display.set_caption('QWirkle by Sven&Rev')
reloj = pygame.time.Clock()

# FUENTE
font = pygame.font.SysFont("Minecraft", 20)
font2 = pygame.font.SysFont("Minecraft", 40)
font3 = pygame.font.SysFont("Minecraft", 10)


# ACOMODAR IMAGENES
def imageSetter(x, y, name):
    qwirkle.blit(name, (x, y))


# Configuracion texto
# E:  Un string, un color, un numero
# S:  No tiene
# D:  Verifica la superficie en la que se escribira el texto

def texto_aux(texto, fuente, color):
    superficie = fuente.render(texto, True, color)
    return superficie, superficie.get_rect()


# E: Tres numeros, un color, un string
# S: Un texto
# D: Crea el texto

def texto(x, y, texto, tamano, color):
    font = pygame.font.SysFont("Minecraft", tamano)
    superficie, rectangulo = texto_aux(texto, font, color)
    rectangulo.center = ((x), (y))
    qwirkle.blit(superficie, rectangulo)


# MOSTRAR DECKS
def mostrarDecks(x, y, deck):
    xAux = x
    cont = 0
    for elem in deck:
        cont += 1
        name = str(elem[1]+1) + "_" + str(elem[0]+1) + ".png"
        image = pygame.image.load(name)
        imageSetter(int(x), int(y), image)
        x = x+55
        if cont == 3:
            x = xAux
            y = y + 55

# MOSTRAR TABLERO
def tableroJuegoGUI():
    for i in range(len(signosTablero)):
        for j in range(len(signosTablero[0])):
            if signosTablero[i][j] == 8 and coloresTablero[i][j] == 8:
                imageSetter(int(j*52+52/2+50),int(i*52+52/2+50),vacio)
            else:
                name = str(signosTablero[i][j]+1) + "_" + str(coloresTablero[i][j]+1) + ".png"
                image = pygame.image.load(name)
                imageSetter(int(j * 52 + 52 / 2 + 50), int(i * 52 + 52 / 2 + 50), image)


# FUNCION DEL JUEGO
def gui():
    # AGREGA FICHAS
    seleccionadorDeFichas()
    # TURNO
    turno = 1
    # pygame.init()
    play = True
    while play:
        qwirkle.blit(bg, (0, 0))
        texto(550, 30, "QWIRKLE", 50, blanco)
        texto(150, 30, "Total Fichas: " + str (cont), 30, blanco)
        texto(50, 585, "P#1:", 25, blanco)
        texto(280, 585, "Ultimo turno P#1:", 13, blanco)
        texto(280, 625, str(lastP1), 50, blanco)
        texto(100, 585, str(p1), 25, blanco)
        mostrarDecks(20, 600, deckP1)
        texto(400, 585, "P#2:", 25, blanco)
        texto(600, 585, "Ultimo turno P#2:", 13, blanco)
        texto(600, 625, str(lastP2), 50, blanco)
        texto(450, 585, str(p2), 25, blanco)
        mostrarDecks(370, 600, deckP2)
        texto(750, 585, "P#3:", 25, blanco)
        texto(1000, 590, "Ultimo turno P#3:", 13, blanco)
        texto(1000, 625, str(lastP3), 50, blanco)
        texto(800, 585, str(p3), 25, blanco)
        mostrarDecks(720, 600, deckP3)
        tableroJuegoGUI()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if turno == 1:
            game_loop(1)
            turno = 2
        elif turno == 2:
            game_loop(2)
            turno = 3
        elif turno == 3:
            print("Turno 3")
            turno = 1
        pygame.display.update()
        reloj.tick(1)


def game_loop(turno):
    # Variables Globales
    global signosTablero
    global coloresTablero
    # PUNTAJES
    global p1
    global p2
    global p3
    # Decks
    global deckP2
    global deckP1
    global deckP3
    #ultimos turnos
    global lastP1
    global lastP2
    global lastP3
    game = True
    #Condicion Extender Tablero
    #checkExtenderTablero(coloresTablero,signosTablero)
    while game:
    # JUGADOR P1 (El mayor)
        if turno == 1:
            play = maxPuntuaciones(buscarSoluciones(coloresTablero, signosTablero, deckP1)) # Jugada con el mayor Puntaje
            if not play:
                lastP1 = 0
                return
            fichasTurno = listaPosiciones_FichasAux(play, 0)  # Crea una lista con las fichas utilizadas
            deckP1 = eliminadorFichasDeck(deckP1, fichasTurno)  # Elimina las fichas del deck
            colocadorFichas(play) # Coloca las fichas en el tablero
            deckP1 = agregaNuevasFichas(deckP1)  # Agrega nuevas fichas al deck
            posiciones = listaPosiciones_FichasAux(play, 1) #Lista de Posiciones (Necesaria para Puntaciones)
            puntos = puntuacion(play,posiciones) #Calcula los puntos de la jugada
            p1 = p1 + puntos # Suma los puntos
            lastP1 = puntos
            reloj.tick(1)
            return
    # JUGADOR P2
        if turno == 2:
            play = maxPuntuaciones(buscarSoluciones(coloresTablero, signosTablero, deckP2))  # Jugada con el mayor Puntaje
            if not play:
                lastP2 = 0
                return
            fichasTurno = listaPosiciones_FichasAux(play, 0)  # Crea una lista con las fichas utilizadas
            deckP2 = eliminadorFichasDeck(deckP2, fichasTurno)  # Elimina las fichas del deck
            colocadorFichas(play)  # Coloca las fichas en el tablero
            deckP2 = agregaNuevasFichas(deckP2)  # Agrega nuevas fichas al deck
            posiciones = listaPosiciones_FichasAux(play, 1)  # Lista de Posiciones (Necesaria para Puntaciones)
            puntos = puntuacion(play, posiciones)  # Calcula los puntos de la jugada
            p2 = p2 + puntos  # Suma los puntos
            lastP2 = puntos
            reloj.tick(1)
            return
    # JUGADOR P3
        if turno == 3: # Inteligente
            return


# JUGADAS CON PUNTUACIONES
# E: Una lista con todas las jugadas
# S: La jugada con el maximo de puntos
# D: Recibe la lista con las jugadas del backtracking, calcula la puntuacion de cada una y luego selecciona la que tiene mayor puntaje

def maxPuntuaciones(jugadas):

    listaPuntajes = [] # Lista que guarda las puntuaciones de cada jugada

    for jugada in jugadas:                          # Loop para recorrer las jugadas
        #print("Jugada: ",jugada)
        posiciones = listaPosiciones_FichasAux(jugada,1)     # Lista de las posiciones de las fichas a poner en la jugada (Necesario para funcion puntuacion)
        # print(posiciones)
        puntajes = puntuacion(jugada,posiciones)    # Calcula los puntos de las fichas a poner
        listaPuntajes.append(puntajes)              # Agrega a lista con los puntajes de las jugadas recibidas
    if  not listaPuntajes:                          #Si no hay jugadas disponibles
        return []
    i = max(listaPuntajes)                          # Busca el puntaje mayor
    index = listaPuntajes.index(i)                  # Busca el index del puntaje maximo
    jugadaMax = jugadas[index]                      # Jugada Maxima
    #print(jugadaMax)
    return jugadaMax

#Auxiliar
# E: Una lista
# S: Una lista
# D: Agarra las posiciones en las que se ponen las fichas

def listaPosiciones_FichasAux(jugadas,i):
    newList = []
    for elem in jugadas:
        newList.append(elem[i])
    return newList


# COLOCADOR DE FICHAS
# E: Una lista con la jugada (Fichas y Posiciones)
# S: No tiene
# D: Coloca las fichas en las matrices

def colocadorFichas(jugada):
    # Variables Globales
    global signosTablero
    global coloresTablero
    for ficha in jugada:
        i = ficha[1][0]  # FILAS
        j = ficha[1][1]  # COLUMNAS
        signosTablero[i][j] = ficha[0][0]
        coloresTablero[i][j] = ficha[0][1]
    return
# ELIMINADOR DE FICHAS DEL DECK
# E: Un deck, una lista con las fichas usadas
# S: Un deck sin las fichas
# D: Elimina las fichas del deck principal
def eliminadorFichasDeck(deck,fichas):
    print(deck,fichas)
    for ficha in fichas:
        deck.remove(ficha)
    return deck

#juego()
#gui()

