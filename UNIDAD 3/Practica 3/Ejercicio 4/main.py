from classDesignacion import Designacion
from ListaEncadenada import ListaEncadenada
import csv,os
from classMenu import Menu
from classManejador import Manejador
if __name__=='__main__':
    os.system('cls')
    menu=Menu()
    manejador=Manejador()
    manejador.carga()
    salir= False           
    while not salir:
            os.system('cls')
            print("\n-------------------Menu-------------------")
            print(' 1- RECORRER LISTA')
            print(' 2- CANTIDAD MUJERES POR CARGO')
            print(' 3- CANT. AGENTES POR CARGO,MATERIA Y AÑO')
            print(' 4- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4'):
                menu.opcion(int(op),manejador)
                if op=='4':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")