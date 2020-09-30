#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#
# Accepted
# 45/45 cases passed (176 ms)
# Your runtime beats 61.6 % of python3 submissions
# Your memory usage beats 77.31 % of python3 submissions (13.5 MB)
# @lc code=start
class Solution:
    def lemonadeChange(self, bills) -> bool:
        change_temp = {'5':0,'10':0}
        for each in bills:
            change = each // 5
            if change == 1:
                change_temp['5'] += 1
            elif change == 2 and change_temp ['5'] > 0:
                change_temp['5'] -= 1
                change_temp['10'] += 1
            elif change == 4:
                if (change_temp['5'] > 0) and (change_temp['10'] > 0):
                    change_temp['5'] -= 1
                    change_temp['10'] -= 1
                    continue
                elif(change_temp['5'] > 2):  # must be here, we need change 10 first
                    change_temp['5'] -= 3
                    continue
                else:
                    return False
            else:
                return False
        return True

# A = Solution()
# A.lemonadeChange([5,5,5,10,20])
# @lc code=end

