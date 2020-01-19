#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# Accepted
# 294/294 cases passed (64 ms)
# Your runtime beats 7.4 % of python3 submissions
# Your memory usage beats 99.69 % of python3 submissions (12.6 MB)

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, extra = '',0 
        i,j=len(a)-1,len(b)-1
        while i>=0 or j>=0:
            if i >= 0:
                extra += ord(a[i]) - ord('0')
            if j >= 0:
                extra += ord(b[j]) - ord('0')
            ans += str(extra % 2)
            extra //= 2
            i,j = i-1,j-1
        if extra == 1:
            ans += '1'
        return ans[::-1]

        
# @lc code=end

