"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]
"""


def find_row(self, row_index: int):
    if row_index == 0:
        return [1]
    elif row_index == 1:
        return [1, 1]

    previous = find_row(row_index - 1)
    current = [1]

    for i in range(1, row_index):
        current.append(previous[i - 1] + previous[i])

    current.append(1)

    return current
