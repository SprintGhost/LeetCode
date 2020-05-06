#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# Accepted
# 149/149 cases passed (28 ms)
# Your runtime beats 97.31 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        temp = 1
        nums_temp = num >> 1
        while (nums_temp != 0):
            temp = (temp | (temp << 1))
            nums_temp = nums_temp >> 1
        return (num ^ temp)

# Accepted
# 149/149 cases passed (44 ms)
# Your runtime beats 37.48 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.6 MB)
        while temp <= num:
            temp = temp << 1
        return temp - num - 1

# A = Solution()
# A.findComplement(5)
# @lc code=end

