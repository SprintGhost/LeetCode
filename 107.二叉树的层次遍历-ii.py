#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Accepted
# 34/34 cases passed (32 ms)
# Your runtime beats 97.24 % of python3 submissions
# Your memory usage beats 73.43 % of python3 submissions (13.3 MB)

class Solution:
    def levelOrderBottom(self, root):
        # result list
        queue = [] 
        # next node                                              
        cur = [root]                        
        while cur:
            # init current node value                                                  
            cur_layer_val = []
            # init next loop node list                                      
            next_layer_node = []
            # foreach each node                                     
            for node in cur:                                        
                if node:                                           
                    cur_layer_val.append(node.val)
                    # add cueernt right && left node to next loop                  
                    next_layer_node.extend([node.left, node.right]) 
            if cur_layer_val:                                       
                queue.insert(0, cur_layer_val)                     
            cur = next_layer_node                                   
        return queue                                                


# @lc code=end

