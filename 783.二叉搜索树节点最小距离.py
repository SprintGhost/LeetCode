#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Accepted
# 45/45 cases passed (44 ms)
# Your runtime beats 60.16 % of python3 submissions
# Your memory usage beats 48.97 % of python3 submissions (13.7 MB)
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        pre,res= float('inf'),float('inf')
        def f(r):
            nonlocal pre,res
            if r:
                f(r.left)
                res = min(res,abs(r.val - pre))
                pre = r.val
                f(r.right)
        f(root)
        return res
# @lc code=end

