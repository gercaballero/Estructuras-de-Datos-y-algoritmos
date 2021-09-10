from ListaEncadenada import ListaEncadenada
import csv,os
from classDesignacion import Designacion
class Manejador:
    __lista=None

    def __init__(self) -> None:
        self.__lista=ListaEncadenada()
    
    def carga(self):
        archivo=open('archivo.csv',encoding="utf-8")
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        self.__lista=ListaEncadenada()
        for fila in reader:
            if bandera:
                bandera=False
            else:
                nuevo=Designacion(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.insertar(self.__lista.getTope()+1,nuevo)
        archivo.close()

    def mostrar(self):
        os.system('cls')
        if self.__lista!=None:
            print('|{0:^4}|{1:^10}|{2:^10}|{3:^10}|{4:^26}|{5:^7}|{6:^7}|'.format("Año","Justicia","Cargo","Instancia","Materia","Varones","Mujeres"))
            print('|{0:^4}|{1:^10}|{2:^10}|{3:^10}|{4:^26}|{5:^7}|{6:^7}|'.format('-'*4,'-'*10,'-'*10,'-'*10,'-'*26,'-'*7,'-'*7))
            self.__lista.recorrer()
        else:
            print('LA LISTA NO HA SIDO CARGADA')
        input()
    
    def cantMujeres(self,cargo):
        años=[]
        cont=[]
        for i in range(1,self.__lista.getTope()+1):
            rec=self.__lista.recuperar(i)
            año=rec.getAño()
            if año not in años:
                años.append(año)
                cont.append(0)
        for i in range(1,self.__lista.getTope()+1):
            rec=self.__lista.recuperar(i)
            if cargo.upper()==rec.getCargo().upper():
                año=rec.getAño()
                indice=años.index(año)
                cont[indice]+=rec.getMujeres()
        self.mostrarOp2(años,cont,cargo)
    
    def mostrarOp2(self,años,cont,cargo):
        print('----------CANTIDAD DE MUJERES EN EL CARGO {} POR AÑO----------'.format(cargo.upper()))
        print('|{0:^4}|{1:^10}|'.format('AÑO','MUJERES'))
        for i in range(len(años)):
            print('|{0:^4}|{1:^10}|'.format(años[i],cont[i]))
    
    def cantAgentes(self,año,cargo,materia):
        cont=0
        materia=self.cambiarMateria(materia)
        for i in range(1,self.__lista.getTope()+1):
            rec=self.__lista.recuperar(i)
            if año.upper()==rec.getAño().upper() and cargo.upper()==rec.getCargo().upper():
                if materia.upper()==rec.getMateria().upper():
                    cont+=rec.getVarones()
                    cont+=rec.getMujeres()
        print('----------CANTIDAD DE AGENTES----------')
        print('>>>AÑO: {}'.format(año))
        print('>>>CARGO: {}'.format(cargo.upper()))
        print('>>>MATERIA: {}'.format(materia.upper()))
        print('>>>CANTIDAD: {}'.format(cont))
        input()
    


    def cambiarMateria(self,materia):
        if materia.upper()=='MULTIPLE':
            materia='Múltiple'
        elif materia.upper()=='CIVIL' or materia.upper()=='COMERCIAL':
            materia='Civil y/o comercial'
        elif materia.upper() =='PENAL ECONOMICO':
            materia='Penal económico'
        return materia