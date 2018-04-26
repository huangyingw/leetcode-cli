#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.33%)
# Total Accepted:    23.3K
# Total Submissions: 72K
# Testcase Example:  '5'
#
# 
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# 
# 
# Example 1:
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# Input: 3
# Output: False
# 
# 
# 
#
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
