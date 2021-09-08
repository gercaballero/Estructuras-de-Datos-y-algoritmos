
from ListaEncadenada import ListaEncadenada
from EncadenadaConCursor import ListaEncadenadaConCursores
if __name__=='__main__':
    lista=ListaEncadenada(5)
    lista.insertarContenido(10)
    lista.insertarContenido(5)
    '''lista.insertarContenido(15)'''
    '''lista.insertarContenido(16)
    lista.insertarContenido(20)'''
    print('Primer elemento {}'.format(lista.primerElemento()))
    print('Ultimo elemento {}'.format(lista.ultimoElemento()))
    #lista.insertar(2,15)
    #lista.insertar(3,20)
    #lista.suprimir(3)
    lista.recorrer()
   