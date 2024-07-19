import unittest
from collections import defaultdict
from typing import List

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.


"""


def group_anagrams(strs: List[str]):
    string_count = defaultdict(list)
    for word in strs:
        string_count[sorted(word)].append(word)

    return list(string_count.values())


# Time Complexity: O(NKlogK) Where N is the length of strs and K is the length of each string
# Space Complexity: O(NK) where N is the number of entries in string_count and K is the length of each string


def group_anagrams_v2(strs: List[str]):
    string_count = defaultdict(list)

    for word in strs:
        ascii_history = [0] * 26
        for char in word:
            ascii_history[ord(char) - ord("a")] += 1

        string_count[tuple(ascii_history)].append(word)
    return list(string_count.values())


# Time Complexity: O(NK) where N is the length of strs and K is the length of each word
# Space Complexity: O(NK) where N is the number of entries in string_count and K is the length of each string

class TestGroupAnagrams(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(group_anagrams_v2([]), [])

    def test_single_word(self):
        self.assertEqual(group_anagrams_v2(["hello"]), [["hello"]])

    def test_no_anagrams(self):
        input = ["cat", "dog", "bird"]
        output = group_anagrams_v2(input)
        self.assertEqual(len(output), 3)
        self.assertIn(["cat"], output)
        self.assertIn(["dog"], output)
        self.assertIn(["bird"], output)

    def test_simple_anagrams(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = group_anagrams_v2(input)
        self.assertEqual(len(output), 3)
        self.assertIn(["eat", "tea", "ate"], output)
        self.assertIn(["tan", "nat"], output)
        self.assertIn(["bat"], output)

    def test_anagrams_with_repeating_letters(self):
        input = ["boo", "bob", "obo"]
        output = group_anagrams_v2(input)
        self.assertEqual(len(output), 2)
        self.assertIn(["boo", "obo"], output)
        self.assertIn(["bob"], output)

    def test_words_with_spaces(self):
        input = ["abc", "cba", "def"]
        output = group_anagrams_v2(input)
        self.assertEqual(len(output), 2)
        self.assertIn(["abc", "cba"], output)
        self.assertIn(["def"], output)

    def test_large_input(self):
        input = ["a"] * 10000 + ["b"] * 10000
        output = group_anagrams_v2(input)
        self.assertEqual(len(output), 2)
        self.assertIn(["a"] * 10000, output)
        self.assertIn(["b"] * 10000, output)


if __name__ == '__main__':
    unittest.main()
