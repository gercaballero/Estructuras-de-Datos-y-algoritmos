import os

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op,raiz,arbol):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(raiz,arbol)

    def salir(self,raiz,arbol):
        print('Salida del programa')

    def opcion1(self,raiz,arbol):
        clave= input('Ingrese la clave de un nodo: ')
        
    def opcion2(self,raiz,arbol):
        band=False
        print('---------MONTO POR TAREA---------')
        tarea=input('INGRESE TAREA:')
        while not band:
            if tarea in ('carpinteria','electricidad','plomeria'):
                os.system('cls')
                print('---------MONTO POR TAREA---------')
                print ('EL TOTAL DE LA TAREA {} ES DE {}'.format(tarea.upper(),co.totalTarea(tarea)))
                band=True
            else:
                os.system('cls')
                print('---------MONTO POR TAREA---------')
                print('TAREA INCORRECTA. REINTENTE\n')
                tarea=input('INGRESE TAREA:')
        input()
        os.system('cls')
    def opcion3(self,co):
        os.system('cls')
        print('\t\t~~~LISTA DE AYUDADOS POR LA EMPRESA~~~')
        co.listarAyudados()
        
    def opcion4(self,co):
        os.system('cls')
        print('\t\t~~~~~~SUELDOS EMPLEADOS~~~~~~')
        co.ListarSueldos()
        input()
        os.system('cls')