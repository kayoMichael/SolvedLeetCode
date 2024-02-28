import unittest


def first_non_repeat(word: str):
    dictionary = {}
    first = ''
    for i in word:
        if i == " ":
            continue
        elif dictionary.get(i.lower()) is None:
            dictionary[i.lower()] = 0
        dictionary[i.lower()] += 1

    for i in dictionary:
        if dictionary[i] == 1:
            first = i
            break

    return first


def first_non_repeat_set(word: str):
    original = set()
    repeated = []
    first = ''
    for i in word:
        length = len(original)
        original.add(i.lower())
        if len(original) == length:
            repeated.append(i.lower())

    for i in word:
        if i.lower() not in repeated:
            first = i.lower()
            break

    return first


# Time Complexity: O(N)
# Space Complexity: O(N)


# Assertion Test
class TestFirstNonRepeating(unittest.TestCase):
    def test_non_repeat(self):
        self.assertEqual(first_non_repeat('A Green Apple'), 'g')
        self.assertEqual(first_non_repeat('AB'), 'a')
        self.assertEqual(first_non_repeat('Tc soiqkmdsoqwd tcsoq e'), 'i')
        self.assertEqual(first_non_repeat('teksamet'), 'k')
        self.assertEqual(first_non_repeat(''), '')

    def test_non_repeat_set(self):
        self.assertEqual(first_non_repeat_set('A Green Apple'), 'g')
        self.assertEqual(first_non_repeat_set('AB'), 'a')
        self.assertEqual(first_non_repeat_set('Tc soiqkmdsoqwd tcsoq e'), 'i')
        self.assertEqual(first_non_repeat_set('teksamet'), 'k')
        self.assertEqual(first_non_repeat_set(''), '')


if __name__ == '__main__':
    unittest.main()
