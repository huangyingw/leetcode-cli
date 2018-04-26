#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (30.57%)
# Total Accepted:    146.3K
# Total Submissions: 478.6K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
# 
# 
# 
# Note: Do not modify the linked list.
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
