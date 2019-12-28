#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        Romam_Data = {'I': 1,
            'IV':4,
            'V': 5,
            'IX':9,
            'X': 10,
            'XL':40,
            'L': 50,
            'XC':90,
            'C': 100,
            'CD':400,
            'D': 500,
            'CM':900,
            'M': 1000
        }
        if (len(s) == 1):
            return Romam_Data[s]
        sum = 0
        current_index = 0
        while(len(s) > current_index):
            if ((s[current_index] == "I") or (s[current_index] == "X") or (s[current_index] == "C")) and (s[current_index:current_index + 2] in Romam_Data):
                sum += Romam_Data[s[current_index:current_index+2]]
                current_index += 2
            else:
                 sum += Romam_Data[s[current_index]]
                 current_index += 1
        return sum

# S = Solution()
# print (S.romanToInt("MCMXCIV"))          
        
# @lc code=end

