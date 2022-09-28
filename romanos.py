


def romanNumbers(n):

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
  
# if __name__ == "__main__":
#     number = 3999
#     print(intToRoman(number))