#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#

# Time Limit Exceeded

# @lc code=start
class Solution:
    def findPairs(self, nums, k: int) -> int:
        temp = list()
        index_x = 0
        index_j = 1
        result = 0
        while index_x < len(nums):
            while index_j < len(nums):
                if (abs(nums[index_x] - nums[index_j]) == k) and ([nums[index_x], nums[index_j]]not in temp) and ([nums[index_j], nums[index_x]] not in temp):
                    result += 1
                    temp.append([nums[index_x], nums[index_j]])
                    temp.append([nums[index_j], nums[index_x]])
                index_j += 1
            index_x += 1
            index_j = index_x + 1
        return result

# Accepted
# 72/72 cases passed (152 ms)
# Your runtime beats 75.22 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (16 MB)
        if k < 0:
            return 0
        if k == 0:
            return len(set([i for i in nums if nums.count(i) >= 2]))
        return len(set(i + k for i in nums) & set(nums))

# 作者：jpch89
# 链接：https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/solution/python-3wu-xing-jie-ba-xing-jie-by-jpch89/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

