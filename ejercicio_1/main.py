"""
Mapa de puestos

DATOS
puestos = [[1, 0, 1], [0, 0, 1]]
0: disponible. 1: ocupado. Las coordenadas son tuplas (fila, columna), desde cero.

IMPLEMENTA
1. crear_mapa(puestos): devuelve un diccionario {(fila, columna): estado}.
   Utiliza una comprension de diccionarios.
2. obtener_disponibles(puestos): devuelve un set de coordenadas disponibles.
   Utiliza una comprension de conjuntos.
No modifiques el tablero.

COMPROBACIONES CON PRINT
- Muestra el mapa completo y los disponibles.
- Consulta el estado de (1, 2) en el mapa: debe ser 1.
- Disponibles esperados: {(0, 1), (1, 0), (1, 1)}. El orden no importa.
- Agrega y comprueba otro tablero propio.

ANALISIS EN COMENTARIOS
- Cuantas celdas se revisan al obtener los disponibles en el ejemplo?
- Cuantas se revisan para f filas y c columnas? Y para n filas y n columnas?

COMMIT SUGERIDO
Completa ejercicio 1: mapa y puestos disponibles
"""

def crear_mapa(puestos):
    return {(f, c): puestos[f][c] for f in range (len(puestos)) for c in range (len(puestos[0]))}


def obtener_disponibles(puestos):
    return {(f, c) for f in range (len(puestos)) for c in range (len(puestos[0])) if puestos[f][c]==0  }


if __name__ == "__main__":
    puestos = [[1, 0, 1], [0, 0, 1]]

    mapa = crear_mapa(puestos)
    disponibles = obtener_disponibles(puestos)

    
    print ("Mapa competo:" , mapa )
    print ("Disponibles:", disponibles)
    print ("Estado de (1,2):", mapa[(1,2)] )


#Tablero propio:

mi_tablero = [[0, 1], [1,0]]

print("\nMi Mapa propio:", crear_mapa(mi_tablero))
print("\nMis disponibles propio:",obtener_disponibles(mi_tablero))




# ANALISIS
# TODO: se revisan 6 celdas al obtener los disponibles.
# para f filas y c columnas se revisan: (f * c) celdas
# para n filas y n columnas se revisan: n*n = n^2 celdas
