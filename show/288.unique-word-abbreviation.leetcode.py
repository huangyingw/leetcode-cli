#
# [288] Unique Word Abbreviation
#
# https://leetcode.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (18.00%)
# Total Accepted:    32.4K
# Total Submissions: 180.3K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# An abbreviation of a word follows the form <first letter><number><last
# letter>. Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
# ⁠    1
# b) d|o|g                   --> d1g
#
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
#
# ⁠             1
# ⁠    1---5----0
# d) l|ocalizatio|n          --> l10n
#
#
# Assume you have a dictionary and given a word, find whether its abbreviation
# is unique in the dictionary. A word's abbreviation is unique if no other word
# from the dictionary has the same abbreviation.
#
# Example:
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
#
#
#


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
