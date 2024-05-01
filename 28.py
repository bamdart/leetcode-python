class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_index_list = []

        now_start_index = -1
        needle_len = len(needle)
        needle_index = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[needle_index]:
                if needle_index == 0:
                    now_start_index = i

                if haystack[i] == needle[0] and needle_index != 0:
                    start_index_list.append(i)

                needle_index += 1
            else:
                if needle_index != 0:
                    if haystack[i] == needle[0]:
                        start_index_list.append(i)
                    needle_index = 0
                    if len(start_index_list) > 0:
                        now_start_index = start_index_list.pop(0)
                        i = now_start_index - 1

            i += 1

            if needle_index == needle_len:
                break

        if needle_index != needle_len:
            return -1
        
        return now_start_index