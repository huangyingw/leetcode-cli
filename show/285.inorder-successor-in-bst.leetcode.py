#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium (35.35%)
# Total Accepted:    59.2K
# Total Submissions: 167.4K
# Testcase Example:  '[0]\nnode with value 0'
#
# 
# Given a binary search tree and a node in it, find the in-order successor of
# that node in the BST.
# 
# 
# 
# Note: If the given node has no in-order successor in the tree, return null.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        
