from classColaEncadenada import ColaEncadenada
from classPaciente import Paciente
from classMesaTurnos import MesaTurnos
from classConsutorio import Consultorio
import time
import random
import os
if __name__ == "__main__":
#-------------------------------------------------# 
    Simulacion = 4*60   #Tiempo de simulacion
    tiempoCli = 1       #Tiempo de llegada a cola de turnos
    tiempoTurnos = 2    #Tiempo de mesa de entrada para dar turnos
    tiempoMedicos=20    #Tiempo de atencion de los medicos en consultorio
    mesaTurnos = MesaTurnos(tiempoTurnos)
#-------------------------------------------------#
    esp=["Ginecologo","Clinico Medico","Oftalmologo","Pediatra"]
    consultorios=[]
    for i in range(len(esp)):
        consultorios.append(Consultorio(tiempoMedicos,esp[i]))
#-------------------------------------------------#
    colaTurnos=ColaEncadenada()     #Cola de llegada para solicitar turnos
    colasEspecialidades=[]          #Lista de colas para cada consultorio
    for i in range(len(esp)):
        colasEspecialidades.append(ColaEncadenada())    #Agrega en la lista las colas para cada consultorio
#-------------------------------------------------#
    contCola=0          #Contador de personas que llegan a la cola de turnos
    sumadorEspera=0     #Sumador de tiempo de espera de personas que se le dio turno
    contTurnos=0        #Contador de personas que se les dio turno
    sumadorEsp=[]       #Lista con sumadores para espera de cada especialidad
    contadorEsp=[]      #Lista con contadores para saber cuantos pacientes se les atendio
    for i in range(len(esp)):  #Cerea los sumadores y contadores de cada consultorio
        sumadorEsp.append(0)
        contadorEsp.append(0)
#-------------------------------------------------# 
    #PRINTS
    turnos=[None,None,None,None,None]  #[tiempo,nombre,dni,especialidad,estado de mesa]
    '''Estado de la mesa de entrada en el tiempo para mostrar los datos de mesa de entrada'''
    atendidos=[]    
    for i in range(len(esp)):
        atendidos.append([])           #ESTADO DE CADA CONSULTORIO       
#-------------------------------------------------# 
    '''-----SIMULACION-----'''
    os.system('cls')
    i = 1
    print('|{0:^5}|{1:^15}|{2:^10}|{3:^15}|{4:^42}|'.format('Min','Nombre','DNI','Especialidad','Mesa De Entradas'))
    while i <= Simulacion:
        if i <=60:      #TIEMPO DE ATENCION DE MESA DE ENTRADA
            turnos[0]=i #ASIGNA A LA LISTA EL TIEMPO DE SIMULACION DEL MOMENTO
            if 1/tiempoCli == 1 /random.randint(1,tiempoCli):
                nombre = 'Paciente '+str(contCola+1)
                dni = random.randint(7000000,44000000)
                posicion=random.randint(0,len(esp)-1)
                especialidad=esp[posicion]
                nuevo = Paciente(nombre,dni,especialidad,posicion,i)
                colaTurnos.insertar(nuevo)
                contCola+=1
                turnos[1]=nombre
                turnos[2]=dni
                turnos[3]=especialidad
            else:
                turnos[1]='-'
                turnos[2]='-' 
                turnos[3]='-'   
            
            if mesaTurnos.getEstado():
                if not colaTurnos.vacia():
                    paciente = colaTurnos.suprimir()
                    num = paciente.getConsultorio()
                    paciente.setTurno(i)
                    colasEspecialidades[num].insertar(paciente)
                    espera = paciente.getEspera(i)
                    sumadorEspera += espera
                    contTurnos += 1
                    mesaTurnos.setOcupado()
                    nombre = paciente.getNombre()
                    turnos[4] = "Toma a {} con espera de {} min".format(nombre,espera)
                else:
                    turnos[4] = "Libre"  
            else:
                turnos[4] = "Ocupado" 
            #-------------------------------------------------------------------------------
            print('|{0:^5}|{1:^15}|{2:^10}|{3:^15}|{4:^42}|'.format(turnos[0],turnos[1],turnos[2],turnos[3],turnos[4]))
            time.sleep(.25)
            #-------------------------------------------------------------------------------

        for j in range(len(esp)):
            if consultorios[j].getEstado():
                if not colasEspecialidades[j].vacia() and consultorios[j].getPacientes() < 10:
                    pacienteAtendido = colasEspecialidades[j].suprimir()
                    espera = pacienteAtendido.getEsperaAtencion(i)
                    sumadorEsp[j] += espera
                    contadorEsp[j] +=1
                    nombre = pacienteAtendido.getNombre()
                    consultorios[j].setOcupado()
                    consultorios[j].sumaPacientes()
                    libreConsultorio = "{} espera {}".format(nombre,espera)
                elif consultorios[j].getPacientes()>=10:
                    libreConsultorio='Maximo'
                else:
                    libreConsultorio = "Libre, {} restantes".format(10-consultorios[j].getPacientes())             
            else:
                libreConsultorio = "Ocupado"
            atendidos[j].append([i,libreConsultorio])
        i+=1
        if not mesaTurnos.getEstado():
            mesaTurnos.contar()
        for k in range(len(esp)):
            if not consultorios[k].getEstado():               
                consultorios[k].contar()   
#-------------------------------------------------------------------------------
    input()
    print('-'*110)
    print('|{0:^5}|{1:^25}|{2:^25}|{3:^25}|{4:^25}|'.format('Min',esp[0],esp[1],esp[2],esp[3]))
    for j in range(Simulacion):
            print('|{0:^5}|{1:^25}|{2:^25}|{3:^25}|{4:^25}|'.format(atendidos[0][j][0],atendidos[0][j][1],atendidos[1][j][1],atendidos[2][j][1],atendidos[3][j][1]))
            time.sleep(0.1)
#-------------------------------------------------------------------------------
    input('Presione para continuar...')
    os.system('cls')
    print('{0:<25}{1:^}{2:>25}\n'.format('-'*25,'RESULTADOS','-'*25))
    print('\n>>>>TIEMPO PROMEDIO DE ESPERA EN COLA: {} min\n'.format(sumadorEspera//contTurnos))
    print('-'*60)
    for i in range(len(esp)):
        print('>>>>TIEMPO PROMEDIO DE ESPERA EN {}: {} min\n'.format(esp[i].upper(),sumadorEsp[i]//contadorEsp[i]))
    print('-'*60)
    print('\n>>>>CANTIDAD DE PERSONAS QUE NO OBTUVIERON TURNO: {}\n'.format(contCola-contTurnos))
    print('-'*60)
    input('Presione para continuar...')