import unittest
from typing import List

"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""


def find_largest_sum_length_k(arr: List[int], k: int) -> int:
    current = 0

    for right in range(k):
        current += arr[right]

    answer = current
    for right in range(k, len(arr)):
        current += arr[right] - arr[right - k]
        answer = max(current, answer)

    return answer


# Time Complexity: O(N)
# Space Complexity: O(1)

class TestLargestSubarray(unittest.TestCase):
    def test_subarray(self):
        self.assertEqual(find_largest_sum_length_k([3, -1, 4, 12, -8, 5, 6], 4), 18)
        self.assertEqual(find_largest_sum_length_k([3, 4, 2, 1], 4), 10)
        self.assertEqual(find_largest_sum_length_k([-1, 0, -1, -1, 0, 1], 2), 1)
