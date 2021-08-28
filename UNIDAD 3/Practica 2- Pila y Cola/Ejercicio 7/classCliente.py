class Cliente:
    __tiempo = 0

    def __init__(self,xtiempo):
        self.__tiempo = xtiempo

    def getTiempo(self):
        return int(self.__tiempo)