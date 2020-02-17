#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# Accepted
# 18/18 cases passed (20 ms)
# Your runtime beats 99.38 % of python3 submissions
# Your memory usage beats 46.33 % of python3 submissions (13 MB)

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <= 0:
            return ''
        result_str = ""
        while(n > 0):
            temp = n % 26
            if temp == 0:
                n -= 1
                result_str += 'Z'
            else:
                result_str += chr(temp + 64)
            n = n // 26
        return result_str[::-1]

A = Solution()
print(A.convertToTitle(52))

# @lc code=end

