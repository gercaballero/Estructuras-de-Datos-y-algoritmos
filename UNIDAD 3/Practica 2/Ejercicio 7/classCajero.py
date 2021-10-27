class Cajero:
    __tiempo = 0
    __contador = 0
    __liberado = None

    def __init__(self,xtiempo):
        self.__tiempo = xtiempo
        self.__contador=0
        self.__liberado = True
    
    def getlibre(self):
        return self.__liberado

    def setEstado(self):
        self.__liberado = False

    def contar(self):
        self.__contador += 1
        if self.__contador == self.__tiempo:
            self.__liberado = True
            self.__contador = 0
    
