MIN_V = -2 ** 31
MAX_V = 2 ** 31 -1

class Solution:
    def myAtoi(self, s: str) -> int:
        result_s = ""
        s = s.strip()

        symbol_count = 0
        for c in s:
            if c.isdigit():
                result_s += c
            elif c == "-" or c == "+":
                if len(result_s) > 0:
                    break

                symbol_count += 1

                if symbol_count > 1:
                    break

                result_s += c

            else:
                break

        if len(result_s) <= symbol_count:
            return 0

        if result_s == "":
            return 0

        result_v = int(result_s)
        result_v = min(MAX_V, result_v)
        result_v = max(MIN_V, result_v)

        return result_v