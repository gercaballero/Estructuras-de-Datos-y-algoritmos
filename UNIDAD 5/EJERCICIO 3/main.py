from random import randint, seed, random
import random
from classTablaHash import TablaHash
import os

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
    print('---------TABLA PRIMO---------')
    acum,cont = tablaPrimo.datos()
    longitud_promedio = acum // cont
    cant_listas=0
    for i in range(len(tablaPrimo.getTabla())):
        if tablaPrimo.getTabla()[i] != None:
            if tablaPrimo.getTabla()[i].len() <= longitud_promedio + 3 and tablaPrimo.getTabla()[i].len() >= longitud_promedio - 3:
                cant_listas += 1
    print("Cantidad de listas con datos: {}".format(cont))
    print("Longitud de listas promedio: {}".format(longitud_promedio))
    print("Cantidad de listas que registran longitud +/-3 respecto de la longitud promedio: {}".format(cant_listas))
    print('---------TABLA NO PRIMO---------')
    input()
    os.system('cls')
    acum,cont = tablaNoPrimo.datos()
    longitud_promedio = acum // cont
    cant_listas=0
    for i in range(len(tablaPrimo.getTabla())):
        if tablaPrimo.getTabla()[i] != None:
            if tablaPrimo.getTabla()[i].len() <= longitud_promedio + 3 and tablaPrimo.getTabla()[i].len() >= longitud_promedio - 3:
                cant_listas += 1
    print("Cantidad de listas con datos: {}".format(cont))
    print("Longitud de listas promedio: {}".format(longitud_promedio))
    print("Cantidad de listas que registran longitud +/-3 respecto de la longitud promedio: {}".format(cant_listas))
    input()