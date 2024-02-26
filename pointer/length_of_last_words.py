"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

"""
与えられた文字列sが単語と空白から構成されている場合、文字列内の最後の単語の長さを返します。

単語は、非空白文字のみから成る最大の部分文字列です。

例1：

入力：s = "Hello World"
出力：5
説明：最後の単語は "World" で、長さは5です。

例2：

入力：s = " fly me to the moon "
出力：4
説明：最後の単語は "moon" で、長さは4です。

例3：

入力：s = "luffy is still joyboy"
出力：6
説明：最後の単語は "joyboy" で、長さは6です。
"""
import unittest


def length_of_last_word(s) -> int:
    """
    :type s: str
    :rtype: int
    """
    word = s.strip()
    i = len(word) - 1
    counter = 0
    while i >= 0:
        if word[i] == ' ':
            break
        counter += 1
        i -= 1
    return counter

# Time Complexity: O(N)
# Space Complexity: O(N)


class TestLengthOfLastWord(unittest.TestCase):
    def test_LastWordLength(self):
        self.assertEqual(length_of_last_word('a'), 1)
        self.assertEqual(length_of_last_word('Hello My Name'), 4)
        self.assertEqual(length_of_last_word('Onomatopoeia'), 12)
        self.assertEqual(length_of_last_word('pleased to meet you    '), 3)


if __name__ == '__main__':
    unittest.main()
