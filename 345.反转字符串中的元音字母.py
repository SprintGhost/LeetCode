#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# Accepted
# 481/481 cases passed (60 ms)
# Your runtime beats 75.99 % of python3 submissions
# Your memory usage beats 5.37 % of python3 submissions (16 MB)

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_list = ["a","e","i","o","u","A","E","I","O","U"]
        temp = list()
        s = list(s) 
        for index, each in enumerate(s):
            if each in vowels_list:
                temp.append(index)
        last = len(temp)
        index = 0
        while index < last:
            temp_v = s[temp[index]]
            s[temp[index]] = s[temp[last - 1]]
            s[temp[last - 1]] = temp_v
            index += 1
            last -= 1
        return "".join(s)


# A = Solution()
# print(A.reverseVowels("hello"))

            

        
# @lc code=end

