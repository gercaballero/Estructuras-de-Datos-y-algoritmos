
from ListaEncadenadaCont import ListaEncadenadaCont
from classAB import ArbolBinario
import os
class Manejador:
    __lista=None
    __arbolDeHuffman=None
    __caracteres = []
    __frecuencias = []
    __archivo=None

    def __init__(self,nombre) -> None:
        self.__lista=ListaEncadenadaCont()
        self.__caracteres=[]
        self.__frecuencias=[]
        self.__archivo=nombre
        self.leerArchivo()
    
    def leerArchivo(self):
        archivo = open(self.__archivo + '.txt','r')
        for fila in archivo:
            for letra in fila:
                if letra != ' ':
                    if letra not in self.__caracteres:
                        self.__caracteres.append(letra)
                        self.__frecuencias.append(1)
                    else:
                        self.__frecuencias[self.__caracteres.index(letra)]+=1
        archivo.close()

    def frecuencias(self):
        for i in range(len(self.__caracteres)):
            print('{}---->{}'.format(self.__caracteres[i],self.__frecuencias[i]))

    def crearArbol(self):
            for i in range(len(self.__caracteres)):
                nuevoArbol = ArbolBinario(self.__caracteres[i],self.__frecuencias[i])
                self.__lista.insertar(nuevoArbol)
            
            while self.__lista.len() > 1:
                primero = self.__lista.suprimir(0)
                segundo = self.__lista.suprimir(0)

                nuevoCaract = primero.getDato().getRaiz().getCaracter() + segundo.getDato().getRaiz().getCaracter()
                nuevaFrecuen = primero.getDato().getRaiz().getFrecuencia() + segundo.getDato().getRaiz().getFrecuencia()
                
                nuevoArbol = ArbolBinario(nuevoCaract,nuevaFrecuen)
                
                nuevoArbol.insertar(primero.getDato().getRaiz())
                nuevoArbol.insertar(segundo.getDato().getRaiz())
                
                self.__lista.insertar(nuevoArbol)
        
            nodo = self.__lista.suprimir(0)
            self.__arbolDeHuffman = nodo.getDato()

    def mostrarArbol(self):
            raiz = self.__arbolDeHuffman.getRaiz()
            self.__arbolDeHuffman.mostrar(raiz)
    
    def comprimirArchivo(self):
            raiz = self.__arbolDeHuffman.getRaiz()
            archivo = open(self.__archivo + '.txt', 'r')
            comprimido = ''
            for fila in archivo:
                for caracter in fila:
                    if caracter == ' ':
                        comprimido += ' '
                    else:
                        comprimido += self.__arbolDeHuffman.codificador(raiz,caracter)
                     
            archivo.close()
            nuevoArchi = self.__archivo + '_comprimido.txt'
            archivo = open (nuevoArchi,'w')
            archivo.write(comprimido)
            archivo.close()
            os.system('cls')
            print('---------ARCHIVO COMPRIMIDO GENERADO--------')
            input()
    def codificarTeclado(self,texto):
        codigo=''
        while texto!='':
            caract=texto[0]
            texto=texto[1:]
            if caract!=' ':
                codigo+=self.__arbolDeHuffman(self.__arbolDeHuffman.getRaiz(),caract)
            else:
                codigo+=' '
            print(codigo)
            return codigo

    def decodificarTeclado(self,codigo):
            texto = ''
            codigo.replace('\n',' ')
            codigos = codigo.split(' ')
            for codigo in codigos:
                char = self.__arbolDeHuffman.decodificador(self.__arbolDeHuffman.getRaiz(),codigo,self.__arbolDeHuffman.getRaiz())
                texto += char
                texto+= ' '
            print('Texto decodificado: {}'.format(texto))
    def getLista(self):
        return self.__lista
    def getArbol(self):
        return self.__arbolDeHuffman
