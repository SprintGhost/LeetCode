#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Accepted
# 41/41 cases passed (56 ms)
# Your runtime beats 51.6 % of python3 submissions
# Your memory usage beats 54.47 % of python3 submissions (15 MB)


# A leaf node is defined as a leaf node when both left and right children are null
# When the root node‘s left && right is empty, return 1
# Returns the depth of the child node that is not empty when one of the children around the root node is empty
# When both the right node and the left child are not empty, the node value of the smaller depth of the left and right child is returned

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_list = [root.left, root.right]
        if not any(node_list):
            return 1
        # Is infinite
        min_depth = float('inf')
        for each in node_list:
            if each:
                min_depth = min(self.minDepth(each), min_depth)
        return min_depth + 1

#  from leeetcode
#  Java solution
# class Solution {
#     public int minDepth(TreeNode root) {
#         if(root == null) return 0;
#         //这道题递归条件里分为三种情况
#         //1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
#         if(root.left == null && root.right == null) return 1;
#         //2.如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度        
#         int m1 = minDepth(root.left);
#         int m2 = minDepth(root.right);
#         //这里其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回m1 + m2 + 1;
#         if(root.left == null || root.right == null) return m1 + m2 + 1;
        
#         //3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
#         return Math.min(m1,m2) + 1; 
#     }
# }

# 作者：reals
# 链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/li-jie-zhe-dao-ti-de-jie-shu-tiao-jian-by-user7208/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

