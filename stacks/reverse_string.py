from stacks import Stack
import unittest


# two pointer method
def reverse_string_pointer(word):
    word_list = list(word)
    start_index = 0
    end_index = len(word_list) - 1
    while start_index < end_index:
        word_list[start_index], word_list[end_index] = word_list[end_index], word_list[start_index]
        start_index += 1
        end_index -= 1
    return ''.join(word_list)


# Stack Method
def reverse_string_stack(word):
    reverse = Stack()
    reverse_word = []  # Since string is immutable in python, it is better to set reverse_word as a list and then append
    for i in word:
        reverse.push(i)

    while not reverse.is_empty():
        reverse_word.append(reverse.pop())

    return ''.join(reverse_word)


class TestReverseWord(unittest.TestCase):
    def test_reverse_string_pointer(self):
        self.assertEqual(reverse_string_pointer("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string_pointer(""), "")
        self.assertEqual(reverse_string_pointer("killik"), "killik")


class TestReverseWordStack(unittest.TestCase):
    def test_reverse_string_stack(self):
        self.assertEqual(reverse_string_stack("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string_stack(""), "")
        self.assertEqual(reverse_string_stack("killik"), "killik")


if __name__ == '__main__':
    unittest.main()







