#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (27.22%)
# Total Accepted:    38.4K
# Total Submissions: 140.9K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
#
# ⁠   Given a list of unique words, find all pairs of distinct indices (i, j)
# in the given list, so that the concatenation of the two words, i.e. words[i]
# + words[j] is a palindrome.
#
#
#
# ⁠   Example 1:
# ⁠   Given words = ["bat", "tab", "cat"]
# ⁠   Return [[0, 1], [1, 0]]
# ⁠   The palindromes are ["battab", "tabbat"]
#
#
# ⁠   Example 2:
# ⁠   Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# ⁠   Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# ⁠   The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
