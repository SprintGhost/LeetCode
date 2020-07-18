#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 35/35 cases passed (48 ms)
# Your runtime beats 17.01 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.7 MB)

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_second = 0xffffffffffffffff
        min_first = root.val
        stack = list()
        stack.append(root)
        while stack != []:
            root = stack.pop()
            if root != None:
                if root.val != min_first:
                    min_second = min(root.val, min_second)
                stack.append(root.right)
                stack.append(root.left)
        if min_second == 0xffffffffffffffff:
            return -1
        return min_second
        
# @lc code=end

