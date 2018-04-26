#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (38.60%)
# Total Accepted:    39.2K
# Total Submissions: 101.5K
# Testcase Example:  '"eceba"\n2'
#
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
#
#
#
# For example,
#
# Given s = “eceba” and k = 2,
#
#
#
# T is "ece" which its length is 3.
#
#


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
