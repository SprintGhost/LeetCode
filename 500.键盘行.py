#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# Accepted
# 22/22 cases passed (32 ms)
# Your runtime beats 90.9 % of python3 submissions
# Your memory usage beats 14.29 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        res = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                res.append(word)
        return res

        
# @lc code=end

