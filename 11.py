from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                now_left_height = height[left]
                left += 1
                while height[left] <= now_left_height  and left < right:
                    left += 1
            else:
                now_right_height = height[right]
                right -= 1
                while height[right] <= now_right_height and left < right:
                    right -= 1
        
        return max_area