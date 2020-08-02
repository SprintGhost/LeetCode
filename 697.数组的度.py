#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# Accepted
# 89/89 cases passed (152 ms)
# Your runtime beats 95.78 % of python3 submissions
# Your memory usage beats 14.29 % of python3 submissions (15.4 MB)

# @lc code=start
class element:
    def __init__(self,start_index, end_index):
        self.start_index = start_index
        self.end_index = end_index
        self.count = 0
class Solution:
    def findShortestSubArray(self, nums) -> int:
        max_elemnt = -1
        max_number = -1
        max_len = 0xfffffffff
        temp = dict()
        for index, each in enumerate(nums):
            if each not in temp:
                e_element = element(index, index)
                temp[each] = e_element
            temp[each].count += 1
            temp[each].end_index = index
            if temp[each].count > max_number:
                max_number = temp[each].count
                max_elemnt = each
            elif (each != max_elemnt) and (temp[each].count == max_number):
                temp1 = len(nums[temp[max_elemnt].start_index:temp[max_elemnt].end_index + 1])
                temp2 = len(nums[temp[each].start_index:temp[each].end_index + 1])
                if temp2 < temp1:
                    max_number = temp[each].count
                    max_elemnt = each
            else:
                pass
        return len(nums[temp[max_elemnt].start_index:temp[max_elemnt].end_index + 1])

# A = Solution()

# A.findShortestSubArray([1,2,2,1,2,1,1,1,1,2,2,2])
# @lc code=end

