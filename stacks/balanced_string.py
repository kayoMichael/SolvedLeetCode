import unittest

from stacks import Stack


# Stack Method
def balanced_string(word):
    bracket_library = {"{": "}", "(": ")", "[": "]"}
    stack = Stack()
    k = list(word)
    nextBracket = None
    for i in k:
        if i == "{" or i == "(" or i == "[":
            stack.push(i)
        elif i == ")" or i == "]" or i == "}":
            if stack.is_empty():
                return False
            open_bracket = stack.pop()
            if bracket_library.get(open_bracket) != i:
                return False

    return stack.is_empty()


# Time Complexity: O(N)
# Space Complexity: O(N)

class TestBalancedString(unittest.TestCase):
    def test_reverse_string_pointer(self):
        self.assertTrue(balanced_string("([])"))
        self.assertTrue(balanced_string("([Heeeee])"))
        self.assertTrue(balanced_string("(dqwoudhqwo)"))
        self.assertTrue(balanced_string("()"))
        self.assertFalse(balanced_string("[])()"))
        self.assertFalse(balanced_string("("))
        self.assertFalse(balanced_string(")"))
        self.assertFalse(balanced_string("[EOijwdowid]()[]{]"))


if __name__ == '__main__':
    unittest.main()
