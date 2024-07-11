from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                i += 1
                k += 1
            elif nums[i] == val:
                i += 1
        return k
