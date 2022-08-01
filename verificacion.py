
# Funciones verificacion

def esValido(opcion, val1, val2):
    return opcion == val1 or opcion == val2


def mssgEsValido(opcion, val1, val2):
    if not esValido(opcion, val1, val2):
        print(f'Valor invalido. Intente nuevamente\n')


def casillaValida(fila, columna):

    '''
    casillaValida(nroFila, nroColumna) -> bool
    Verifica si los valores ingresados pertenecen 
    a los de una casilla valida
    '''

    valido = (0 < fila < 4) and (0 < columna < 4)
    return valido


def filaCompleta(lst, simbolo):

    '''
    filaCompleta(lista, simbolo) -> bool
    Verifica si alguna fila esta completamente 
    formada por simbolos de un jugador
    '''

    filaOk = False

    for fila in lst:
       if fila.count(simbolo) == 3:
        filaOk = True

    return filaOk


def columnaCompleta(lst, simbolo):

    '''
    columnaCompleta(lista, simbolo) -> bool
    Verifica si alguna columna esta formada completamente 
    formada por simbolos de un jugador
    '''

    columnaOk = False

    for columna in range(3):

        lstAux = []

        for fila in lst:
            lstAux.append(fila[columna])
            
        if lstAux.count(simbolo) == 3:
            columnaOk = True

    return columnaOk


def diagonal1Completa(lst, simbolo):

    '''
    diagonal1Completa(lista, simbolo) -> bool
    Verifica si la primer diagonal esta formada completamente 
    formada por simbolos de un jugador
    '''

    lstAux = []

    for i in range(3):
        lstAux.append(lst[i][i])

    return lstAux.count(simbolo) == 3


def diagonal2Completa(lst, simbolo):

    '''
    diagonal2Completa(lista, simbolo) -> bool
    Verifica si la segunda diagonal esta formada completamente 
    formada por simbolos de un jugador
    '''

    lstAux = []

    for i in range(3):
        lstAux.append(lst[0+i][2-i])

    return lstAux.count(simbolo) == 3


def existeGanador(lst, simbolo):
    
    '''
    existeGanador(lista, simbolo) -> bool
    Verifica si existe un ganador relacionado con simbolo
    EXISTE: imprime al ganador y finaliza el programa
    NO EXISTE: el programa sigue normalmente
    '''

    ganador = False

    if filaCompleta(lst, simbolo) or columnaCompleta(lst, simbolo) or diagonal1Completa(lst, simbolo) or diagonal2Completa(lst, simbolo):
        ganador = True
    return ganador