import unittest
from typing import List

"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.



Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.


"""


def find_max_length(nums: List[int]) -> int:
    hash_map = {0: -1}
    count = max_len = 0
    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1
        if count in hash_map:
            max_len = max(max_len, i - hash_map[count])
        else:
            hash_map[count] = i

    return max_len


# Time Complexity: O(N)
# Space Complexity: O(N)

class TestFindMaxLength(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(find_max_length([]), 0)

    def test_single_element(self):
        self.assertEqual(find_max_length([0]), 0)
        self.assertEqual(find_max_length([1]), 0)

    def test_two_elements(self):
        self.assertEqual(find_max_length([0, 1]), 2)
        self.assertEqual(find_max_length([1, 1]), 0)
        self.assertEqual(find_max_length([0, 0]), 0)

    def test_multiple_elements(self):
        self.assertEqual(find_max_length([0, 1, 0]), 2)
        self.assertEqual(find_max_length([0, 1, 0, 1]), 4)
        self.assertEqual(find_max_length([1, 1, 1, 1, 1, 0, 0]), 4)
        self.assertEqual(find_max_length([0, 0, 1, 0, 0, 0, 1, 1]), 6)

    def test_all_zeros(self):
        self.assertEqual(find_max_length([0, 0, 0, 0]), 0)

    def test_all_ones(self):
        self.assertEqual(find_max_length([1, 1, 1, 1]), 0)

    def test_complex_case(self):
        self.assertEqual(find_max_length([0, 1, 1, 0, 1, 1, 1, 0]), 4)

    def test_large_array(self):
        large_array = [0, 1] * 10000  # 20000 elements
        self.assertEqual(find_max_length(large_array), 20000)


if __name__ == '__main__':
    unittest.main()
