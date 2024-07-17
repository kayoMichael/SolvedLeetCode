import unittest
from collections import defaultdict
from typing import List

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2



Constraints:

    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107


"""


def subarray_sum(nums: List[int], k: int) -> int:
    diff_count = defaultdict(int)
    diff_count[0] = 1

    prefix = count = 0

    for num in nums:
        prefix += num

        if prefix - k in diff_count:
            count += diff_count[prefix - k]

        diff_count[prefix] += 1

    return count


class TestSubarraySum(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 1, 1]
        k = 2
        self.assertEqual(subarray_sum(nums, k), 2)

    def test_example_2(self):
        nums = [1, 2, 3]
        k = 3
        self.assertEqual(subarray_sum(nums, k), 2)

    def test_single_element_equal_to_k(self):
        nums = [5]
        k = 5
        self.assertEqual(subarray_sum(nums, k), 1)

    def test_no_subarrays(self):
        nums = [1, 2, 3, 4]
        k = 10
        self.assertEqual(subarray_sum(nums, k), 1)

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        k = 0
        self.assertEqual(subarray_sum(nums, k), 10)

    def test_negative_numbers(self):
        nums = [-1, -1, 1]
        k = 0
        self.assertEqual(subarray_sum(nums, k), 1)

    def test_large_numbers(self):
        nums = [1000000, -1000000, 1000000]
        k = 1000000
        self.assertEqual(subarray_sum(nums, k), 3)

    def test_empty_array(self):
        nums = []
        k = 0
        self.assertEqual(subarray_sum(nums, k), 0)


if __name__ == '__main__':
    unittest.main()
