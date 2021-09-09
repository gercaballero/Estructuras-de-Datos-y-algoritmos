class Paciente:
    __nombre = ""
    __dni = ""
    __especialidad = ""
    __consultorio = 0
    __tiempo = 0
    __tiempoTurno = 0
    
    def __init__(self,nom,dni,esp,num,tiempo,tiempoTurno = 0):
        self.__nombre = nom 
        self.__dni = dni
        self.__especialidad = esp
        self.__consultorio = num
        self.__tiempo = tiempo
        self.__tiempoTurno = tiempoTurno
    def getNombre(self):
        return self.__nombre
    def getDni(self):
        return self.__dni
    def getEsp(self):
        return self.__especialidad
    def getConsultorio(self): #Obtiene el numero de consultorio
        return self.__consultorio
    def getEspera(self,tiempo): #Nos da el tiempo de espera 
        return tiempo - self.__tiempo #restando el tiempo del momento menos el de llegada
    def setTurno(self,tiempo): #Guarda el tiempo en el que se obtuvo el turno
        self.__tiempoTurno = tiempo
    def getEsperaAtencion(self,tiempo): #Nos da el tiempo de espera para ser atendido
        return tiempo - self.__tiempoTurno  #Resta el tiempo de Obtencion del turno menos el actual
    
    