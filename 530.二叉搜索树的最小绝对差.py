=#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 186/186 cases passed (60 ms)
# Your runtime beats 93.98 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (15.8 MB)

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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

