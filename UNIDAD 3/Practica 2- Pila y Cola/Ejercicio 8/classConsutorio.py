class Consultorio:
    __tiempoA = 0
    __contador = 0
    __estado= True
    __especialidad = ""
    __pacientes = 0

    def __init__(self,tiempo,esp,pacientes=0):
        self.__tiempoA=tiempo
        self.__contador=0
        self.__estado=True
        self.__especialidad=esp
        self.__pacientes=pacientes

    def getEstado(self):
        return self.__estado
    def setOcupado(self):
        self.__estado = False
    def contar(self):
        self.__contador += 1
        if self.__contador == self.__tiempoA:
            self.__estado = True
            self.__contador = 0
    def getEspecialidad(self):
        return self.__especialidad
    def getPacientes(self):
        return self.__pacientes
    def sumaPacientes(self):
        self.__pacientes+=1
