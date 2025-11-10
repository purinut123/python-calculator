import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # Add
    def test_add2(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_add1(self):
        self.assertEqual(self.calc.add(4, 5), 9)

    # subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(9, 5), 4)

    # multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(9, 5), 45)

    # divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    # modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)


if __name__ == '__main__':
    unittest.main()