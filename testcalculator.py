import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setup(self):
        print("SETUP")
        self.calulator = Calculator()

    def test_add(self):
        print("test_add")
        result = self.calculator.add(3,4)
        self.assertEqual(7,result)

    def test_subtract(self):
        print("test_subtract")
        result = self.calculator.subtract(3,2)
        self.assertEqual(1,result)

    def tearDown(self):
        print("TEAR DOWN")

if __name__ == '__main__':
    unittest.main()
