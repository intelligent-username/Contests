class IntegerToRomanConverter:
    def __init__(self):
        self.roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
    def convert(self, num):
        """
        Convert an integer to a Roman numeral.
        
        :param num: Integer to convert (must be between 1 and 3999).
        :return: A string representing the Roman numeral.
        """
        
        roman_numeral = []
        for value, symbol in self.roman_numerals:
            while num >= value:
                roman_numeral.append(symbol)
                num -= value
        return ''.join(roman_numeral)
    


converter = IntegerToRomanConverter()
print("Less than 4000,")
num_to_convert = int(input("Int to convert: "))
print(converter.convert(num_to_convert))
