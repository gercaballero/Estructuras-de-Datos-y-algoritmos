from classTablaHash import TablaHash
import unittest

class TestTablaH(unittest.TestCase):

    def testBuscarPorPosicion(self):
        self.tabla = TablaHash(5,True)

        self.tabla.insertar(15)
        self.tabla.insertar(23)
        self.tabla.insertar(11)
        self.tabla.insertar(25)

        #Tests
        self.assertEqual(self.tabla.buscar(25),5)
        self.assertEqual(self.tabla.buscarPorPosicion(5),25)
    
    def testBuscarClaveInexistente(self):

        self.tabla = TablaHash(5,True)

        self.tabla.insertar(15)
        self.tabla.insertar(23)
        self.tabla.insertar(11)
        self.tabla.insertar(25)

        #Test
        self.assertEqual(self.tabla.buscar(45),None)

if __name__ == '__main__':
    unittest.main()