class Cajero:
    __tiempo = 0
    __contador = 0
    __liberado = None

    def __init__(self,xtiempo):
        self.__tAtencion = xtiempo
        self.__contador=0
        self.__libre = True
    
    def getlibre(self): #Verificar si esta libre el cajero
        return self.__liberado

    def setEstado(self):
        self.__liberado = False

    def contar(self):
        self.__contador += 1
        if self.__contador == self.__tiempo:
            self.__liberado = True
            self.__contador = 0
    
