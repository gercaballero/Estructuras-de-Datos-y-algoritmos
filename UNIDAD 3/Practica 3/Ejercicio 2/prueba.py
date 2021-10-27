from ListaEncadenadaConCursor import ListaEncadenadaConCursores

if __name__=='__main__':
    lista=ListaEncadenadaConCursores(5)
    lista.insertarContenido(10)
    lista.insertarContenido(5)
    lista.insertarContenido(15)
    lista.insertar(1,1)
    print('Primer elemento {}'.format(lista.primerElemento()))
    print('Ultimo elemento {}'.format(lista.ultimoElemento()))
    lista.recorrer()
   