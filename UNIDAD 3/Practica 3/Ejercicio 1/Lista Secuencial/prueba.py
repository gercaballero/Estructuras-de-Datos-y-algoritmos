
from ListaContenido import Lista
import numpy as np
if __name__=='__main__':
    li=Lista(3)
    li.insertar(10)
    li.insertar(20)
    li.insertar(33)
    li.insertar(50)
    li.suprimir(22)
    li.recorrer()