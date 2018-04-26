#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.22%)
# Total Accepted:    208.9K
# Total Submissions: 433.2K
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
