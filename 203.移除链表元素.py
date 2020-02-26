#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Accepted
# 65/65 cases passed (136 ms)
# Your runtime beats 6.32 % of python3 submissions
# Your memory usage beats 5.03 % of python3 submissions (32.4 MB)

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        while(head.val == val):
            head = head.next
            if not head:
                return head
        temp = head
        while temp.next:
            if (temp.next.val == val):
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
        
# @lc code=end

