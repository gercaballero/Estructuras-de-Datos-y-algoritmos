from classTorres import Torres
import os
if __name__=='__main__':
    os.system('cls')
    print('----------------------TORRES DE HANOI----------------------')
    print('\n------------------------BIENVENIDO-------------------------')
    n=int(input('>>>¿Con cuantos discos desea jugar?:'))
    torres=Torres(n)
    salir = False
    contador=0
    mov=None
    
    while not salir:
        os.system('cls')
        print('----------------------TORRES DE HANOI----------------------')
        print('-----------------------------------------------------------')
        torres.mostrar()
        print('-----------------------------------------------------------')
        if not torres.comprobar():
            inicial=input('Ingrese torre inicial (salir para terminar): ')
            if inicial.upper()=='SALIR':
                salir=True
            else:
                final=input('Ingrese torre final: ')
                if inicial.isdigit() and final.isdigit():
                    if (int(inicial)>=1 and int(inicial)<4) and (int(final)>=1 and int(final)<4):
                        mov=torres.movimiento(int(inicial)-1,int(final)-1)
                        if mov:
                            contador=contador+1
                    else:
                        print('Numeros de torres no existentes. Reintente')
                else:
                    print('Debe ingresar un numero de torre')
                    input()
        else:
            salir =True
    os.system('cls')
    print('----------------------TORRES DE HANOI----------------------')
    torres.mostrar()
    print('----------------------JUEGO FINALIZADO----------------------')
    print('>>>MOVIMIENTOS REALIZADOS:{}'.format(contador))
    print('>>>MOVIMIENTOS NECESARIOS:{}'.format(2**n-1))
    input()
