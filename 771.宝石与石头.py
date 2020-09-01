#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#
# Accepted
# 254/254 cases passed (44 ms)
# Your runtime beats 50.85 % of python3 submissions
# Your memory usage beats 90.39 % of python3 submissions (13.5 MB)
# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for each in S:
            if each in J:
                result += 1
        return result

        
# @lc code=end

