#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
# Accepted
# 200/200 cases passed (216 ms)
# Your runtime beats 90.87 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions (13.7 MB)
class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))

            
        
# @lc code=end

