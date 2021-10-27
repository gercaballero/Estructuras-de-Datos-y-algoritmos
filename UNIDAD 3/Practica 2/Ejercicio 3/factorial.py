from classPilas import PilaEncadenada

def factorial(num):
    pila=PilaEncadenada()
    fac=1
    while num > 0:
        pila.insertar(num)
        num -= 1
    while not pila.vacia():
        x = pila.suprimir()
        fac = fac * x
    print('EL FACTORIAL ES: {}'.format(fac))