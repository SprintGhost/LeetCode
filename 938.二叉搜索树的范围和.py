#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Accepted
# 41/41 cases passed (392 ms)
# Your runtime beats 5.39 % of python3 submissions
# Your memory usage beats 14.82 % of python3 submissions (21.7 MB)

# Accepted
# 41/41 cases passed (224 ms)
# Your runtime beats 89.12 % of python3 submissions
# Your memory usage beats 17.2 % of python3 submissions (21.7 MB)
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                if low <= node.val <= high:
                    result += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return result

# @lc code=end

