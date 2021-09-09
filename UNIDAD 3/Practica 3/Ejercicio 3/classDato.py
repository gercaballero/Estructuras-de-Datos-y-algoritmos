class Dato:
    __provincia=None
    __superficie=None

    def __init__(self,prov,sup) -> None:
        self.__provincia=prov
        self.__superficie=sup

    def getSup(self):
        return self.__superficie

    def __gt__(self,otroDato):
        if isinstance(otroDato,Dato):
            return float(self.__superficie)>float(otroDato.getSup())
    
    def __str__(self):
        return ('{0:^20}{1:^10}\n{2:<30}').format(self.__provincia,self.__superficie,'-'*30)