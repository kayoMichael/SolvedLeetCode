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

from functools import cache


# Top Down
def longest_common_subsequence(text1: str, text2: str) -> int:
    pointer, pointer_2 = len(text1) - 1, len(text2) - 1

    @cache
    def find_longest(pointer, pointer_2):
        if pointer < 0 or pointer_2 < 0:
            return 0
        if text1[pointer] == text2[pointer_2]:
            return 1 + find_longest(pointer - 1, pointer_2 - 1)
        else:
            return max(find_longest(pointer - 1, pointer_2), find_longest(pointer, pointer_2 - 1))

    return find_longest(pointer, pointer_2)
