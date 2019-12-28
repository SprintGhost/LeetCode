#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        Head = ListNode(0)
        result_list = ListNode(0)
        Head.next = result_list
        while (True):
            if l1.val< l2.val:
                result_list.val = l1.val
                if (l1.next != None):
                    l1 = l1.next
            elif l1.val > l2.val:
                result_list.val = l1.val
                if (l2.next != None):
                    l2 = l2.next
            else:
                result_list.val = l1.val
                result_list.next = ListNode(0)
                result_list = result_list.next
                result_list.val = l1.val
                if (l1.next != None):
                    l1 = l1.next
                if (l2.next != None):
                    l2 = l2.next
            if (l1.next == None) and (l2.next == None):
                break
            result_list.next = ListNode(0)
            result_list = result_list.next
        return Head.next
# A = Solution()
# print (A.mergeTwoLists([1,2,4],[1,3,4]))
        
# @lc code=end

