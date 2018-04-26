#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.01%)
# Total Accepted:    116.3K
# Total Submissions: 314.3K
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Example 1:
#
#
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
#
# Example 2:
#
#
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
#


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
