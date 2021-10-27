from classPilas import PilaEncadenada
def conversor(decimal):
    binario=PilaEncadenada()
    cadena=''
    if decimal!=0:
        while decimal!=0:
            bit=decimal%2
            binario.insertar(bit)
            decimal=decimal//2
        while not binario.vacia():
            num=str(binario.suprimir())
            cadena=cadena+num
        print('El numero en binario es: {}'.format(cadena))
    else:
        print('El numero en binario es: 0')

