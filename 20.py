class Solution:
    def isValid(self, s: str) -> bool:
        temp_list = []

        for c in s:
            if c in ['(', '{', '[']:
                temp_list.append(c)
            else:
                if len(temp_list) == 0:
                    return False
                if c == ')' and temp_list[-1] != '(':
                    return False
                if c == '}' and temp_list[-1] != '{':
                    return False
                if c == ']' and temp_list[-1] != '[':
                    return False
                temp_list.pop()

        return len(temp_list) == 0