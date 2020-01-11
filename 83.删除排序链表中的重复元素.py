#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Accepted
# 165/165 cases passed (48 ms)
# Your runtime beats 71.55 % of python3 submissions
# Your memory usage beats 5.01 % of python3 submissions (13.3 MB)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head == None):
            return None
        temp = head
        while(temp.next != None):
            next = temp.next
            if (temp.val == next.val):
                temp.next = next.next
            else:
                temp = temp.next
        return head
# @lc code=end

