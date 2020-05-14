#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# Accepted
# 315/315 cases passed (52 ms)
# Your runtime beats 69.63 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_len = len(num1) - 1
        num2_len = len(num2) - 1
        carry_bit = 0
        result = str()
        while (num1_len >=0) or (num2_len >= 0):
            if num1_len < 0:
                temp_1 = 0
            else:
                temp_1 = ord(num1[num1_len]) - ord("0")
            if num2_len < 0:
                temp_2 = 0
            else:
                temp_2 = ord(num2[num2_len]) - ord("0")
            temp_sum = temp_1 + temp_2 + carry_bit
            carry_bit = temp_sum // 10
            result = chr(temp_sum%10 + 48) + result
            num1_len -= 1
            num2_len -= 1
        return "1" + result if carry_bit else result
                

# A = Solution()
# A.addStrings("0", "9")    
        
# @lc code=end

