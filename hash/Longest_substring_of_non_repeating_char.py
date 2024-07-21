import unittest

"""
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


"""


def length_of_longest_substring(s: str) -> int:
    start = max_length = 0
    index_track = {}

    for index, char in enumerate(s):
        if char in index_track and index_track.get(char) >= start:
            start = index_track[char] + 1
        else:
            max_length = max(max_length, index - start + 1)

        index_track[char] = index

    return max_length


# Time Complexity: O(N)
# Space Complexity: O(M)


class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(length_of_longest_substring(""), 0)

    def test_single_character(self):
        self.assertEqual(length_of_longest_substring("a"), 1)

    def test_all_same_characters(self):
        self.assertEqual(length_of_longest_substring("aaaa"), 1)

    def test_no_repeating_characters(self):
        self.assertEqual(length_of_longest_substring("abcde"), 5)

    def test_repeating_characters(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)

    def test_longest_at_end(self):
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)

    def test_longest_in_the_middle(self):
        self.assertEqual(length_of_longest_substring("pwwketrckew"), 6)

    def test_longest_at_beginning(self):
        self.assertEqual(length_of_longest_substring("abcdefghijklmnopqrstuvwxyzABC"), 29)
