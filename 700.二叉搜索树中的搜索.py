#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 36/36 cases passed (88 ms)
# Your runtime beats 89.5 % of python3 submissions
# Your memory usage beats 13.86 % of python3 submissions (15.9 MB)

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or root.val == val:
            return root
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)


        
# @lc code=end

