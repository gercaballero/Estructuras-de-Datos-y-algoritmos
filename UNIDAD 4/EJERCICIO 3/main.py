import os
from classABB import ABB
from classMenu import Menu 
if __name__=='__main__':
    '''----CARGA ARBOL----'''
    arbol = ABB(70)
    raiz = arbol.getRaiz()
    arbol.insertar(raiz,47)
    arbol.insertar(raiz,92)
    arbol.insertar(raiz,35)
    arbol.insertar(raiz,68)
    arbol.insertar(raiz,83)
    arbol.insertar(raiz,100)
    arbol.insertar(raiz,79)
    '''------------------------------'''


    menu= Menu()
    salir= False     
    os.system('cls')      
    while not salir:
            print("-------------------Menu-------------------")
            print(' 1- MOSTRAR NODO PADRE Y NODO HERMANO')
            print(' 2- CANTIDAD DE NODOS (RECURSIVA)')
            print(' 3- ALTURA DEL ARBOL')
            print(' 4- SUCESORES DE UN NODO')
            print(' 5- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5'):
                menu.opcion(int(op),raiz,arbol)
                if op=='5':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")
            input()
            os.system('cls')