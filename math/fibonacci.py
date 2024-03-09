"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1.

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""


def fibonacci(n: int) -> int:
    cache = {}  # memoization

    def find_fib(num):
        if num in cache:
            return cache[num]
        else:
            cache[num] = num
        if num == 0:
            return 0
        if num < 2:
            return 1
        return find_fib(num - 1) + find_fib(num - 2)

    return find_fib(n)
