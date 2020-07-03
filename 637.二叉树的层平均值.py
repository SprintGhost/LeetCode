#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 65/65 cases passed (64 ms)
# Your runtime beats 66.93 % of python3 submissions
# Your memory usage beats 16.67 % of python3 submissions (16.4 MB)

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        count = list()
        res = list()
        self.average(root, 0, res, count)
        for index, each in enumerate(res):
            res[index] = res[index]/ count[index]
        return res
    
    def average(self, t, i, sum, count):
        if (t == None):
            return
        if (i < len(sum)):
            sum[i] = sum[i] + t.val
            count[i] = count[i] + 1
        else:
            sum.append(1.0 * t.val)
            count.append(1)
        self.average(t.left, i + 1, sum, count)
        self.average(t.right, i + 1, sum, count)

        
# @lc code=end

