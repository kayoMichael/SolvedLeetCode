import unittest
from typing import List

"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000



Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

"""


def maximum_average_subarray(nums: List[int], k: int) -> float:
    current = 0
    current += sum(nums[:k])
    answer = current

    for index in range(k, len(nums)):
        current += nums[index] - nums[index - k]
        answer = max(current, answer)

    return answer / k


class TestMaximumAverageSubArray(unittest.TestCase):
    def test_maximum_average_sub_array(self):
        self.assertEqual(maximum_average_subarray([1, 12, -5, -6, 50, 3], 4), 12.75)
        self.assertEqual(maximum_average_subarray([5], 1), 5.0)
