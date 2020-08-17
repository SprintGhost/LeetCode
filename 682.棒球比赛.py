#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# Accepted
# 39/39 cases passed (56 ms)
# Your runtime beats 49.89 % of python3 submissions
# Your memory usage beats 14.29 % of python3 submissions (13.8 MB)

# @lc code=start
class Solution:
    def calPoints(self, ops) -> int:
        temp_sum = 0
        pre_val = list()
        for each in ops:
            if each == "+":
                pre_val.append(sum(pre_val[-2:]))
            elif each == "D":
                pre_val.append(pre_val[-1] * 2)
            elif each == "C":
                if pre_val:
                    pre_val.pop()
            else:
                pre_val.append(int(each))   
        return sum(pre_val)

# A = Solution()
# A.calPoints(["36","28","70","65","C","+","33","-46","84","C"])
        
# @lc code=end

