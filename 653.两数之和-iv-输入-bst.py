#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 421/421 cases passed (96 ms)
# Your runtime beats 72.05 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (15.7 MB)

class Solution:
    def __init__(self):
        self.list = list()

    def bst2list(self,root):
        if not root:
            return None
        self.bst2list(root.left)
        self.list.append(root.val)
        self.bst2list(root.right)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.bst2list(root)
        head = 0
        end = len(self.list) - 1
        while(head < end):
            sum = self.list[head] + self.list[end]
            if (sum == k):
                return True
            if (sum < k):
                head += 1
            else:
                end -= 1
        return False
        
# @lc code=end

