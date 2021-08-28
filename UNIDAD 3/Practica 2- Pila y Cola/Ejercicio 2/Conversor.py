from classPilaEncadenada import PilaEncadenada
def conversor(decimal):
    bit=None
    binario=PilaEncadenada()
    if decimal!=0:
        while decimal!=0:
            bit=decimal%2
            binario.insertar(bit)
            decimal=decimal//2
        print('El numero en binario es: ')
        binario.mostrar()
    else:
        print('El numero en binario es: 0')

