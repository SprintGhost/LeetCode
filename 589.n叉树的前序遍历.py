#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Accepted
# 37/37 cases passed (68 ms)
# Your runtime beats 49.06 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (15.6 MB)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        if root is not None:
            stack.append(root)
        
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children[::-1])

        return result
        
# @lc code=end

