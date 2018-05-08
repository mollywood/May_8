from calculator import calculator

class TestCalculator(unittest.TestCase):

    def setup(self):
        print("SETUP IS RUNNING")

    def test_add(self):
        calculator = Calculator()
        result = calculator.add(5.4)
        self.assertEqual(9, result)

    def test_subtract(self):
        result = calculator.subtract(9,3)
        self.assertEqual(6,result)

    def tearDown(self):
        print("TEAR DOWN")

if __name__== '__main__':
    unittest.main()
