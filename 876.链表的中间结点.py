#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Accepted
# 15/15 cases passed (36 ms)
# Your runtime beats 83.78 % of python3 submissions
# Your memory usage beats 16.87 % of python3 submissions (13.4 MB)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        total_len = 0
        mid_number = 0
        temp = head
        while temp != None:
            total_len += 1
            temp = temp.next
        mid_number = total_len // 2
        temp = head
        while mid_number > 0:
            mid_number -= 1
            temp = temp.next
        return temp

# Fast && Slow ppoint solution from leet code
# Accepted
# 15/15 cases passed (32 ms)
# Your runtime beats 95.04 % of python3 submissions
# Your memory usage beats 5.81 % of python3 submissions (13.5 MB)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/solution/lian-biao-de-zhong-jian-jie-dian-by-leetcode-solut/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

