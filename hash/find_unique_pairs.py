import unittest

"""
Given an array of integers, count the number of unique pairs of integers that have difference k. 
Input: [1, 7, 5, 9, 2, 12, 3] K=2 Output: 4 We have four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9). 
Note that we only want the number of these pairs, not the pairs themselves. 
"""


def number_of_unique_pairs_diff_k(integers: [], k: int):
    dictionary = dict()
    unique = set()

    for i in integers:
        dictionary[i] = 0

    for i in integers:
        if dictionary.get(i + k) is not None:
            unique.add((i, i + k))
        elif dictionary.get(i - k) is not None:
            unique.add((i - k, i))
    return len(unique)


# Efficient approach: First find out the number of unique elements in an array. Let the number of unique elements be x.
# Then, the number of unique pairs would be x2. This is because each unique element can
# form a pair with every other unique element including itself.
def number_of_unique_pairs(integers: []):
    unique = set()
    for i in integers:
        unique.add(i)
    return len(unique) ^ 2


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def number_of_unique_pairs_unordered(integers: []):
    unique = set()
    for i in integers:
        unique.add(i)
    return factorial(len(unique))


class TestUnique(unittest.TestCase):
    def test_unique_pairs_k_diff(self):
        self.assertEqual(number_of_unique_pairs_diff_k([3, 2, 5, 8, 3, 2], 2), 1)
        self.assertEqual(number_of_unique_pairs_diff_k([3, 2, 5, 8, 3, 2], 1), 1)
        self.assertEqual(number_of_unique_pairs_diff_k([3, 2, 5, 8, 3, 2], 3), 2)
        self.assertEqual(number_of_unique_pairs_diff_k([3, 6, 9, 12, 15], 3), 4)
        self.assertEqual(number_of_unique_pairs_diff_k([3, 2, 5, 8, 3, 2], 10), 0)
        self.assertEqual(number_of_unique_pairs_diff_k([], 5), 0)
        self.assertEqual(number_of_unique_pairs_diff_k([], 0), 0)
        self.assertEqual(number_of_unique_pairs_diff_k([2, 2, 2, 2, 2], 0), 1)
        self.assertEqual(number_of_unique_pairs_diff_k([2, 3], 1), 1)

    def text_number_of_unique_pairs(self):
        self.assertEqual(number_of_unique_pairs([2, 3, 4, 5, 6]), 25)
        self.assertEqual(number_of_unique_pairs([3, 5, 10]), 9)
        self.assertEqual(number_of_unique_pairs([3]), 1)
        self.assertEqual(number_of_unique_pairs([3, 3, 2, 1, 5, 4, 3, 2]), 25)

    def text_number_of_unqiue_pairs_unordered(self):
        self.assertEqual(number_of_unique_pairs_unordered([2, 3, 4, 5, 6], ))


if __name__ == '__main__':
    unittest.TestCase()
