#
# [562] Longest Line of Consecutive One in Matrix
#
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
#
# algorithms
# Medium (41.28%)
# Total Accepted:    7.1K
# Total Submissions: 17.2K
# Testcase Example:  '[[0,1,1,0],[0,1,1,0],[0,0,0,1]]'
#
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# Example:
#
# Input:
# [[0,1,1,0],
# ⁠[0,1,1,0],
# ⁠[0,0,0,1]]
# Output: 3
#
#
#
#
# Hint:
# The number of elements in the given matrix will not exceed 10,000.
#
#


class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
