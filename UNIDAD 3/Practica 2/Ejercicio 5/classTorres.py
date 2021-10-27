from classPila import PilaSecuencial
class Torres:
    __pilas=[]
    __mostrar=[]
    __discos=0
    def __init__(self,xn) -> None:
        self.__discos=xn
        self.setear()
        
    
    def setear(self):
        for i in range(3):
            self.__pilas.append(PilaSecuencial(self.__discos))
            self.__mostrar.append([])
        for j in range(self.__discos,0,-1):
            self.__pilas[0].insertar(j)
        for i in range(self.__discos):
            self.__mostrar[0].append('*'*(i+(i+1)))
            self.__mostrar[1].append('-')
            self.__mostrar[2].append('-')

    def mostrar(self):
        print('{0:^20}{1:^20}{2:^20}'.format('Torre 1','Torre 2','Torre 3'))
        fila=''
        for i in range(self.__discos):
             print('{0:^20}{1:^20}{2:^20}'.format(self.__mostrar[0][i],self.__mostrar[1][i],self.__mostrar[2][i]))

    def movimiento(self,inicio,final):
        exito=False
        a=self.__pilas[inicio].suprimir()
        b=self.__pilas[final].suprimir()
        if b!=None:
            self.__pilas[final].insertar(b)
        if a==None:
            print('---------------------MOVIMIENTO INVALIDO---------------------')
            print('----No hay disco en la torre {}----'.format(inicio+1))
            input()
        else:
            if self.__pilas[final].vacia() or a < b:
                self.__pilas[final].insertar(a)
                self.__mostrar[inicio][int(a)-1]='-'
                self.__mostrar[final][int(a)-1]='*'*(a+(a-1))
                exito=True
            else:                                                                 
                print('---------------------MOVIMIENTO INVALIDO---------------------')
                print('--El disco de la torre {} es mayor que el de la torre {}--'.format(inicio+1,final+1))
                self.__pilas[inicio].insertar(a)
                input()
        return exito


    def comprobar(self):
        fin=False
        if self.__pilas[2].llena():
            fin = True
        return fin
