from ListaContenido import ListaSecContenido
from ListaPosicion import ListaSecPosicion
import os
if __name__ == '__main__':
    os.system('cls')
    n = int(input('Ingrese cantidad de elementos: '))
    lista = ListaSecPosicion(n)
    listaCont = ListaSecContenido(n)
    
    for i in range(n):
        elemento = int(input('Ingrese valor {}: '.format(i+1)))
        lista.insertar(i+1,elemento)
        listaCont.insertar(elemento)
    print('-----LISTA CARGADA-----')
    lista.recorrer()
    input('Presione una tecla para continuar...')
    os.system('cls')


    print("\n-----LISTA SEC POR POSICION-----")
    i = 1
    while i <= lista.tope():
        valor1 = lista.recuperar(i)
        j = i+1
        while j < lista.tope()+1:
            valor2 = lista.recuperar(j)
            if valor1 == valor2:
                lista.suprimir(j)
            else:
                j += 1
        i+=1
    lista.recorrer()
    input('Presione una tecla para continuar...')
    os.system('cls')

    print("\n-----LISTA SEC POR CONTENIDO-----")
    i = 1

    while i <= listaCont.tope()-1:
        valor1 = listaCont.recuperar(i)
        valor2 = listaCont.recuperar(i+1)
        if valor1 == valor2:
            listaCont.suprimir(i+1)
        else:
            i+=1
    listaCont.recorrer()
    input('Presione una tecla para continuar...')
    os.system('cls')