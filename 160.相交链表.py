#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#  I can't find a good sulution, the following solution from leetcode
# Accepted
# 45/45 cases passed (304 ms)
# Your runtime beats 5.1 % of python3 submissions
# Your memory usage beats 29.52 % of python3 submissions (28.4 MB)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA == None or headB == None):
            return None
        pA = headA
        pB = headB
        while (pA != pB):
            pA = headB if (pA == None) else pA.next
            pB = headA if (pB == None) else pB.next
        return pA

# 作者：reals
# 链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/tu-jie-xiang-jiao-lian-biao-by-user7208t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

