#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (44.06%)
# Total Accepted:    22.4K
# Total Submissions: 50.8K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.
# 
# 
# For example:
# Given binary tree,
# 
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
# 
# 
# 
# return 4.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
