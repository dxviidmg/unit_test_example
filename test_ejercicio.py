import unittest
from ejercicio import is_multiplo

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        r = is_multiplo(2, 2, 'yes')
        self.assertEqual(r, 'yes')

if __name__ == '__main__':
    unittest.main()