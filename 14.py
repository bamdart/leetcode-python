from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        strs = sorted(strs)
        result = ""
        min_s = strs[0]
        max_s = strs[-1]

        min_len = min(len(min_s), len(max_s))
        for i in range(min_len):
            if min_s[i] != max_s[i]:
                break
            result += min_s[i]

        return result