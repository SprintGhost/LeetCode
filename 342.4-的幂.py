#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# Accepted
# 1060/1060 cases passed (40 ms)
# Your runtime beats 51.85 % of python3 submissions
# Your memory usage beats 6.99 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 0:
            return False
        while (num % 4 == 0):
            num = num // 4
        return num == 1 
       
# Accepted
# 1060/1060 cases passed (36 ms)
# Your runtime beats 68.67 % of python3 submissions
# Your memory usage beats 6.99 % of python3 submissions (13.8 MB)
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0

# Accepted
# 1060/1060 cases passed (32 ms)
# Your runtime beats 85.09 % of python3 submissions
# Your memory usage beats 6.99 % of python3 submissions (13.4 MB)
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/power-of-four/solution/4de-mi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

