#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (24.92%)
# Total Accepted:    81.4K
# Total Submissions: 326.8K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
#
#
#


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
