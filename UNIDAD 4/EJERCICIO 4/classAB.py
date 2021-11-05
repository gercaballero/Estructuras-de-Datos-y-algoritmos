import sys
class Nodo:
    __izq = None
    __der = None
    __char = None
    __frec = 0

    def __init__(self,char=None,frec=0):
        self.__izq = None
        self.__der = None
        self.__char = char
        self.__frec = frec
   
    def setIzq(self,izq):
        self.__izq = izq
    def setDer(self,der):
        self.__der = der
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setCaracter(self,char):
        self.__char = char
    def getCaracter(self):
        return self.__char
    def getFrecuencia(self):
        return self.__frec
    def setFrecuencia(self,frec):
        self.__frec = frec


class ArbolBinario:
    __raiz = None

    def __init__(self,caract,frec):
        self.__raiz = Nodo(caract,frec)

    def getRaiz(self):
        return self.__raiz

    def insertar(self,nodo):
        if self.__raiz.getIzq() is None:
            self.__raiz.setIzq(nodo)
        else:
            self.__raiz.setDer(nodo)


    def codificador(self,raiz,caracter):
        if raiz.getCaracter() != caracter:
            Izq = raiz.getIzq()
            Der = raiz.getDer()
            if caracter in Izq.getCaracter():

                codificado = '0' + self.codificador(Izq,caracter)
            
            elif caracter in Der.getCaracter():

                codificado = '1' + self.codificador(Der,caracter)
            
            else:
                codificado = '-'
            return codificado
        else:
            #Caso base
            return ''
    
    def decodificador(self,raiz,cod,inicio):
            if raiz.getIzq() != None and raiz.getDer() != None:
                if cod=='':
                    #El codigo no es decodificable
                    return '-'
                else:
                    #tomo el primer digito
                    primerDigito = cod[0]

                    #suprimo el primer digito
                    cod = cod[1:] 
                    if primerDigito == '0':
                        char = self.decodificador(raiz.getIzq(),cod,inicio)
                    if primerDigito == '1':
                        char = self.decodificador(raiz.getDer(),cod,inicio)
                    return char
            else:
                if cod != '':
                    #Encuentra un nodo hoja pero sigue habiando codigo por decodificar
                    char = raiz.getCaracter() + self.decodificador(inicio,cod,inicio)
                    return char
                if  cod=='':
                    #Encuentra un nodo hoja y no hay mas codigo
                    #Caso base
                    return raiz.getCaracter()
            

    def mostrar(self, raiz, nivel=0):
        if raiz is not None:
            self.mostrar(raiz.getDer(),  nivel+1)
            print(' ' *7 * nivel + '--> {0}'.format(raiz.getCaracter()))
            print(' ' *7 * nivel + '    {0}'.format(raiz.getFrecuencia()))
            self.mostrar(raiz.getIzq(), nivel+1)

    '''---------SOBRECARGA DE OPERADORES---------'''
    def __le__(self,arbol):
        result = False
        if type(arbol) == ArbolBinario:
            raiz = arbol.getRaiz()
            if self.__raiz.getFrecuencia() <= raiz.getFrecuencia():
                result = True
        return result
