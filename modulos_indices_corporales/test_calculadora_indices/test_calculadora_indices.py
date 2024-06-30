import unittest
import modulos_indices_corporales.calculadora_indices as calc


class TestCalculadora(unittest.TestCase):
    def test_calcular_imc(self):
        self.assertEqual(calc.calcular_imc(81, 1.75), 26.45)
        self.assertEqual(calc.calcular_imc(58, 1.69), 20.31)


if __name__ == '__main__':
    unittest.main()
