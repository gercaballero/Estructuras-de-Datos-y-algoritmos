class MesaTurnos:
    __tiempoA = 0
    __contador = 0
    __estado = True

    def __init__(self,tiempo):
        self.__tiempoA = tiempo
        self.__contador = 0
        self.__estado = True
    def setOcupado(self):
        self.__estado = False    
    def getEstado(self):
        return self.__estado
    def contar(self):
        self.__contador += 1
        if self.__contador == self.__tiempoA:
            self.__estado = True
            self.__contador = 0