import unittest
from typing import List

"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

    0 <= j <= nums[i] and
    i + j < n

Return the minimum number of jumps to reach nums[n - 1] using Dynamic Programming.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 1000
    It's guaranteed that you can reach nums[n - 1].


"""


def jump_dp(nums: List[int]) -> int:
    length = len(nums) - 1
    if length == 1:
        return 0

    memo = {}

    def helper(i):
        if i == length:
            return 0
        if i in memo:
            return memo[i]
        else:
            if nums[i] == 0:
                return float('inf')

            level = []
            for val in range(1, nums[i] + 1):
                if val + i <= length:
                    level.append(helper(i + val))
            memo[i] = 1 + min(level)
        return memo[i]

    return helper(0)


# Time Complexity: O(N^2)
# Space Complexity: O(N)


class TestDPJump(unittest.TestCase):
    def test_common_subsequence(self):
        self.assertEqual(jump_dp([2, 3, 1, 1, 4]), 2)
        self.assertEqual(jump_dp([2, 3, 0, 1, 4]), 2)
        self.assertEqual(jump_dp([0]), 0)
        self.assertEqual(jump_dp([1, 1, 1, 1, 0]), 4)
