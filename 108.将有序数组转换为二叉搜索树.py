#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 32/32 cases passed (52 ms)
# Your runtime beats 99.78 % of python3 submissions
# Your memory usage beats 63 % of python3 submissions (15.2 MB)

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid+1:]
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)

        return node


# @lc code=end

