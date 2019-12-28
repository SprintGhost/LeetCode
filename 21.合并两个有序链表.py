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
    def mergeTwoLists(self, l1:ListNode, l2:ListNode):
        if len(l1) == 0:
            return l2
        if len(l2) == 0:
            return l1
        index_1 = 0
        index_2 = 0
        result_list = list()
        while (True):
            if l1[index_1] < l2[index_2]:
                result_list.append(l1[index_1])
                index_1 = index_1 + 1
            elif l1[index_1] > l2[index_2]:
                result_list.append(l2[index_2])
                index_2 = index_2 + 1
            else:
                result_list.append(l2[index_2])
                index_2 = index_2 + 1
                index_1 = index_1 + 1
            if (index_1 >= len(l1)) and (index_2 < len(l2)):
                index_1 = len(l1) - 1
            elif (index_1 < len(l1)) and (index_2 >= len(l2)):
                index_2 = len(l2) - 1
            elif (index_1 >= len(l1)) and (index_2 >= len(l2)):
                break
        return result_list
A = Solution()
print (A.mergeTwoLists([1,2,4],[1,3,4]))
        
# @lc code=end

