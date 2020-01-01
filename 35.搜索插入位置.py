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

# A = Solution()
# print (A.searchInsert([3,4,7,9,10],8))
# print (A.searchInsert([1,3,5,6],7)


# Accepted
# 62/62 cases passed (52 ms)
# Your runtime beats 95.91 % of python3 submissions
# Your memory usage beats 97.58 % of python3 submissions (13.5 MB)
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        # 返回大于等于 target 的索引，有可能是最后一个
        size = len(nums)
        # 特判
        if size == 0:
            return 0

        left = 0
        # 如果 target 比 nums里所有的数都大，则最后一个数的索引 + 1 就是候选值，因此，右边界应该是数组的长度
        right = size
        # 二分的逻辑一定要写对，否则会出现死循环或者数组下标越界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                assert nums[mid] >= target
                # [1,5,7] 2
                right = mid
        # 调试语句
        # print('left = {}, right = {}, mid = {}'.format(left, right, mid))
        return left


# @lc code=end
