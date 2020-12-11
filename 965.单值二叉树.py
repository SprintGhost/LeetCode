#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 72/72 cases passed (36 ms)
# Your runtime beats 87.48 % of python3 submissions
# Your memory usage beats 38.19 % of python3 submissions (13.5 MB)

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        temp = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val != temp:
                    return False
                stack.append(node.left)
                stack.append(node.right)
        return True
# @lc code=end

