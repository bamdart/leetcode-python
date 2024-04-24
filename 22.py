from typing import List

class Solution:
    def backtrack(self, s: str, left: int, n: int):
        result = []
        s_len = len(s)

        if s_len == 2 * n:
            return [s]
        
        if left < 2 * n - s_len:
            result += self.backtrack(s + "(", left + 1, n)
        
        if left > 0:
            result += self.backtrack(s + ")", left - 1, n)

        return result
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack("", 0, n)

