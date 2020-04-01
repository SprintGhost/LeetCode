#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# Accepted
# 68/68 cases passed (48 ms)
# Your runtime beats 26.85 % of python3 submissions
# Your memory usage beats 5.63 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        half = num // 2
        low_flag = True
        while True:
            if (half * half) == num:
                return True
            elif (half * half) > num:
                if (not low_flag):
                    return False
                half = half // 2
            else:
                half += 1
                low_flag = False


# Accepted
# 68/68 cases passed (32 ms)
# Your runtime beats 81.48 % of python3 submissions
# Your memory usage beats 5.63 % of python3 submissions (13.7 MB)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/valid-perfect-square/solution/you-xiao-de-wan-quan-ping-fang-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Accepted
# 68/68 cases passed (48 ms)
# Your runtime beats 26.85 % of python3 submissions
# Your memory usage beats 5.63 % of python3 submissions (13.6 MB)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num1 = 1
        while(num > 0): 
            num -= num1
            num1 += 2
        return num == 0

# 作者：lu-guo-de-feng-2
# 链接：https://leetcode-cn.com/problems/valid-perfect-square/solution/zhi-xing-yong-shi-0-ms-zai-suo-you-c-ti-jiao-zh-44/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        
# @lc code=end

