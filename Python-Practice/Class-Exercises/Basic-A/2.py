class Roman_Int:
    def __init__(self):
        self.roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self, roman: str) -> int:
        result = 0
        prev_value = 0

        for char in reversed(roman):
            value = self.roman_to_int[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

        return result

# Example usage:
converter = Roman_Int()
print(converter.convert(int(input("Num to cnovert: "))))  # Output: 1994
