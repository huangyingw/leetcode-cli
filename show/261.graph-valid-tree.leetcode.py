#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (38.45%)
# Total Accepted:    55.6K
# Total Submissions: 144.5K
# Testcase Example:  '5\n[[0,1],[0,2],[2,3],[2,4]]'
#
# 
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to check whether these edges make
# up a valid tree.
# 
# 
# 
# For example:
# 
# 
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# 
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return
# false.
# 
# 
# 
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
# 
#
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
