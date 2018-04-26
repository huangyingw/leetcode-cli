#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (40.92%)
# Total Accepted:    5.9K
# Total Submissions: 14.4K
# Testcase Example:  '10'
#
#
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
#
#
# Example 1:
#
# Input: N = 10
# Output: 9
#
#
#
# Example 2:
#
# Input: N = 1234
# Output: 1234
#
#
#
# Example 3:
#
# Input: N = 332
# Output: 299
#
#
#
# Note:
# N is an integer in the range [0, 10^9].
#
#


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
