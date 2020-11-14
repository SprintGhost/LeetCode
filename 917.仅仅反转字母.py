#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# Accepted
# 116/116 cases passed (36 ms)
# Your runtime beats 88.48 % of python3 submissions
# Your memory usage beats 8.26 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        start = 0
        end = len(S) - 1
        S = list(S)
        while start < end:
            start_isalpha = S[start].isalpha()
            end_isalpha = S[end].isalpha()
            if start_isalpha and end_isalpha:
                temp = S[start]
                S[start] = S[end]
                S[end] = temp
                start += 1
                end -= 1
            elif not start_isalpha:
                start += 1
                continue
            elif not end_isalpha:
                end -= 1
                continue
            else:
                pass
        return ''.join(S)
        
# @lc code=end

