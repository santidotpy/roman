


def decimalToRoman(n):

    if n >= 4000:
        return False

    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    thousands = m[n // 1000]
    hundreds = c[(n % 1000) // 100]
    tens = x[(n % 100) // 10]
    ones = i[n % 10]

    roman = (thousands + hundreds +
           tens + ones)

    return roman


def romanToDecimal(roman):
     roman = roman.upper()
     roman_values = {    'I': 1, 'V': 5, 'X': 10, 'L': 50,
                         'C':  100, 'D': 500, 'M': 1000
                    }
     int_value = 0

     # check invalid characters
     characters = []
     for char in roman:
          characters.append(char)
          if char not in roman_values.keys():
               return False

     if check_four_consecutive(roman):
          return False

     for i in range(len(roman)):
          if i > 0 and roman_values[roman[i]] > roman_values[roman[i - 1]]:
               int_value += roman_values[roman[i]] - 2 * roman_values[roman[i - 1]]
          else:
               int_value += roman_values[roman[i]]
     return int(int_value)

def check_four_consecutive(roman):
     for char in roman:
          if char*4 in roman:
               return True
     return False


# if __name__ == "__main__":
#     print(romanToDecimal('XXXX'))
#     number = 3999
#     print(intToRoman(number))