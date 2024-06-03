import unittest
from functools import lru_cache

"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""


def longest_subsequence_top_down(text1: str, text2: str) -> int:
    @lru_cache(maxsize=None)
    def find_subsequence(t1, t2):
        if t1 == len(text1) or t2 == len(text2):
            return 0

        if text1[t1] == text2[t2]:
            return 1 + find_subsequence(t1 + 1, t2 + 1)

        return max(find_subsequence(t1 + 1, t2), find_subsequence(t1, t2 + 1))

    return find_subsequence(0, 0)


# Time Complexity: O(M * N) where M is the length of text1 and N is the length of text2
# Space Complexity: O(M * N)

def longest_subsequence_bottom_up(text1: str, text2: str) -> int:
    if len(text2) < len(text1):
        text1, text2 = text2, text1

    previous = [0] * (len(text1) + 1)
    for col in reversed(range(len(text2))):
        current = [0] * (len(text1) + 1)
        for row in reversed(range(len(text1))):
            if text2[col] == text1[row]:
                current[row] = 1 + previous[row + 1]
            else:
                current[row] = max(previous[row], current[row + 1])
        previous = current

    return previous[0]


# Time Complexity: O(M * N) where M is the length of text1 and N is the length of text2
# Space Complexity: O(min(N, M))


class TestCommonSubsequence(unittest.TestCase):
    def test_common_subsequence(self):
        self.assertEqual(longest_subsequence_top_down(text1="abcde", text2="ace"), 3)
        self.assertEqual(longest_subsequence_top_down(text1="abc", text2="abc"), 3)
        self.assertEqual(longest_subsequence_top_down(text1="abc", text2="def"), 0)
        self.assertEqual(longest_subsequence_bottom_up(text1="abcde", text2="ace"), 3)
        self.assertEqual(longest_subsequence_bottom_up(text1="abc", text2="abc"), 3)
        self.assertEqual(longest_subsequence_bottom_up(text1="abc", text2="def"), 0)
