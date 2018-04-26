#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (41.41%)
# Total Accepted:    157.6K
# Total Submissions: 380.7K
# Testcase Example:  '[1,2,3,null,5]'
#
#
# Given a binary tree, return all root-to-leaf paths.
#
#
# For example, given the following binary tree:
#
#
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
#
#
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
