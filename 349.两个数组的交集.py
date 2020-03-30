#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# Accepted
# 60/60 cases passed (120 ms)
# Your runtime beats 8.61 % of python3 submissions
# Your memory usage beats 5.65 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        for each in nums1:
            if each in nums2 and each not in result:
                result.append(each)
        return result
# Accepted
# 60/60 cases passed (120 ms)
# Your runtime beats 8.61 % of python3 submissions
# Your memory usage beats 5.65 % of python3 submissions (13.7 MB)
        return list(set(nums1) & set(nums2))
        
# @lc code=end

