MIN_V = -2 ** 31
MAX_V = 2 ** 31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        if x <= MIN_V or x >= MAX_V:
            return 0

        s = str(abs(x))[::-1]

        s = s.lstrip('0')
        if x < 0:
            s = f"-{s}"

        n = int(s)

        if n <= MIN_V or n >= MAX_V:
            return 0

        return n