#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# Accepted
# 1000/1000 cases passed (40 ms)
# Your runtime beats 46.49 % of python3 submissions
# Your memory usage beats 44.95 % of python3 submissions (13.2 MB)

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        index = 0
        result = 0
        for each in s[::-1]:
            result += (ord(each) - 64) * (26 ** index)
            index += 1
        
        return result

# Accepted
# 1000/1000 cases passed (32 ms)
# Your runtime beats 84.78 % of python3 submissions
# Your memory usage beats 44.95 % of python3 submissions (13 MB)

class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for each in s:
            result = result * 26 + (ord(each) - 64)
        
        return result

# A = Solution()
# print(A.titleToNumber("AB"))
        
# @lc code=end

