"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2



Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


# Time Complexity: O(N) Since we may assume that the majority exists
# Space Complexity: O(1)

def majority_element(nums: List[int]):
    candidate = None
    count = 0

    for i in nums:
        if count == 0:
            candidate = i
        if i == candidate:
            count += 1
        else:
            count -= 1
    return candidate
