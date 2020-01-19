#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Accepted
# 227/227 cases passed (48 ms)
# Your runtime beats 94.91 % of python3 submissions
# Your memory usage beats 77.62 % of python3 submissions (16.6 MB)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.depth(root) != -1

    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

# A = Solution()
# A.isBalanced([3,9,20,None,None,15,7])
# @lc code=end

