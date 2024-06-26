import unittest

"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.



Example 1:

Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:

Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive.

Example 3:

Input: nums = [1,-2,-3]
Output: 5



Constraints:

    1 <= nums.length <= 100
    -100 <= nums[i] <= 100


"""


def minimum_start_value(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    target = min(prefix)

    if target >= 0:
        return 1
    else:
        return abs(target) + 1


# Time Complexity: O(N)
# Space Complexity: O(N)

def minimum_start_value_optimized(nums):
    min_value = nums[0]
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
        min_value = min(nums[i], min_value)

    if min_value < 0:
        return abs(min_value) + 1
    else:
        return 1


# Time Complexity: O(N)
# Space Complexity: O(1)


class TestMinimumStartValue(unittest.TestCase):
    def test_consecutive_ones(self):
        self.assertEqual(minimum_start_value([-3, 2, -3, 4, 2]), 5)
        self.assertEqual(minimum_start_value([1, -2, -3]), 5)
        self.assertEqual(minimum_start_value([1, 2, 3, 4, 5]), 1)
        self.assertEqual(minimum_start_value_optimized([-3, 2, -3, 4, 2]), 5)
        self.assertEqual(minimum_start_value_optimized([1, -2, -3]), 5)
        self.assertEqual(minimum_start_value_optimized([1, 2, 3, 4, 5]), 1)
