#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 114/114 cases passed (40 ms)
# Your runtime beats 96.73 % of python3 submissions
# Your memory usage beats 59.06 % of python3 submissions (15 MB)


# The above Accept result is partial, 
# which is related to the test data. 
# Sometimes the test result is very poor, 
# and the runtime only beats 7.64% Coder

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if (not root):
            return False
        if not root.left and not root.right:
            return (sum - root.val) == 0
        left_bool = False
        right_bool = False
        if root.left:
            left_bool = self.hasPathSum(root.left, sum - root.val)
        if root.right:
            right_bool = self.hasPathSum(root.right, sum - root.val)
        # if not left_bool and right_bool:
        #     return right_bool
        # if not right_bool and left_bool:
        #     return left_bool
        return left_bool or right_bool


# Following from LeeetCode
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

