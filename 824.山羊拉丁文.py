#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文

# Accepted
# 99/99 cases passed (44 ms)
# Your runtime beats 43.53 % of python3 submissions
# Your memory usage beats 19.3 % of python3 submissions (13.4 MB)#


# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        result = str()
        vowel_list = ['a','A','e','E','i','I','o','O','u','U']
        end = "ma"
        for index, word in enumerate(words):
            if word[0] in vowel_list:
                word += end
            else:
                word = word[1:] + word[0] + end
            word += (index + 1) * "a"
            result += word + " "
        return result[:-1]
    

        
# @lc code=end

