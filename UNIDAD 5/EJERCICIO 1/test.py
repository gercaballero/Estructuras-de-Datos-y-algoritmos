import os
from classTablaHash import TablaHash
if __name__ =='__main__':
    os.system('cls')
    tabla = TablaHash(10)
    num = int (input('INGRESE NUMERO ----> '))
    while num != -1:
        tabla.insertar(num)
        print(num%tabla.getTamano())
        input()
        os.system('cls')
        num = int (input('INGRESE NUMERO ----> '))
    tabla.mostrarTabla()
    tabla.buscar(1520)
    