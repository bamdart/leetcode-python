class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        value_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        temp_value = 0
        prev_c = ""
        for c in s:
            temp_value = value_dict[c]
            
            if c != prev_c:
                if prev_c == "I" and (c == "V" or c == "X"):
                    temp_value -= 2
                elif prev_c == "X" and (c == "L" or c == "C"):
                    temp_value -= 20
                elif prev_c == "C" and (c == "D" or c == "M"):
                    temp_value -= 200

            result += temp_value
            prev_c = c

        return result