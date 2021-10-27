from classPila import PilaSecuencial
import os

if __name__ == "__main__":

    pila = PilaSecuencial(20)
    print('PILAS LLENADAS')
    for i in range(1,11):         #LLENADO PILA INFERIOR
        pila.insertarInf(i)
    
    for i in range(11,21):         #LLENADO PILA SUPERIOR
        pila.insertarSup(i)

    print("Inserto Inferior")  #PROBAMOS INSERTAR NUEVOS ITEMS
    pila.insertarInf(20)
    print("Inserto Superior")
    pila.insertarSup(30)

    input()
    os.system('cls')
    
    print("Pila Inferior")
    cadena=''
    for i in range(10):
        cadena = cadena +' '+ str(pila.suprimirInf())
    print(cadena)

    input()
    os.system('cls')

    print("\nPila Superior")
    cadena=''
    for i in range(10):
        cadena = cadena +' '+ str(pila.suprimirSup())
    print(cadena)