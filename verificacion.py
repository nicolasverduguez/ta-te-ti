
# -- Funciones de verificación --

def esOpcionValida(num, valor, otroValor):
    return num == valor or num == otroValor


def mssg(num, valor, otroValor):
    if not esOpcionValida(num, valor, otroValor):
        print(f'Opción invalido. Intente nuevamente\n')


def existeCasilla(fila, columna):

    # Verifica que los valores ingresados correspondan a una posicion que exista
    # dentro del tablero

    valido = (0 < fila < 4) and (0 < columna < 4)
    return valido


def filaCompleta(tablero, simbolo):

    # Verifica si una fila contiene unicamente simbolos de un mismo jugador

    filaOk = False

    for fila in tablero:
       if fila.count(simbolo) == 3:
        filaOk = True
        break

    return filaOk


def columnaCompleta(tablero, simbolo):

    # Verifica si una columna contiene unicamente simbolos de un mismo jugador

    columnaOk = False

    for num in range(3):
        if tablero[0][num] == simbolo and tablero[1][num] == simbolo and tablero[2][num] == simbolo:
            columnaOk = True
            break

    return columnaOk


def primerDiagonalCompleta(tablero, simbolo):

    # Verifica si la primer diagonal contiene unicamente simbolos de un mismo jugador

    lstAux = []

    for num in range(3):
        lstAux.append(tablero[num][num])

    return lstAux.count(simbolo) == 3


def segundaDiagonalCompleta(tablero, simbolo):

    # Verifica si la segunda diagonal contiene unicamente simbolos de un mismo jugador

    lstAux = []

    for num in range(3):
        lstAux.append(tablero[0+num][2-num])

    return lstAux.count(simbolo) == 3


def alguienGano(tablero, simbolo):
    
    # Verifica si algun jugador gano el juego

    ganador = False

    if filaCompleta(tablero, simbolo) or columnaCompleta(tablero, simbolo) or primerDiagonalCompleta(tablero, simbolo) or segundaDiagonalCompleta(tablero, simbolo):
        ganador = True

    return ganador
    