#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# Accepted
# 601/601 cases passed (28 ms)
# Your runtime beats 92.12 % of python3 submissions
# Your memory usage beats 22.9 % of python3 submissions (13.2 MB)

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while (n > 0):
            result += n & 1
            n = n >> 1
        return result

# Accepted
# 601/601 cases passed (36 ms)
# Your runtime beats 53.05 % of python3 submissions
# Your memory usage beats 22.9 % of python3 submissions (13.2 MB)

class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            result += 1
            n &= (n - 1)
        return result



        
# @lc code=end

