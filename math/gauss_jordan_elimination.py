"""
Given a R^m*n matrix where m and n are integers, transform the matrix into its Reduced Row-echelon form. Then Calculate 
its Null space, nullity, Range and Rank. Then verify the solution using the rank-nullity theorem.

input:     
[1 2 3]   
[0 3 2]
[1 2 0]    

output:
[1 0 0]   
[0 1 0]
[0 0 1]

Rank: 3
Nullity: 0
Range: 3

rank-nullity theorem: 3 + 0 = number of columns    

"""

"""
与えられた m 行 n 列の行列 R^m*n において、こちらの行列をその簡約行列形式に変換します。その後、ヌル空間、ヌル度、範囲、およびランクを計算します。
最後に、ランク-ヌル度定理を使用して解を検証します

入力:     
[1 2 3|1]
[1 3 2|2]
[0 2 0|3] 

出力:
[1 0 0]   
[0 1 0]
[0 0 1]

ランク: 3
ヌル度: 0

rank-nullity theorem: 3 + 0 = number of columns   
"""

import unittest

k = [[1, 2, 4], [1, 2, 1], [0, 2, 3]]


# Three Elementary Row Operations

# R_index_1 <-> R_index_2
def row_swap(matrix: list, index_1: int, index_2: int):
    matrix[index_1], matrix[index_2] = matrix[index_2], matrix[index_1]


# R_index = R_index * x where x is any real number
def row_multiply(matrix: list, index: int, multiple: float):
    matrix[index] = [element * multiple for element in matrix[index]]


# R_index_2 = R_index_1 * multiple + R_index_2
def row_addition(matrix: list, index_1: int, index_2: int, multiple: int):
    new_matrix = matrix.copy()
    row_multiply(new_matrix, index_1, multiple)
    matrix[index_2] = [element + new_matrix[index_1][index] for index, element in enumerate(matrix[index_2])]


def gauss_jordan_elimination(matrix: list, answer: list):
    pass

