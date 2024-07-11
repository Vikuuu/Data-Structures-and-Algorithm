from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newarray_pointer = 1
        count = 1

        length = len(nums)

        for unique_pointer in range(1, length):
            if nums[unique_pointer] != nums[unique_pointer - 1]:
                nums[newarray_pointer] = nums[unique_pointer]
                count += 1
                newarray_pointer += 1

        return count
