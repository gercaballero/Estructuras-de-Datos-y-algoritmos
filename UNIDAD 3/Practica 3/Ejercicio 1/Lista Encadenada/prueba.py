from ListaEncadenadaPos import ListaEncadenadaPos

if __name__=='__main__':
    lista=ListaEncadenadaPos(5)
    lista.insertar(1,10)
    lista.insertar(1,5)
    lista.insertar(4,30)
    print('Primer elemento {}'.format(lista.primerElemento()))
    print('Ultimo elemento {}'.format(lista.ultimoElemento()))
    #lista.insertar(2,15)
    #lista.insertar(3,20)
    #lista.suprimir(3)
    lista.recorrer()
   