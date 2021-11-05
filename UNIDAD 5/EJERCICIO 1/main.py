
import random
from classTablaHash import TablaHash

def cargaTabla():
    pass


if __name__ == '__main__':
    cant= int(input('Ingrese cantidad de claves: '))
    tablaPrimo = TablaHash(cant)
    tablaNoPrimo = TablaHash(cant,False)
    for i in range(tablaPrimo.getTamano()):
        num = random.randrange(10000,99999)
        tablaPrimo.insertar(num)
        tablaNoPrimo.insertar(num)
    print('---------TABLA CON NUMERO DE CLAVES PRIMO---------')
    tablaPrimo.mostrarTabla()
    print('---------TABLA SIN NUMERO DE CLAVES PRIMO---------')
    tablaNoPrimo.mostrarTabla()
    claveBus = int(input('INGRESE LA CLAVE A BUSCAR ----> '))
    tablaPrimo.buscar(claveBus)
    tablaNoPrimo.buscar(claveBus)
    input()