from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # We know that the list 'nums' contains n distinct numbers from 0 to n,
        # meaning one number in the range [0, n] is missing.
        # We loop over all numbers from 0 to n (inclusive).
        for i in range(len(nums) + 1):
            # The 'if i not in nums' checks whether the current number 'i'
            # is not present in the list 'nums'.
            # If it is not present, then 'i' is the missing number.
            if i not in nums:
                return i
