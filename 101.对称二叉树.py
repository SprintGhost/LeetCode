#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Accepted
# 195/195 cases passed (24 ms)
# Your runtime beats 99.65 % of python3 submissions
# Your memory usage beats 84.37 % of python3 submissions (13.1 MB)

class Solution:
    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.compare(root.left, root.right)
# @lc code=end

