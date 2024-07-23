import unittest
from typing import List


def counting_sort(arr: List[int]):
    if not arr:
        return []
    
    max_value = max(arr)

    auxiliary_list = [0] * (max_value + 1)

    for num in arr:
        auxiliary_list[num] += 1

    sorted_list = []
    for x in range(len(auxiliary_list)):
        count = auxiliary_list[x]
        if count > 0:
            sorted_list.extend([x] * count)

    return sorted_list


# Time Complexity: O(N + M) Where N is the length of list to sort and M is the maximum value + 1 in the list.
# Space Complexity: O(M)


class TestCountingSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_single_element(self):
        self.assertEqual(counting_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(counting_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(counting_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(counting_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8])

    def test_list_with_zeros(self):
        self.assertEqual(counting_sort([0, 3, 0, 2, 1, 0]), [0, 0, 0, 1, 2, 3])

    def test_list_with_large_numbers(self):
        self.assertEqual(counting_sort([1000, 1, 10, 100]), [1, 10, 100, 1000])

    def test_stability(self):
        input_list = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
        sorted_list = counting_sort([x[0] for x in input_list])
        self.assertEqual(sorted_list, [1, 1, 2, 2])


if __name__ == '__main__':
    unittest.main()
