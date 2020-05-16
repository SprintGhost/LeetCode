#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# Accepted
# 25/25 cases passed (72 ms)
# Your runtime beats 59.49 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (17.6 MB)

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = [root]  
        d = {} 
        while queue:
            node = queue.pop(0)

            if node.val not in d:
                d[node.val] = 1
            else:
                d[node.val] +=1

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        m = max(d.values())
        l = []
        for k,v in d.items():
            if v == m:
                l.append(k)
        return l

# 作者：guo-guo-69
# 链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/cai-niao-ti-jie-by-guo-guo-69/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 


      
# @lc code=end

