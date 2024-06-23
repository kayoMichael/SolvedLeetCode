import unittest

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


def sort_list_by_absolute_value(nums):
    length = len(nums)
    result = [0] * length
    left = 0
    right = length - 1
    for i in range(length - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            square = nums[left]
            left += 1
        else:
            square = nums[right]
            right -= 1
        result[i] = square * square
    return result


class TestSortListByAbsolute(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort_list_by_absolute_value([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(sort_list_by_absolute_value([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])
        self.assertEqual(sort_list_by_absolute_value([-10, -9, -8, -7]), [49, 64, 81, 100])
        self.assertEqual(sort_list_by_absolute_value([7, 8, 9, 10]), [49, 64, 81, 100])


if __name__ == '__main__':
    unittest.main()
