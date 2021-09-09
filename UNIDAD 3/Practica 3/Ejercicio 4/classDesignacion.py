
from numpy import insert


class Designacion:
    __año=None
    __justicia=None
    __cargo=None
    __instancia=None
    __materia=None
    __cantVarones=None
    __cantMujeres=None
    
    def __init__(self,año,just,cargo,inst,mat,varones,mujeres) -> None:
        self.__año=año
        self.__justicia=just
        self.__cargo=cargo
        self.__instancia=inst
        self.__materia=mat
        self.__cantVarones=varones
        self.__cantMujeres=mujeres
    def __str__(self) -> str:
        return ('|{0:^4}|{1:^10}|{2:^10}|{3:^10}|{4:^26}|{5:^7}|{6:^7}|'
        .format(self.__año,self.__justicia,self.__cargo,self.__instancia,self.__materia,self.__cantVarones,self.__cantMujeres))
    def getAño(self):
        return self.__año
    def getJusticia(self):
        return self.__justicia
    def getCargo(self):
        return self.__cargo
    def getInstancia(self):
        return self.__instancia
    def getMateria(self):
        return self.__materia
    def getVarones(self):
        return self.__cantVarones
    def getMujeres(self):
        return self.__cantMujeres