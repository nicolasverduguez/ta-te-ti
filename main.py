
# Juego de Ta Te Ti

from verificacion import *
from tablero import *


CRUZ = 'X'
CIRCULO = 'O'
continuarJuego = True
opcion = None

print(' ¡Bienvenido al Ta-Te-Ti! '.center(50,'-'))
print('1. Comenzar juego')
print('2. Salir')

while not esOpcionValida(opcion,1,2):
    try:
        opcion = int(input('-> Ingrese opción: '))
        mssg(opcion,1,2)
    except:
        print(f'Valor invalido. Intente nuevamente\n')

if opcion == 1:

    while continuarJuego:

        tablero = generarTablero()
        hayGanador = False
        turno = 0

        while turno < 9 and not hayGanador:
            
            finJugador = False
            simbolo = None
            
            if turno % 2 == 0:
                print('TURNO DEL JUGADOR 1')
                simbolo = CRUZ
            else:
                print('TURNO DEL JUGADOR 2')
                simbolo = CIRCULO
                
            while not finJugador:
                
                fila = None
                columna = None
                
                try:
                    fila = int(input('-> Fila: '))
                    columna = int(input('-> Columna: '))
                    if existeCasilla(fila, columna):
                        if marcarTablero(tablero, fila, columna, simbolo):
                            turno += 1
                            finJugador = True
                except:
                    print(f'Valor invalido. Intente nuevamente\n')
                        
                if alguienGano(tablero, simbolo):
                    if simbolo == CRUZ:
                        print(f'El JUGADOR 1 ha ganado')
                    else:
                        print(f'El JUGADOR 2 ha ganado')

                    hayGanador = True
                    break

        if not hayGanador:
            print(f'El juego quedo empatado')

        print('FIN DEL JUEGO')
        print('Jugar otra vez? [NO -> 0 | SI -> 1]')

        continuarJuego = None

        while not esOpcionValida(continuarJuego,0,1):
            try:
                continuarJuego = int(input('-> Ingrese opción: '))
                mssg(continuarJuego,0,1)
            except:
                print(f'Valor invalido. Intente nuevamente\n')

    print(' Fin del programa '.center(40,'-'))

else:

    print(' Fin del programa '.center(40,'-'))
