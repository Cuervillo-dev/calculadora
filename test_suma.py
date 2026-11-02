import unittest
from suma import suma


class TestSuma(unittest.TestCase):
    def test_positivos(self):
        self.assertEqual(suma(2, 5), 5)

    def test_negativos(self):
        self.assertEqual(suma(-1, 1), 0)

    def test_cero(self):
        self.assertEqual(suma(10, 0), 10)


if __name__ == "__main__":
    unittest.main()
