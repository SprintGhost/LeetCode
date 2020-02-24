#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Accepted
# 27/27 cases passed (36 ms)
# Your runtime beats 82.89 % of python3 submissions
# Your memory usage beats 53.91 % of python3 submissions (14.4 MB)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        current = head
        while current != None:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        return pre
        
# @lc code=end

