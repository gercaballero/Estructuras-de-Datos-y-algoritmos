from classDesignacion import Designacion
from ListaEncadenada import ListaEncadenada
import csv,os
from classMenu import Menu
if __name__=='__main__':
    os.system('cls')
    menu=Menu()
    salir= False           
    while not salir:
            print("\n-------------------Menu-------------------")
            print(' 1- LEER DATOS DE ARCHIVO/GENERAR LISTA')
            print(' 2- RECORRER LISTA')
            print(' 3- CANTIDAD MUJERES POR CARGO')
            print(' 4- CANT. AGENTES POR CARGO,MATERIA Y AÑO')
            print(' 5- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5'):
                menu.opcion(int(op))
                if op=='5':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")