class Cliente:
    __tiempo = 0
    __numero=0

    def __init__(self,xtiempo):
        self.__tiempo = xtiempo

    def setNumero(self,num):
        self.__numero = num
    def getNumero(self):
        return self.__numero
    def getTiempo(self):
        return int(self.__tiempo)