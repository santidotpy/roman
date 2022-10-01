import unittest
import romanos

class Test_FourInLine(unittest.TestCase):
    
    def test_decimalToRoman(self):
        params = [  (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'),
                    (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'),
                    (500, 'D'), (900, 'CM'), (1000, 'M'), (1549, 'MDXLIX'), (3999, 'MMMCMXCIX')]
        for p1, p2 in params:
            with self.subTest():
                self.assertEqual(p2, romanos.decimalToRoman(p1))

    def test_high_number(self):
        number = romanos.decimalToRoman(4000)
        self.assertFalse(number)

    def test_romanToDecimal(self):
        params = [  ('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10),
                    ('XL', 40), ('L', 50), ('XC', 90), ('C', 100), ('CD', 400),
                    ('D', 500), ('CM', 900), ('M', 1000), ('MDXLIX', 1549), ('MMMCMXCIX', 3999)]
        for p1, p2 in params:
            with self.subTest():
                self.assertEqual(p2, romanos.romanToDecimal(p1))

    def test_wrong_value(self):
        number = romanos.romanToDecimal('a')
        self.assertFalse(number)

    def test_consecutive(self):
        number = romanos.romanToDecimal('XXXX')
        self.assertFalse(number)        

    def test_check_four_consecutive(self):
        number = romanos.check_four_consecutive('XXXDDDMMMLLLL')
        self.assertTrue(number)

    def test_check_four_consecutive_false(self):
        number = romanos.check_four_consecutive('XXX')
        self.assertFalse(number)     


if __name__ == '__main__':
    unittest.main()