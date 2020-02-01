#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# Accepted
# 17/17 cases passed (1164 ms)
# Your runtime beats 5.07 % of python3 submissions
# Your memory usage beats 60.75 % of python3 submissions (16.3 MB)

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        temp_list = list()
        while(head):
            if head in temp_list:
                return True
            temp_list.append(head)
            head = head.next
        return False

# Other method


# Accepted
# 17/17 cases passed (64 ms)
# Your runtime beats 35.01 % of python3 submissions
# Your memory usage beats 56.66 % of python3 submissions (16.4 MB)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (not head) or (not head.next):
            return False
        slow_node = head
        fast_node = head.next
        while(slow_node != fast_node):
            if (not fast_node) or (not fast_node.next):
                return False
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return True
# @lc code=end

