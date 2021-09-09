import os,csv
from classDesignacion import Designacion
from ListaEncadenada import ListaEncadenada
class Menu:
    __switcher=None
    __lista=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salida del programa')

    def opcion1(self):
        os.system('cls')
        archivo=open('archivo.csv')
        numline = len(archivo.readlines()) #Obtenemos la cantidad de lineas
        archivo=open('archivo.csv')        #Como se sierra el archivo lo volvemos a abrir
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        self.__lista=ListaEncadenada(numline)
        for fila in reader:
            if bandera:
                bandera=False
            else:
                nuevo=Designacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.insertar(self.__lista.getTope()+1,nuevo)
        archivo.close()
        print('------ARCHIVO LEIDO: LISTA CARGADA------')
        input('Presione para continuar...')
        os.system('cls')
    
    def opcion2(self):
        os.system('cls')
        if self.__lista!=None:
            print('|{0:^4}|{1:^10}|{2:^10}|{3:^10}|{4:^26}|{5:^7}|{6:^7}|'.format("Año","Justicia","Cargo","Instancia","Materia","Varones","Mujeres"))
            print('|{0:^4}|{1:^10}|{2:^10}|{3:^10}|{4:^26}|{5:^7}|{6:^7}|'.format('-'*4,'-'*10,'-'*10,'-'*10,'-'*26,'-'*7,'-'*7))
            self.__lista.recorrer()
        else:
            print('LA LISTA NO HA SIDO CARGADA')
        input()
    def opcion3(self,MH,MS):
        os.system('cls')
        cargo=input('>>>Ingrese un cargo: ')
        for i in range(self.__lista.getTope()):
            
        os.system('cls')

    def opcion4(self,MH,MS):
        os.system('cls')
        band=False
        tipo=input('-Ingrese tipo de helado (100/150/250/500/1000) gramos:')
        while not band:
            if tipo in('100','150','250','500','1000'):
                print('TIPO DE HELADO --{} GRAMOS--'.format(tipo))
                MH.saborPorTipo(int(tipo))
                band=True
            else:
                os.system('cls')
                print('GRAMOS INCORRECTOS')
                tipo=input('-Ingrese tipo de helado (100/150/250/500/1000) gramos:')
        input()
        os.system('cls')