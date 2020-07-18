#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# Accepted
# 36/36 cases passed (92 ms)
# Your runtime beats 87.76 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions (14.8 MB)

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        index_i = 0
        index_j = 1
        n = len(nums)
        while (index_i < n) and (index_j < n):
                if (nums[index_j] > nums[index_j - 1]):
                    index_j += 1
                else:
                    max_len = max(index_j - index_i, max_len)
                    index_i = index_j
                    index_j += 1
        
        return max(max_len, index_j - index_i)
                    

# @lc code=end

