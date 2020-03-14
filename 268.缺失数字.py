#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# Accepted
# 122/122 cases passed (52 ms)
# Your runtime beats 90.68 % of python3 submissions
# Your memory usage beats 11.06 % of python3 submissions (14.5 MB)

# @lc code=start
class Solution:
    def missingNumber(self, nums) -> int:
        nums = sorted(nums)
        nums_len = len(nums)
        for index in range(0, nums_len - 1):
            if (nums[index + 1] - nums[index]) != 1:
                return nums[index] + 1
        if (nums[0] == 0):
            return nums[nums_len - 1] + 1
        return 0


# Accepted
# 122/122 cases passed (72 ms)
# Your runtime beats 81.97 % of python3 submissions
# Your memory usage beats 11.65 % of python3 submissions (14.5 MB)

class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

# Accepted
# 122/122 cases passed (44 ms)
# Your runtime beats 96.04 % of python3 submissions
# Your memory usage beats 12.68 % of python3 submissions (14.4 MB)
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/missing-number/solution/que-shi-shu-zi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# print(A.missingNumber([0,1]))

# @lc code=end

