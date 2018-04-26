#
# [311] Sparse Matrix Multiplication
#
# https://leetcode.com/problems/sparse-matrix-multiplication/description/
#
# algorithms
# Medium (52.50%)
# Total Accepted:    45.7K
# Total Submissions: 87.1K
# Testcase Example:  '[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]'
#
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
#
# A = [
# ⁠ [ 1, 0, 0],
# ⁠ [-1, 0, 3]
# ]
#
# B = [
# ⁠ [ 7, 0, 0 ],
# ⁠ [ 0, 0, 0 ],
# ⁠ [ 0, 0, 1 ]
# ]
#
#
# ⁠    |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
# ⁠                 | 0 0 1 |
#
#


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
