"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""
from collections import defaultdict
from functools import cache
from typing import List


# Bottom Up
def delete_and_earn(nums: List[int]) -> int:
    max_number = 0
    max_points = defaultdict(int)

    for i in nums:
        max_points[i] += i
        max_number = max(max_number, max_points[i])

    arr = [0] * (max_number + 1)
    arr[0] = 0
    arr[1] = max_points[1]

    for i in range(2, len(arr)):
        arr[i] = max(max_points[i] + arr[i - 2], arr[i - 1])
    return arr[-1]


# top down
def delete_and_earn_2(nums: List[int]) -> int:
    max_number = 0
    max_points = defaultdict(int)

    for i in nums:
        max_points[i] += i
        max_number = max(max_number, max_points[i])

    @cache
    def helper(nums):
        if i == 0:
            return 0
        if i == 1:
            return max_points[1]

        return max(max_points[nums] + helper(nums - 2), helper(nums - 1))
