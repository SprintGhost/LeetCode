#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start


# Accepted
# 202/202 cases passed (76 ms)
# Your runtime beats 86.64 % of python3 submissions
# Your memory usage beats 54.96 % of python3 submissions (13.6 MB)

class Solution:
    def maxSubArray(self, nums) -> int:
        len_max = len(nums)
        if len_max == 0:
            return None
        if len_max == 1:
            return nums[0]
        max_sum = nums[0]
        tem_max = max_sum
        for index in range(1, len_max):
            tem_max = max(nums[index], tem_max + nums[index])
            max_sum = max(tem_max, max_sum)
        return max_sum



# Accepted
# 202/202 cases passed (132 ms)
# Your runtime beats 9.47 % of python3 submissions
# Your memory usage beats 74.13 % of python3 submissions (13.6 MB)

class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)

        return max_sum

# Accepted
# 202/202 cases passed (220 ms)
# Your runtime beats 5.14 % of python3 submissions
# Your memory usage beats 84.25 % of python3 submissions (13.5 MB)

class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)

A = Solution()
A.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

# @lc code=end

