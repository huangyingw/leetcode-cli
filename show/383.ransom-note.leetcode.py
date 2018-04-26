#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (47.84%)
# Total Accepted:    78.6K
# Total Submissions: 164.3K
# Testcase Example:  '"a"\n"b"'
#
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
#
#
# Each letter in the magazine string can only be used once in your ransom
# note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
