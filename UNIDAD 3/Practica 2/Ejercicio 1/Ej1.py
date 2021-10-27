from classPilaEncadenada import PilaEncadenada

if __name__=='__main__':
    pilaE=PilaEncadenada()
    pilaE.insertar(1)
    pilaE.insertar(2)
    pilaE.insertar(3)
    pilaE.mostrar()
    pilaE.suprimir()
    print('-----------------------')
    pilaE.mostrar()