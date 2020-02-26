#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# Accepted
# 401/401 cases passed (40 ms)
# Your runtime beats 59.94 % of python3 submissions
# Your memory usage beats 41.41 % of python3 submissions (13.1 MB)

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 7 or n == 1:
            return True
        if ((n < 10) and (n > 1)):
            return False
        sum = 0
        while n > 0:
            sum += ((n % 10) ** 2)
            n = n // 10
        return self.isHappy(sum)

# Accepted
# 401/401 cases passed (36 ms)
# Your runtime beats 78.93 % of python3 submissions
# Your memory usage beats 41.3 % of python3 submissions (13.1 MB)

class Solution:
    def isHappy(self, n):
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 4:
                return False
            if n == 1:
                return True

# 作者：000sheldon
# 链接：https://leetcode-cn.com/problems/happy-number/solution/python-jie-fa-by-000sheldon-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# Accepted
# 401/401 cases passed (36 ms)
# Your runtime beats 78.93 % of python3 submissions
# Your memory usage beats 41.3 % of python3 submissions (13.3 MB)

# Excellent solution
class Solution:
    def bitSquareSum(self, n):
        sum = 0
        while(n > 0):
            bit = n % 10
            sum += bit * bit
            n = n // 10
        return sum
    
    def isHappy(self, n):
        slow = n
        fast = n
        while(True):
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
            if (slow == fast):
                break
        return (slow == 1)



# 作者：rachy
# 链接：https://leetcode-cn.com/problems/happy-number/solution/shi-yong-kuai-man-zhi-zhen-si-xiang-zhao-chu-xun-h/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# print (A.isHappy(19))
        
# @lc code=end

