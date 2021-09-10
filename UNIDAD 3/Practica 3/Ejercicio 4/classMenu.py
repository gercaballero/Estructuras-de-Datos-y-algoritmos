import os,csv
from classDesignacion import Designacion
from ListaEncadenada import ListaEncadenada
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.salir
                         }
    def getSwitcher(self,m):
        return self.__switcher
    def opcion(self,op,m):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(m)

    def salir(self,m):
        print('Salida del programa')

    def opcion1(self,m):
        m.mostrar()
    
    def opcion2(self,m):
        os.system('cls')
        cargo=input('>>>Ingrese un cargo: ')
        m.cantMujeres(cargo)
        input()
        os.system('cls')
    def opcion3(self,m):
        os.system('cls')
        año=input('>>>Ingrese un año(2000-2021): ')
        cargo=input('>>>Ingrese un cargo: ')
        materia=input('>>>Ingrese una materia: ')
        m.cantAgentes(año,cargo,materia)
        os.system('cls')
