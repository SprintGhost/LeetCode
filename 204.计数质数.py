#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# Accepted
# 20/20 cases passed (124 ms)
# Your runtime beats 85.76 % of python3 submissions
# Your memory usage beats 28.36 % of python3 submissions (36.8 MB)

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)

        
# @lc code=end

