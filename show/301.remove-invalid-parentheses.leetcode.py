#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (35.86%)
# Total Accepted:    68K
# Total Submissions: 189.5K
# Testcase Example:  '"()())()"'
#
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and
# ).
#
#
#
# Examples:
#
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
#
#
#
# Credits:Special thanks to @hpplayer for adding this problem and creating all
# test cases.
#


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
