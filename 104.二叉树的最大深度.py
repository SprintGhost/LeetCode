#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Accepted
# 39/39 cases passed (36 ms)
# Your runtime beats 98.86 % of python3 submissions
# Your memory usage beats 86.14 % of python3 submissions (15 MB)

class Solution:
    def tree_node(self, node):
        if node == None:
            return 0
        len = 1
        return len + max(self.tree_node(node.left), self.tree_node(node.right))
    def maxDepth(self, root: TreeNode) -> int:
        return self.tree_node(root)
# @lc code=end

