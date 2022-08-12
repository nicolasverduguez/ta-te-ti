
# -- Funciones del tablero --

def generarTablero():

    # Genera un tablero vacio

    return [['-','-','-'],['-','-','-'],['-','-','-']]


def mostrarTablero(tablero):

    # Imprime el tablero e informa la cantidad de casillas libres

    print('\n' + 'Tablero'.center(15,'-') + '\n')

    contadorCasillas = 0
    
    for fila in tablero:
        print(f'{fila[0]} {fila[1]} {fila[2]}')
        contadorCasillas += fila.count('-')

    print(f'\nQuedan {contadorCasillas} casillas libres\n')


def marcarTablero(tablero, fila, columna, simbolo):

    # Marca, si es posible, el simbolo del jugador en la posicion ingresada
    marcaRealizada = None
    

    if tablero[fila - 1][columna - 1] == '-':

        # Si no esta ocupada la casilla, marca el simbolo

        tablero[fila - 1][columna - 1] = simbolo
        print(f'\nMarca realizada')
        mostrarTablero(tablero)
        marcaRealizada = True

    else:

        # Si esta ocupada se le avisa por consola

        print('Casilla ocupada, elige una que este libre\n')
        marcaRealizada = False
    
    return marcaRealizada
