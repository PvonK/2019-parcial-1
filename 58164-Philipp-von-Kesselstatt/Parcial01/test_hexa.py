import unittest
from hexad import hexad


class test_hexa_1(unittest.TestCase):
    def test_factorial_1(self):
        result = hexad(17)
        self.assertEqual(result, '011')




if __name__ == '__main__':
    unittest.main()