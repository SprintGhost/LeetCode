#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#


# Accepted
# 95/95 cases passed (68 ms)
# Your runtime beats 88.25 % of python3 submissions
# Your memory usage beats 48.25 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        min_num = 0
        max_num = len(S)
        result = list()
        for each in S:
            if each == "I":
                result.append(min_num)
                min_num += 1
            else:
                result.append(max_num)
                max_num -= 1
        result.append(min_num)
        return result
        
# @lc code=end

