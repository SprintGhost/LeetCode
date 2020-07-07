#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# Accepted
# 37/37 cases passed (64 ms)
# Your runtime beats 68.28 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (15.6 MB)

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        if root is not None:
            stack.append(root)
        
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children)

        return result[::-1]
        
# @lc code=end

