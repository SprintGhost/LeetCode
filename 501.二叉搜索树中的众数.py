#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.curTimes = 1
        self.maxTimes = 0
        self.res = list()
    def inOrder(self, root, pre):
        if (not root):
            return
        self.inOrder(root.left, pre)
        if (pre):
            if root.val == pre.val:
                self.curTimes += 1
            else:
                self.curTimes = 1  
        if (self.curTimes == self.maxTimes):
            self.res.append(root.val)
        elif (self.curTimes > self.maxTimes):
            self.res = list()
            self.res.append(root.val)
            self.maxTimes = self.curTimes
        self.inOrder(root.right, root)

    def findMode(self, root: TreeNode):
        if (not root):
            return None
        pre = None
        self.inOrder(root, pre)
        return self.res

T = TreeNode(1)
T_left = TreeNode(1)
T.left = T_left

A = Solution()
A.findMode(T)

      
# @lc code=end

