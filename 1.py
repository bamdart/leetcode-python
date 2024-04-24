class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index_1, num_1 in enumerate(nums[:-1]):
            for index_2, num_2 in enumerate(nums[index_1 + 1:]):
                if num_1 + num_2 != target:
                    continue

                return [index_1, index_2 + index_1 + 1]
