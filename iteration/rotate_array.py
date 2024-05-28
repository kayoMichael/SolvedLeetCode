from typing import List

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


"""

"""
Explanation: Consider the arbitrary example [-1,-100,3,99], k = 2
the perceived solution is [3, 99, -1, -100]

Notice How rotating a list to the right by k steps causes the elements to go to the front to the list which represents 
a reversal. The algorithm is follows

Rotating a element k times in the list is equivalent to
1. Reversing the entire list
2. Reversing the first k elements of the list
3. Reversing the remaining elements of the list

example:
[-1,-100,3,99] -> [99,3,-100,-1] -> [3, 99, -100, -1] -> [3, 99, -1, -100]

If k is greater than length of nums, k % length of nums is applied

exmaple:
if k = 6 -> k % 4 -> 2 which is equivalent
[-1,-100,3,99] -> [99,3,-100,-1] -> [3, 99, -100, -1] -> [3, 99, -1, -100]

"""


def rotate_array(nums: List[int], k: int) -> None:
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k %= len(nums)
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)
