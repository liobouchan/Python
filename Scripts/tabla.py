import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas <1 or filas >9 or columnas <1 or columnas >9:
        print("Filas o columnas incorrectas")
    else:
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                print("*", end=' ')

else:
    print("Mala forma de ejecutar")