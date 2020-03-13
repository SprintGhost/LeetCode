#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 68/68 cases passed (56 ms)
# Your runtime beats 7.8 % of python3 submissions
# Your memory usage beats 26.75 % of python3 submissions (13.2 MB)
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
# @lc code=end

