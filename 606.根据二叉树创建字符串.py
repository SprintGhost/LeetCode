#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 162/162 cases passed (60 ms)
# Your runtime beats 88.33 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (15.5 MB)

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        if (not t.left and not t.right):
            return str(t.val) + ""
        if not t.right:
            return str(t.val) +"(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) +')(' + self.tree2str(t.right) + ')'

        
# @lc code=end

