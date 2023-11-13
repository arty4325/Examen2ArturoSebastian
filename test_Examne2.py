# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 14:18:32 2023

@author: artur
"""

from Exame2 import MiClase
import unittest

class TestEx(unittest.TestCase):
    global objeto 
    objeto = MiClase(35, 35, 35, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    # Test primera funcion Obtine Valencia
    def test_ifNoHayImpares (self): 
        # Test de cuando no hay numeros impares
        global objeto
        self.assertEqual(objeto.ObtieneValencia(200), 0)
    def test_hayImpares (self):
        # Test de cuando si hay numeros impares
        global objeto
        self.assertEqual(objeto.ObtieneValencia(2003), 1)
    def test_unDigito (self):
        # Test de cuando hay un solo digito
        global objeto
        self.assertEqual(objeto.ObtieneValencia(1), 1)
    def test_cero (self):
        # Test de cuando el unico digito es cero
        global objeto
        self.assertEqual(objeto.ObtieneValencia(0), 0)
        
    # Test segunda funcion divisible tempo
    def test_tieneDivisores (self):
        global objeto
        self.assertEqual(objeto.DivisibleTempo((8)), [1, 2, 4, 8])
    def test_numeroPrimo (self):
        global objeto
        self.assertEqual(objeto.DivisibleTempo((13)), [1, 13])
    def test_divisibleUno (self):
        global objeto
        self.assertEqual(objeto.DivisibleTempo((1)), [1])
    def test_impar (self):
        global objeto
        self.assertEqual(objeto.DivisibleTempo((15)), [1, 3, 5, 15])
        
    # Test obtiene maximo de lista
    def test_obtieneMaximo (self):
        global objeto
        self.assertEqual(objeto.ObtieneMasBailable([1,5,3,2]), 5)
    def test_tresValoresIguales (self):
        global objeto
        self.assertEqual(objeto.ObtieneMasBailable([3,3,3]), 3)
    def test_listaVacia (self):
        global objeto
        self.assertEqual(objeto.ObtieneMasBailable([]), None)
    def test_listaDecimales (self):
        global objeto
        self.assertEqual(objeto.ObtieneMasBailable([4.2,3.0,5.4,1.5]), 5.4)
    
    # Test Verifica Lista Canciones
    def test_todasCanciones (self):
        global objeto
        self.assertEqual(objeto.VerificaListaCanciones(["C1", "C2", "C3"]), True)
    def test_faltaUnaCancion (self):
        global objeto
        self.assertEqual(objeto.VerificaListaCanciones(["C1", None, "C2"]), False)
    def test_noHayCanciones (self):
        global objeto
        self.assertEqual(objeto.VerificaListaCanciones([None, None, None]), False)
    def test_listaVaciaCanciones (self):
        global objeto
        self.assertEqual(objeto.VerificaListaCanciones([]), True)
        
    # Test Encuentra Elemento
    def test_EncuentraElemento (self):
         global objeto
         self.assertEqual(objeto.Encuentra([1,2,3,4], 4), True)
    def test_NoEncuentraElemento (self):
         global objeto
         self.assertEqual(objeto.Encuentra([1,2,3,5], 4), False)
    def test_listaNoDeEnteros (self):
         global objeto
         self.assertEqual(objeto.Encuentra([1,2,3,"6"], 6), None)
    def test_listaVaciaEncuentra (self):
         global objeto
         self.assertEqual(objeto.Encuentra([], 6), True)

if __name__ == "__main__":
    unittest.main()