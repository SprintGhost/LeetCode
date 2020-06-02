#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 106/106 cases passed (60 ms)
# Your runtime beats 51.36 % of python3 submissions
# Your memory usage beats 22.22 % of python3 submissions (15.5 MB)

class Solution:
    def __init__(self):
        self.max = 0
    def depth(self,root):
        if root == None:
            return 0
        right_dep = self.depth(root.right) 
        left_dep = self.depth(root.left) 
        self.max = max(right_dep + left_dep, self.max)
        return max(right_dep, left_dep) + 1
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.max
        
# @lc code=end

