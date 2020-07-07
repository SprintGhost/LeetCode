#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# Accepted
# 113/113 cases passed (40 ms)
# Your runtime beats 68.24 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (13.7 MB)
# @lc code=start

# Accepted
# 113/113 cases passed (28 ms)
# Your runtime beats 99.46 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (13.5 MB)
class Solution:
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s:
            return False
        s_len = len(s)
        flag_a = 0
        flag_l = 0
        for each in s:
            if each != "L" and flag_l != 0:
                flag_l = 0
            if each == "L":
                flag_l +=1
            elif each == 'A':
                flag_a += 1
            if flag_l == 3 or flag_a == 2:
                return False
        return True

# A = Solution()
# A.checkRecord("PPALLA")

# @lc code=end

