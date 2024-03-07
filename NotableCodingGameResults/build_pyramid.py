# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# First Podium Finish
# Time: 00:07:17
# Game Type Reverse (Determine the function from looking at the output).
# Standing. 2nd


n = int(input())
c = input()

max = 1 + 2 * (n - 1)
count = 1
for i in range(1, n + 1):
    print(" " * (max - n) + count * c)
    max -= 1
    count += 2
