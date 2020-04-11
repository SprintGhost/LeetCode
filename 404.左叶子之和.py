#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 102/102 cases passed (44 ms)
# Your runtime beats 47.57 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions (14.4 MB)

class Solution:
    def add_each_left(self, right, left):
        temp = 0
        if left != None:
            temp += self.add_each_left(left.right, left.left)
        if right != None:
            temp += self.add_each_left(right.right, right.left)
        if (left != None) and (left.left == None) and (left.right == None):
            temp += left.val
        return temp


    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return self.add_each_left(root.right,root.left)


# [0,2,4,1,null,3,-1,5,1,null,6,null,8]
# @lc code=end

