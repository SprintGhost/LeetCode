#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#
# Accepted
# 40/40 cases passed (36 ms)
# Your runtime beats 95.79 % of python3 submissions
# Your memory usage beats 57.1 % of python3 submissions (13.4 MB)
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result1 = list()
        self.result2 = list()
    def get_child(self,root,isroot1):
        if root.right == None and root.left == None:
            if isroot1:
                self.result1.append(root.val)
            else:
                self.result2.append(root.val)
        if root.left != None:
            self.get_child(root.left,isroot1)
        if root.right != None:
            self.get_child(root.right,isroot1)


    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 != None:
            self.get_child(root1, True)
        if root2 != None:
            self.get_child(root2, False)
        return self.result1 == self.result2
        
# @lc code=end

