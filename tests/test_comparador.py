
import unittest
from comparador import encontrar_mais_barato, normalizar_preco

class TestComparador(unittest.TestCase):
    def test_encontrar_mais_barato_simples(self):
        precos = {"A": 10.0, "B": 7.5, "C": 11.0}
        vencedores, menor = encontrar_mais_barato(precos)
        self.assertEqual(vencedores, ["B"])  # mercado B é o mais barato
        self.assertAlmostEqual(menor, 7.5, places=2)

    def test_encontrar_mais_barato_empate(self):
        precos = {"A": 9.9, "B": 9.9, "C": 12.0}
        vencedores, menor = encontrar_mais_barato(precos)
        self.assertCountEqual(vencedores, ["A", "B"])  # empate entre A e B
        self.assertAlmostEqual(menor, 9.9, places=2)

    def test_normalizar_preco(self):
        self.assertAlmostEqual(normalizar_preco("R$ 27,90"), 27.90, places=2)
        self.assertAlmostEqual(normalizar_preco("27.90"), 27.90, places=2)
        self.assertAlmostEqual(normalizar_preco("  15,5  "), 15.5, places=2)

    def test_normalizar_preco_invalido(self):
        with self.assertRaises(ValueError):
            normalizar_preco("abc")
        with self.assertRaises(ValueError):
            normalizar_preco("-10")

if __name__ == '__main__':
    unittest.main()
