from classManejador import Manejador
import os
if __name__=='__main__':
    manej=Manejador('texto')
    manej.frecuencias()
    input()
    os.system('cls')
    manej.crearArbol()
    manej.getLista().recorrer()
    manej.mostrarArbol()
    manej.comprimirArchivo()
    print(manej.getArbol().decodificador(manej.getArbol().getRaiz(),'01000111110',manej.getArbol().getRaiz()))
    manej.decodificarTeclado('01111101100 01110 0100110')
