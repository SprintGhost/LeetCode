#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Accepted
# 126/126 cases passed (816 ms)
# Your runtime beats 46 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (14.6 MB)

class Solution:
    def CalPath(self, root, sum):
        if root == None:
            return 0
        sum -= root.val
        result = 1 if sum == 0 else 0
        return result + self.CalPath(root.left, sum) + self.CalPath(root.right, sum)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        return self.CalPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right,sum)
# @lc code=end

