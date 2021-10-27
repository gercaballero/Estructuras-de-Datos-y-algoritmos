class Nodo:
    __clave=None
    __izq=None
    __der=None

    def __init__(self,clave=None) -> None:
        self.__clave=clave
        self.__izq=None
        self.__der=None

    def getClave(self):
        return self.__clave
    def getIzq(self):
        return self.__izq
    def getDer(self):
        return self.__der
    def setClave(self,clave):
        self.__clave=clave
    def setIzq(self,izq):
        self.__izq=izq
    def setDer(self,der):
        self.__der=der

class ABB:
    __raiz=None

    def __init__(self,clave) -> None:
        self.__raiz=Nodo(clave)
    
    def getRaiz(self):
        return self.__raiz

    def insertar(self,raiz,clave):
        if raiz.getClave() == clave:
            print('Elemento Existente')
        else:
            if clave<raiz.getClave():
                if raiz.getIzq()==None:
                    raiz.setIzq(Nodo(clave))
                else:
                    self.insertar(raiz.getIzq(),clave)
            elif clave > raiz.getClave():
                if raiz.getDer()==None:
                    raiz.setDer(Nodo(clave))
                else:
                    self.insertar(raiz.getDer(),clave)
    
    def buscar(self,raiz,clave):
        if raiz == None:
            return None
            #Retorna None cuando no encuentra el nodo
        else:
            if clave == raiz.getClave():
                return raiz
            elif clave < raiz.getClave():
                nodo = self.buscar(raiz.getIzq(),clave)
            elif clave > raiz.getClave():
                nodo = self.buscar(raiz.getDer(),clave)
        return nodo

    def nivel(self,raiz,clave,nivel=1):
        if raiz == None:
            print("Elemento inexistente")
            return None
        else:
            if clave == raiz.getClave():
                return nivel
            elif clave < raiz.getClave():
                level = self.nivel(raiz.getIzq(),clave,nivel+1)
            elif clave > raiz.getClave():
                level = self.nivel(raiz.getDer(),clave,nivel+1)        
        return level

    def hoja(self,raiz,clave):
        if raiz == None:
            print("Elemento inexistente")
            return None
        else:
            if clave == raiz.getClave():
                if raiz.getIzq() == None and raiz.getDer() == None:
                    print("Es una hoja")
                    return True
                else:
                    print("NO es una hoja")
                    return False
            elif clave < raiz.getClave():
                esHoja = self.hoja(raiz.getIzq(),clave)
            elif clave > raiz.getClave():
                esHoja = self.hoja(raiz.getDer(),clave)
        return esHoja

    def hijo(self,raiz,claveH,claveP):
        if raiz == None:
            print("Error: Elemento inexistente")
            return None
        else:
            if claveP == raiz.getClave():
                izq = raiz.getIzq()
                der = raiz.getDer()
                if izq.getClave() == claveH or der.getClave() == claveH:
                    return True
                else:
                    return False
            elif claveP < raiz.getClave():
                esHijo = self.hijo(raiz.getIzq(),claveP,claveH)
            elif claveP > raiz.getClave():
                esHijo = self.hijo(raiz.getDer(),claveP,claveH)        
            return esHijo

    def padre(self,raiz,claveH,claveP):
        if raiz == None:
            print("Error: Elemento inexistente")
            return None
        else:
            if claveP == raiz.getClave():
                izq = raiz.getIzq()
                der = raiz.getDer()
                if izq.getClave() == claveH or der.getClave() == claveH:
                    return True
                else:
                    return False
            elif claveP < raiz.getClave():
                esPadre = self.padre(raiz.getIzq(),claveP,claveH)
            elif claveP > raiz.getClave():
                esPadre = self.padre(raiz.getDer(),claveP,claveH)        
            return esPadre

    def camino(self,raiz,claveX,claveZ,start=True,camino=None):
        if start:
            if raiz == None:
                print("Elemento con clave X inexistente")
                return None
            else:
                if claveX == raiz.getClave():
                    camino = []
                    miCamino = self.camino(raiz,claveX,claveZ,False,camino)
                elif claveX < raiz.getClave():
                    miCamino = self.camino(raiz.getIzq(),claveX,claveZ)
                elif claveX > raiz.getClave():
                    miCamino = self.camino(raiz.getDer(),claveX,claveZ)        
        else:
            if raiz == None:
                print("No existe camino desde {} a {}".format(str(claveX),str(claveZ)))
                return None
            else:
                if claveZ == raiz.getClave():
                    camino.append(claveZ)
                    return camino
                elif claveZ < raiz.getClave():
                    camino.append(raiz.getClave())
                    miCamino = self.camino(raiz.getIzq(),claveX,claveZ,False,camino)
                elif claveZ > raiz.getClave():
                    camino.append(raiz.getClave())
                    miCamino = self.camino(raiz.getDer(),claveX,claveZ,False,camino)
        return miCamino

    def grado(self,raiz):
        grado = 0
        if raiz.getIzq() != None:
            grado += 1
        if raiz.getDer() != None:
            grado += 1
        return grado

    def __encontrarReemplazo(self,raiz,start=True):
        if raiz == None:
            return None
        else:
            if start:
                raiz = raiz.getIzq()
            if raiz.getDer() != None:
                raiz = raiz.getDer()
                self.__encontrarReemplazo(raiz,False)
            return raiz

    def suprimir(self,raiz,clave,ant=None):
        if raiz == None:
            return None
        else:
            if clave == raiz.getClave():
                if raiz.getDer() is None and raiz.getIzq() is None:
                    if ant.getDer() == raiz:
                        ant.setDer(None)
                    else:
                        ant.setIzq(None)
                    del raiz
                elif raiz.getDer() is not None and raiz.getIzq() is None:
                    hijo = raiz.getDer()
                    ant.setDer(hijo)
                    del raiz
                elif raiz.getIzq() is not None and raiz.getDer() is None:
                    hijo = raiz.getIzq()
                    ant.setIzq(hijo)
                    del raiz
               
                elif raiz.getIzq() is not None and raiz.getDer() is not None:
                   
                    nodoReemplazo = self.__encontrarReemplazo(raiz)
                    newClave = nodoReemplazo.getClave()
                    self.suprimir(self.__raiz,newClave)
                    raiz.setClave(newClave)
                    
        
            elif clave < raiz.getClave():
                self.suprimir(raiz.getIzq(),clave,raiz)
            elif clave > raiz.getClave():
                self.suprimir(raiz.getDer(),clave,raiz)            
            
    def altura(self,raiz):
        if raiz is None:
            return 0
        else :
            HIzq = self.altura(raiz.getIzq())
            HDer = self.altura(raiz.getDer())
            if (HIzq > HDer):
                altura = HIzq + 1
            else:
                altura = HDer + 1
            return altura


    '''--------RECORRIDOS-------'''
    def preorden(self, raiz):
        if raiz is not None:
            print(raiz.getClave(), end=", ")
            self.preorden(raiz.getIzq())
            self.preorden(raiz.getDer())
    
    def inorden(self, raiz, nivel=0):
        if raiz is not None:
            self.inorden(raiz.getIzq(),  nivel+1)
            print(' ' *7 * nivel + '--> {}'.format(raiz.getClave()))
            self.inorden(raiz.getDer(), nivel+1)

    def postorden(self, raiz):
        if raiz is not None:
            self.postorden(raiz.getIzq())
            self.postorden(raiz.getDer())
            print(raiz.getClave(), end=", ")