"""
Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

"""
import unittest
from collections import deque
from typing import List


def longest_subarray(nums: List[int], limit: int) -> int:
    left = 0
    diff = 0
    maximum = deque()
    minimum = deque()

    for right in range(len(nums)):
        while maximum and nums[right] > maximum[-1]:
            maximum.pop()

        while minimum and nums[right] < minimum[-1]:
            minimum.pop()
        maximum.append(nums[right])
        minimum.append(nums[right])

        while maximum[0] - minimum[0] > limit:
            if maximum[0] == nums[left]:
                maximum.popleft()
            if minimum[0] == nums[left]:
                minimum.popleft()
            left += 1
        diff = max(diff, right - left + 1)

    return diff


# Time Complexity: O(N)
# Space Complexity: O(N+M)


class TestLongestSubarray(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(longest_subarray([8, 2, 4, 7], 4), 2)
        self.assertEqual(longest_subarray([10, 1, 2, 4, 7, 2], 5), 4)
        self.assertEqual(longest_subarray([4, 2, 2, 2, 4, 4, 2, 2], 0), 3)

    def test_empty(self):
        self.assertEqual(longest_subarray([], 0), 0)

    def test_single_element(self):
        self.assertEqual(longest_subarray([1], 0), 1)
        self.assertEqual(longest_subarray([1], 1), 1)
        self.assertEqual(longest_subarray([1], 2), 1)
        self.assertEqual(longest_subarray([1], 3), 1)
        self.assertEqual(longest_subarray([1], 4), 1)
