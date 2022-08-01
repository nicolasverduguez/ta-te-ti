
# Juego de Ta Te Ti hecho con listas

from verificacion import *
from tablero import *


CRUZ = 'X'
CIRCULO = 'O'
continuarJuego = True
opcion = None

print('¡Bienvenido al Ta-Te-Ti!'.center(50,'-'))
print('1. Comenzar juego')
print('2. Salir')

while not esValido(opcion,1,2):
    try:
        opcion = int(input('>: '))
        mssgEsValido(opcion,1,2)
    except:
        print(f'Valor invalido. Intente nuevamente\n')

if opcion == 1:

    while(continuarJuego):

        tablero = generarTablero()
        hayGanador = False
        turno = 0

        while(turno < 9 and not hayGanador):
            
            finJugador_1 = False
            finJugador_2 = False
            
            if (turno % 2) == 0:
                
                while(not finJugador_1):

                    print('TURNO DEL JUGADOR 1')
                    fila = None
                    columna = None

                    try:
                        fila = int(input('> Fila: '))
                        columna = int(input('> Columna: '))
                        if casillaValida(fila, columna):
                            if marcaRealizada(tablero, fila, columna, CRUZ):
                                turno += 1
                                finJugador_1 = True
                    except:
                        print(f'Valor invalido. Intente nuevamente\n')
                        
                if existeGanador(tablero, CRUZ):
                    hayGanador = True
                    print(f'El JUGADOR 1 ha ganado')
                    break

            else:

                while(not finJugador_2):

                    print('TURNO DEL JUGADOR 2')
                    fila = None
                    columna = None
                    
                    try:
                        fila = int(input('> Fila: '))
                        columna = int(input('> Columna: '))
                        if casillaValida(fila, columna):
                            if marcaRealizada(tablero, fila, columna, CIRCULO):
                                turno += 1
                                finJugador_2 = True
                    except:
                        print(f'Valor invalido. Intente nuevamente\n')

                if existeGanador(tablero, CIRCULO):
                    hayGanador = True
                    print(f'El JUGADOR 2 ha ganado')
                    break

        if not hayGanador:
            print(f'El juego quedo empatado')

        print('Fin del juego\nJugar otra vez? [NO -> 0 | SI -> 1]')

        continuarJuego = None

        while not esValido(continuarJuego,0,1):
            try:
                continuarJuego = int(input('>: '))
                mssgEsValido(continuarJuego,0,1)
            except:
                print(f'Valor invalido. Intente nuevamente\n')

    print('Fin del programa'.center(40,'-'))
else:
    print('Fin del programa'.center(40,'-'))