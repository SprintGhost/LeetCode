#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# Accepted
# 204/204 cases passed (28 ms)
# Your runtime beats 99.26 % of python3 submissions
# Your memory usage beats 16.67 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = bin(n).replace("0b",'')
        temp_len = len(temp) - 1
        index = 0
        while index < temp_len:
            if temp[index] == temp[index + 1]:
                return False
            index += 1
        return True

# Accepted
# 204/204 cases passed (40 ms)
# Your runtime beats 71.43 % of python3 submissions
# Your memory usage beats 16.67 % of python3 submissions (13.5 MB)

        n = (n ^ (n >> 1)) + 1
        return ((n & (n -1)) == 0)



# @lc code=end

