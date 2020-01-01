#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# Accepted
# 62/62 cases passed (60 ms)
# Your runtime beats 78.63 % of python3 submissions
# Your memory usage beats 95.67 % of python3 submissions (13.5 MB)
# @lc code=start
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        nums_len = len(nums)
        if (nums_len == 0):
            return 0
        start = 0
        end = nums_len - 1
        mid = nums_len // 2
        while (mid <= end) and (mid > start):
            if (target == nums[mid]):
                return mid
            elif (target > nums[mid]):
                start = mid
                mid = (end - mid) // 2 + mid
            else:
                end = mid
                mid = (start + mid) // 2
        if (start == 0) and (mid == start) and (target <= nums[start]):
            return 0
        if ((end == nums_len - 1) and (target > nums[end])) and ((mid == end) or (mid == end -1)):
            return end + 1
        return mid + 1

A = Solution()
# print (A.searchInsert([3,4,7,9,10],8))
# print (A.searchInsert([1,3,5,6],7))

# @lc code=end
