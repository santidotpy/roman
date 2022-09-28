import unittest
import romanos

class Test_FourInLine(unittest.TestCase):
    
    def test_numbers(self):
        params = [  (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
                    (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'),
                    (500, 'D'), (900, 'CM'), (1000, 'M'), (1549, 'MDXLIX'), (3999, 'MMMCMXCIX')]
        for p1, p2 in params:
            with self.subTest():
                self.assertEqual(p2, romanos.romanNumbers(p1))

    def test_high_number(self):
        number = romanos.romanNumbers(4000)
        self.assertFalse(number)
        

if __name__ == '__main__':
    unittest.main()