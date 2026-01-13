class Solution:
    def intToRoman(self, num: int) -> str:
        roman_mapper = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",
        }
        result = ""

        for n in roman_mapper:
            char_count = num // n
            result += roman_mapper[n] * char_count
            num -= char_count * n

        result = (
            result
            .replace("IIII", "IV")
            .replace("VIV", "IX")
            .replace("XXXX", "XL")
            .replace("LXL", "XC")
            .replace("CCCC", "CD")
            .replace("DCD", "CM")
        )

        return result