
from ListaContenido import Lista
from classDato import Dato
import csv
import os
if __name__=='__main__':
    os.system('cls')
    archivo=open('archivo.csv')
    numline = len(archivo.readlines()) #Obtenemos la cantidad de lineas
    archivo=open('archivo.csv')        #Como se sierra el archivo lo volvemos a abrir
    reader=csv.reader(archivo,delimiter=';')
    bandera=True
    lista=Lista(numline,Dato)
    for fila in reader:
        if bandera:
            bandera=False
        else:
            prov=fila[3]
            sup=fila[6]
            nuevo=Dato(prov,sup)
            lista.insertar(nuevo)
    archivo.close()
    print('{0:^20}{1:^10}'.format('Provincia','Superficie (ha)'))
    print('---------------------------------------------')
    lista.recorrer()
