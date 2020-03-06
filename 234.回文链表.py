#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Accepted
# 26/26 cases passed (80 ms)
# Your runtime beats 55.53 % of python3 submissions
# Your memory usage beats 23.85 % of python3 submissions (23.8 MB)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp_list = list()
        while head:
            temp_list.append(head.val)
            head = head.next
        return (temp_list == temp_list[::-1])

# Accepted
# 26/26 cases passed (88 ms)
# Your runtime beats 38.25 % of python3 submissions
# Your memory usage beats 24.08 % of python3 submissions (23.5 MB)

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/palindrome-linked-list/solution/hui-wen-lian-biao-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# data = ListNode(0)
# data1 = ListNode(0)
# data.next = data1
# A = Solution()
# print (A.isPalindrome(data))      

        
# @lc code=end

