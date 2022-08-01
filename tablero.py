
# Funciones de tablero

def generarTablero():
    
    '''
    generarTablero()
    Genera un nuevo tablero
    '''

    return [['-','-','-'],['-','-','-'],['-','-','-']]


def mostrarTablero(lst):

    '''
    mostrarTablero(lista)
    Imprime el tablero e informa la cantidad de casillas libres
    '''

    print('\n' + 'Tablero'.center(15,'-') + '\n')
    contador = 0
    
    for fila in lst:
        print(f'{fila[0]} {fila[1]} {fila[2]}')
        
        for valor in fila:
            if valor == '-':
                contador += 1

    print(f'\nQuedan {contador} casillas libres\n')


def marcaRealizada(lst, fila, columna, simbolo):
    
    '''
    marcaRealizada(lista, nroFila, nroColumna, simbolo) -> bool
    Marca el tablero, si es posible, en la posicion establecida
    SI: asigna el simbolo a la casilla y devuelve True
    NO: imprime un mensaje y devuelve False
    '''

    if lst[fila-1][columna-1] == '-':
        lst[fila-1][columna-1] = simbolo
        print(f'\n{simbolo} marcado en el tablero')
        mostrarTablero(lst)
        return True
    else:
        print('\nCasilla ocupada, elige una que este libre\n')
        return False
