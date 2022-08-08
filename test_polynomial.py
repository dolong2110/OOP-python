from unittest import TestCase

from polynomial import Polynomial

class Test(TestCase):

    def test_polynomial(self):
        self.countTestCases()
        self.assertEqual(str(Polynomial([1, 2, 3])), "1.000 z**2 + 2.000 z + 3.000")
        self.assertEqual(str(-Polynomial([1, 2, 3])), "-1.000 z**2 - -2.000 z - -3.000")

if __name__ == '__main__':
    unittest.main()