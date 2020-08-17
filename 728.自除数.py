#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# Accepted
# 31/31 cases passed (48 ms)
# Your runtime beats 95.03 % of python3 submissions
# Your memory usage beats 66.67 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        result = list()
        for each in range(left, right + 1):
            flag = True
            if '0' in str(each):
                continue
            for temp in str(each):
                if each % int(temp) != 0:
                    flag = False
                    break
            if flag:
                result.append(each)
        return result
# A = Solution()
# A.selfDividingNumbers(1,22)   
# @lc code=end

