#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (17.16%)
# Total Accepted:    5.7K
# Total Submissions: 33.5K
# Testcase Example:  '"1"'
#
# Given an integer n, find the closest integer (not including itself), which is
# a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two
# integers.
#
# Example 1:
#
# Input: "123"
# Output: "121"
#
#
#
# Note:
#
# The input n is a positive integer represented by string, whose length will
# not exceed 18.
# If there is a tie, return the smaller one as answer.
#
#
#


class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
