#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (41.16%)
# Total Accepted:    100.9K
# Total Submissions: 245.1K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
#


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
