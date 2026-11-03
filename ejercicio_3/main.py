"""
Reservar y liberar puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]

IMPLEMENTA
1. reservar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta disponible, cambia su estado a 1 y devuelve True. En otro caso, False.
2. liberar_puesto(puestos, coordenada): si la coordenada es valida y el puesto
   esta ocupado, cambia su estado a 0 y devuelve True. En otro caso, False.
Rechaza indices negativos y coordenadas fuera del tablero.
Supone que coordenada es una tupla de dos enteros y el tablero es rectangular,
no vacio y contiene solo 0 y 1. Estas funciones SI modifican el tablero.

COMPROBACIONES CON PRINT
Realiza en orden, sobre el mismo tablero:
- Reservar (0, 1): True.
- Reservar otra vez (0, 1): False.
- Liberar (1, 2): True.
- Liberar otra vez (1, 2): False.
- Reservar (5, 0): False.
- Reservar (-1, 0): False.
Muestra el tablero final y agrega una comprobacion propia.

ANALISIS EN COMENTARIOS
Es necesario recorrer todo el tablero para reservar una coordenada conocida?
Justifica la complejidad de reservar, sin contar la impresion del tablero.

COMMIT SUGERIDO
Completa ejercicio 3: reservas y liberaciones
"""

def reservar_puesto(puestos, coordenada):
    f, c = coordenada
    if f < 0 or c < 0 or f >= len(puestos) or c >= len(puestos[0]):
        return False    
    
    if puestos[f][c] == 0:
        puestos[f][c] = 1
        return True
    return False


def liberar_puesto(puestos, coordenada):
    f, c = coordenada
    if f < 0 or c < 0 or f >= len(puestos) or c >= len(puestos[0]):
        return False

    if puestos[f][c] == 1:
        puestos[f][c] = 0
        return True
    
    return False


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    # TODO: escribe las llamadas y muestra los resultados con print.
    print(reservar_puesto(puestos, (0, 1)))  # True
    print(reservar_puesto(puestos, (0, 1)))  # False
    print(liberar_puesto(puestos, (1, 2)))  # True
    print(liberar_puesto(puestos, (1, 2)))  # False
    print(reservar_puesto(puestos, (5, 0)))  # False
    print(reservar_puesto(puestos, (-1, 0)))  # False

    # TODO: agrega al menos un caso propio.

# ANALISIS
# TODO: responde aqui las preguntas del enunciado.
