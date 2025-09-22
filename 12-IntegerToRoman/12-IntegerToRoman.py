# Last updated: 9/21/2025, 10:06:25 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        #define the pair
        value_symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
        ]

        resultt = ""
        for value, symbol in value_symbols:
            while num >= value:
                resultt += symbol
                num -= value
        return resultt
        