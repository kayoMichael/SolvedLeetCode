"""
Given a string or integer, determine if it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward,
ignoring spaces, punctuation, and capitalization.

Input: "A man, a plan, a canal, Panama!"
Output: true
Explanation: Ignoring spaces, punctuation, and capitalization, the string is a palindrome.

Input: 121
Output: true
Explanation: The number reads the same backward as forward.

Input: "hello"
Output: false
Explanation: The string is not a palindrome.



与えられた文字列または整数が回文かどうかを判断します。
回文とは、スペース、句読点、大文字小文字を無視して前後どちらから読んでも同じになる単語、フレーズ、数字、または他の文字の並びのことを指します。

Input: "A man, a plan, a canal, Panama!"
Output: true
説明: スペース、句読点、大文字小文字を無視すると、文字列は回文です。

Input: 121
Output: true
説明: 数字は前後どちらから読んでも同じです。

Input: "hello"
Output: false
説明: 文字列は回文ではありません。

"""
import unittest


def is_palindrome(word: str) -> bool:
    pointer_1 = 0
    pointer_2 = len(word) - 1
    while pointer_1 < pointer_2:
        if not word[pointer_1].isalnum():
            pointer_1 += 1
        elif not word[pointer_2].isalnum():
            pointer_2 -= 1
        elif word[pointer_1].lower() != word[pointer_2].lower():
            return False
        else:
            pointer_1 += 1
            pointer_2 -= 1
    return True


# Time Complexity: O(N)
# Space Complexity: O(1)

# Assertion Test
class TestIsPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama!"))
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("121"))
        self.assertTrue(is_palindrome("U"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertFalse(is_palindrome("Player"))


if __name__ == '__main__':
    unittest.main()
