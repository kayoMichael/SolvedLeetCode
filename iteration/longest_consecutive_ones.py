import unittest

"""
You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
"""


def consecutive_ones(s):
    left = 0
    flip = 1
    answer = 0

    for right in range(len(s)):
        if s[right] == "0":
            flip -= 1
        while flip < 0:
            if s[left] == "0":
                flip += 1
            left += 1
        answer = max(answer, right - left + 1)

    return answer


x


# Time Complexity: O(N)
# Space Complexity: O(1)

class TestConsecutiveOnes(unittest.TestCase):
    def setUp(self) -> None:
        self.long_list = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        self.str_list = [str(x) for x in self.long_list]

    def test_consecutive_ones(self):
        self.assertEqual(consecutive_ones(["1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "0"]), 5)
        self.assertEqual(consecutive_ones(self.str_list), 6)
