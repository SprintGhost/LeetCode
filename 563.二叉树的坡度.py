#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 75/75 cases passed (92 ms)
# Your runtime beats 29.17 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (15.6 MB)

class Solution:
    def __init__(self):
        self.sum = 0
    def node(self,node):
        if not node:
            return 0
        right = self.node(node.right)
        left = self.node(node.left)
        self.sum += abs(right - left)
        return right + left + node.val
    def findTilt(self, root: TreeNode) -> int:
        self.node(root)
        return self.sum

#    [1,2,3,4,null,5]     
# @lc code=end

