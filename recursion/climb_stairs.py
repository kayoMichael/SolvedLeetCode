"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


# Time Complexity O(N) due to memoization
# Space Complexity O(N)


def climb_stairs(n):
    cache = {}

    def helper(n, memo):
        if n == 0 or n == 1:
            return 1
        if n in memo:
            return memo[n]

        memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        return memo[n]

    return helper(n, cache)

