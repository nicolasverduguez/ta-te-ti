# ta-te-ti
Juego de Ta-Te-Ti hecho con Python

### Descripcion
El objetivo del juego es lograr una linea de marcas ('X' o 'O', dependiendo de que jugador sea) de longitud 3 en cualquier sentido (vertical, horizontal o diagonal).
El primero que lo logre se declarara ganador

### Funcionamiento
Es un juego para dos personas:
- JUGADOR 1: le corresponden los turnos pares
- JUGADOR 2: le corresponden los turnos impares
- En total son 9 turnos
- Gana el primero en lograr las 3 marcas en cualquier sentido mencionado en la descripción
- De lo contrario, el juego quedara en empate
- Existen validaciones para las entradas de datos, de modo que:
    - No se permite ingresar valores diferentes a los notificados por pantalla, de lo contrario el programa no avanzara
    - No se permite sobrescribir el valor de la casilla que ya haya marcado otro jugador
    - Se alertara por mensaje si los valores ingresados son incorrectos
