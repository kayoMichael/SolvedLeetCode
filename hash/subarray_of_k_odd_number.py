import unittest
from collections import defaultdict
from typing import List

"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16



Constraints:

    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length


"""


def number_of_k_odd_subarrays(nums: List[int], k: int) -> int:
    total = current = 0
    odd_count = defaultdict(int)
    odd_count[0] = 1
    for num in nums:
        current += num % 2
        total += odd_count[current - k]
        odd_count[current] += 1
    return total


# Time Complexity: O(N)
# Space Complexity: O(N)


class TestNumberOfKOddSubarrays(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 1, 2, 1, 1]
        k = 3
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 2)

    def test_example_2(self):
        nums = [2, 4, 6]
        k = 1
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 0)

    def test_example_3(self):
        nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
        k = 2
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 16)

    def test_empty_array(self):
        nums = []
        k = 1
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 0)

    def test_single_element_array(self):
        nums = [1]
        k = 1
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 1)

    def test_all_odd_numbers(self):
        nums = [1, 3, 5, 7, 9]
        k = 3
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 3)

    def test_k_greater_than_array_length(self):
        nums = [1, 2, 3, 4, 5]
        k = 6
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 0)

    def test_large_array(self):
        nums = [1] * 50000
        k = 25000
        self.assertEqual(number_of_k_odd_subarrays(nums, k), 25001)


if __name__ == '__main__':
    unittest.main()
