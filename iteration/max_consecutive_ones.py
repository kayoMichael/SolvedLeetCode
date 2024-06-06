import unittest
from typing import List

"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""


def max_consecutive_ones(nums: List[int], k: int) -> int:
    answer = 0
    left = 0
    current = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            current += 1
        if current > k:
            if nums[left] == 0:
                current -= 1
            left += 1

        answer = max(right - left + 1, answer)

    return answer


# Time Complexity: O(N)
# Space Complexity: O(1)

# Reason for not using a while loop in the inner for loop to make the window valid in the sliding window algorithm:
# Since we are finding the MAXIMUM subarray, there is no point of making the window smaller since once we get to line
# 29, We already have found a valid subarray of length x. minimizing might make the window valid but would not
# constitute a maximum.

class TestConsecutiveOnes(unittest.TestCase):
    def test_consecutive_ones(self):
        self.assertEqual(max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6)
        self.assertEqual(max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10)
