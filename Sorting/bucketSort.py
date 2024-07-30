from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for i in range(0, len(nums)):
            n = nums[i]
            counts[n] += 1

        i = 0
        for n in range(0, len(counts)):
            for _ in range(0, counts[n]):
                nums[i] = n
                i += 1
