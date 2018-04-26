#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Medium (44.67%)
# Total Accepted:    51.8K
# Total Submissions: 115.9K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
#
# Given a string s and a string t, check if s is subsequence of t.
#
#
#
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short
# string (
#
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
#
# Return true.
#
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
#
# Return false.
#
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
