#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
# Accepted
# 156/156 cases passed (48 ms)
# Your runtime beats 62.64 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (13.6 MB)

# @lc code=start
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        temp = int(math.sqrt(num))
        sum_temp = 0
        while temp > 0:
            if (num % temp) != 0:
                temp -= 1
                continue
            if temp != 1:
                sum_temp += (temp + num // temp)
            else:
                sum_temp += 1
            temp -= 1
        return (sum_temp == num)

# The following sulution use Euclidean euler's theorem
# Accepted
# 156/156 cases passed (40 ms)
# Your runtime beats 86.68 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (13.7 MB)
        primes = [2,3,5,7,13,17,19,31]
        for prime in primes:
            if (self.pn(prime) == num):
                return True
        return False
    def pn(slef, p):
        return (1 << (p - 1)) * ((1 << p) - 1)


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/perfect-number/solution/wan-mei-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
# A = Solution()
# print(A.checkPerfectNumber(28))
# @lc code=end

