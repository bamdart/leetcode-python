from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)

        if nums_len == 0:
            return 0

        max_index = nums_len
        min_index = 0

        while 1:
            if max_index - min_index == 1:
                if nums[min_index] >= target:
                    return min_index
                else:
                    return max_index
            
            middle_index = (max_index + min_index) // 2

            if nums[middle_index - 1] < target and nums[middle_index] >= target:
                return middle_index
            
            if nums[middle_index] > target:
                max_index = middle_index
                continue

            if nums[middle_index] < target:
                min_index = middle_index
                continue

