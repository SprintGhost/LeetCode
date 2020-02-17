#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# Accepted
# 600/600 cases passed (48 ms)
# Your runtime beats 16.28 % of python3 submissions
# Your memory usage beats 16.39 % of python3 submissions (13 MB)

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = bin(n)[2:][::-1]
        while (len(result) < 32):
            result= result + '0'
        return int(result,2)

# Accepted
# 600/600 cases passed (36 ms)
# Your runtime beats 59.03 % of python3 submissions
# Your memory usage beats 16.39 % of python3 submissions (13.2 MB)
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bit_index = 31
        while bit_index >= 0:
            result = result | (((n>>(31-bit_index)) & 1) << bit_index)
            bit_index -= 1
        return result



# @lc code=end

