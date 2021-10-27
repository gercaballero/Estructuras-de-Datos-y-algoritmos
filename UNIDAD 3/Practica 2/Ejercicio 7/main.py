import os
from classColaEncadenada import ColaEncadenada
from classCliente import Cliente
from classCajero import	Cajero
from random import randint
import time

if __name__ == '__main__':
    os.system('cls')
    Simulacion = 60
    tiempoCaj = int(input(">>>Ingrese el tiempo de atencion cajero: "))
    tiempoCli = int(input(">>>Ingrese la frecuencia llegada clientes: "))
    os.system('cls')
    cola = ColaEncadenada()
    cajero = Cajero(tiempoCaj)
    llego=None
    libre=None
    maxima= 0
    cont = 1
    numCli=1
    espera='-'
    print('-----------------------------------SIMULACION-----------------------------------')
    print('{0:^20}{1:^20}{2:^20}{3:^20}\n'.format('Tiempo','Cola','Cajero','Espera'))
    while cont <= Simulacion:
        #Analizo llegada de cliente
        random = 1/randint(1,tiempoCli)
        if random==1/tiempoCli:
            cliente = Cliente(cont)
            
            cliente.setNumero(numCli)
            cola.insertar(cliente)
            llego='Cliente {}'.format(numCli)
            numCli=numCli+1
        else:
            llego='-'
        
        #Atencion del cajero
        if cajero.getlibre():
            if not cola.vacia():
                clienteCola = cola.suprimir()
                espera=cont-clienteCola.getTiempo()
                #Actualizo maximo
                if espera > maxima:
                    maxima = espera
                cajero.setEstado()
                libre='Atiende cliente {}'.format(clienteCola.getNumero())
            else:
                libre='LIBRE'
        print('{0:^20}{1:^20}{2:^20}{3:^20}'.format(cont,llego,libre,espera))
        espera='-'
        if not cajero.getlibre():
            libre='OCUPADO'
            cajero.contar()
        cont+=1
        time.sleep(0.5)
    print('--------------------------------------------------------------------------------')
    print('----------------------------TIEMPO MAXIMO DE ESPERA-----------------------------')
    print('---------------------------------------{}---------------------------------------'.format(maxima))
