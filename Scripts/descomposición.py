import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error el numero está mal")
    else:
        cadena = str(numero)
        longuitud = len(cadena)

        for i in range(longuitud):
            print("{:04d}".format(int(cadena[longuitud-1-i])*10**i))

else:
    print("Error")