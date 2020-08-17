#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# Accepted
# 46/46 cases passed (368 ms)
# Your runtime beats 11.44 % of python3 submissions
# Your memory usage beats 62.66 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        else:
            return nums.index(target)

# Accepted
# 46/46 cases passed (324 ms)
# Your runtime beats 38.86 % of python3 submissions
# Your memory usage beats 15.88 % of python3 submissions (15.1 MB)
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            elif (nums[mid] == target):
                right = mid - 1
            else:
                pass
        if (left >= len(nums) or nums[left] != target):
            return -1
        return left

        
# @lc code=end

