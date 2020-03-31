#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# Accepted
# 61/61 cases passed (84 ms)
# Your runtime beats 32.02 % of python3 submissions
# Your memory usage beats 5.21 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
    def intersect(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = list()
        index_1 = 0
        index_2 = 0
        len_1 = len(nums1)
        len_2 = len(nums2)
        while (index_1 < len_1) and (index_2 < len_2):
            if nums1[index_1] == nums2[index_2]:
                result.append(nums1[index_1])
                index_1 += 1
                index_2 += 1
            else:
                if nums1[index_1] > nums2[index_2]:
                    index_2 += 1
                else:
                    index_1 += 1
        return result
# A = Solution()
# A.intersect([1,2,2,1],[2,2])
        
# @lc code=end

