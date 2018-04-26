#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Hard (42.89%)
# Total Accepted:    37.6K
# Total Submissions: 87.7K
# Testcase Example:  '"eceba"'
#
# Given a string s , find the length of the longest substring t  that contains
# at most 2 distinct characters.
#
# Example 1:
#
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
#
#
# Example 2:
#
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
#
#
#


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
