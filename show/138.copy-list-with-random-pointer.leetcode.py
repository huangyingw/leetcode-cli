#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.81%)
# Total Accepted:    154.2K
# Total Submissions: 597.4K
# Testcase Example:  '{}'
#
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
#
#
#
# Return a deep copy of the list.
#
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
