from classPilaEncadenada import PilaEncadenada

def factorial(num):
    factorial=PilaEncadenada()
    for i in range (num):
        mult=num * (num-1)
        factorial.insertar(mult)
        