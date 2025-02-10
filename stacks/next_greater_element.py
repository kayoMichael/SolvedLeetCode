"""
 Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array answer of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.



Constraints:

    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.

"""
import unittest
from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    monotonic_stack = []
    next_great = {}
    for num in nums2:
        while monotonic_stack and num > monotonic_stack[-1]:
            next_great[monotonic_stack.pop()] = num

        monotonic_stack.append(num)

    answer = [-1] * len(nums1)
    for index, num in enumerate(nums1):
        if num in next_great:
            answer[index] = next_great[num]
    return answer


# Time Complexity O(N)
# Space Complexity O(N)

class TestNextGreaterElement(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(next_greater_element([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater_element([2, 4], [1, 2, 3, 4]), [3, -1])
        self.assertEqual(next_greater_element([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]), [7, 7, 7, 7, 7])

    def test_empty(self):
        self.assertEqual(next_greater_element([], []), [])

    def test_single_element(self):
        self.assertEqual(next_greater_element([1], [1]), [-1])
        self.assertEqual(next_greater_element([2], [2]), [-1])
