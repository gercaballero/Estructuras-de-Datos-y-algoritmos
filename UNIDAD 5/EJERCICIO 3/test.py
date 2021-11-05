from classTablaHash import TablaHash
import unittest

class TestTablaH(unittest.TestCase):

    def test_generar_pos_por_plegado_cant_digitos_impar(self):
        self.__tablaH = TablaHash(109)

        #Test
        self.assertEqual(self.__tablaH.funcionHash(10547),71)

    def test_generar_pos_por_plegado__cant_digitos_par(self):
        self.__tablaH = TablaHash(109)
        
        self.assertEqual(self.__tablaH.funcionHash(1054),64)


    def test_buscar_claves_por_posicion_con_colision(self):
        
        self.__tablaH = TablaHash(109)

        self.__tablaH.insertar(1142)
        self.__tablaH.insertar(1241)
        self.__tablaH.insertar(1538)

        self.__tablaH.buscarPorPosicion(53)

if __name__ == '__main__':
    unittest.main()
