import os
from classColaEncadenada import ColaEncadenada
from classCliente import Cliente
from classCajero import	Cajero
from random import randint


if __name__ == '__main__':
    os.system('cls')
    Simulacion = 60
    tiempoCaj = int(input("Ingrese el tiempo de atencion cajero: "))
    tiempoCli = int(input("Ingrese la frecuencia llegada clientes: "))
    cola = ColaEncadenada()
    cajero = Cajero(tiempoCaj)
    maxima= 0
    cont = 1

    while cont <= Simulacion:
        print('\n\n-----Tiempo {}-----'.format(cont))
        #Analizo llegada de cliente
        random = randint(1,tiempoCli)
        if random==2:
            cliente = Cliente(cont)
            cola.insertar(cliente)
            print('\n >> Llego Cliente: SI')
        else:
            print('\n >> Llego Cliente: NO')
        
        #Atencion del cajero
        if cajero.getlibre():
            if not cola.vacia():
                clienteCola = cola.suprimir()
                espera=cont-clienteCola.getTiempo()
                #Actualizo maximo
                if espera > maxima:
                    maxima = espera
                cajero.setEstado()
            else:
                print('\n >> Cajero: LIBRE')             
        
        if not cajero.getlibre():
            print('\n >> Cajero: OCUPADO')
            cajero.contar()
        print('\n >> EN COLA: {}'.format(cola.getCant()))
        cont+=1
