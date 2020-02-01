#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# Accepted
# 16/16 cases passed (96 ms)
# Your runtime beats 82.89 % of python3 submissions
# Your memory usage beats 52.83 % of python3 submissions (15.7 MB)

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        if nums[0] != nums[1]:
            return nums[0]
        for index in range(1, len(nums) - 1):
            if (nums[index] != nums[index + 1]) and (nums[index - 1] != nums[index]):
                return nums[index]
        return nums[index + 1]

# Math funtion from Leetcode

# Accepted
# 16/16 cases passed (100 ms)
# Your runtime beats 72.54 % of python3 submissions
# Your memory usage beats 53.39 % of python3 submissions (15.5 MB)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


# Exclusive or method
# Accepted
# 16/16 cases passed (100 ms)
# Your runtime beats 72.54 % of python3 submissions
# Your memory usage beats 52.64 % of python3 submissions (15.8 MB)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

