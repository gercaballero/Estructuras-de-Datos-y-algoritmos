from random import randint, seed, random
import random
from classTablaHash import TablaHash


if __name__ == '__main__':
    cant= int(input('Ingrese cantidad de claves: '))
    tablaPrimo = TablaHash(cant)
    tablaNoPrimo = TablaHash(cant,False)
    claves=[]
    for i in range(tablaPrimo.getTamano()):
        num = randint(10000,99999)
        while num in claves:
            num = randint(5000,9999)
        claves.append(num)
        tablaPrimo.insertar(num)
        tablaNoPrimo.insertar(num)
    tablaPrimo.mostrarTabla()
    tablaNoPrimo.mostrarTabla()
    claveBus = int(input('INGRESE LA CLAVE A BUSCAR ----> '))
    tablaPrimo.buscar(claveBus)
    tablaNoPrimo.buscar(claveBus)
    input()