#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#

# Accepted
# 18/18 cases passed (32 ms)
# Your runtime beats 97.22 % of python3 submissions
# Your memory usage beats 99.27 % of python3 submissions (12.9 MB)

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        num = self.countAndSay(n -1) + "*"
# Accepted
# 18/18 cases passed (56 ms)
# Your runtime beats 17.53 % of python3 submissions
# Your memory usage beats 99.36 % of python3 submissions (12.8 MB)
# if not use list, runtime  will get longer.
        num_list = list(num)
        count = 1
        return_str = ""
        for index in range(len(num) - 1):
            # if (num[index] == num[index + 1]):
            if (num[index] == num_list[index + 1]):
                count += 1
            else:
                # return_str += str(count) + num[index]
                return_str += str(count) + num_list[index]
                count = 1
        return return_str
# A = Solution()
# A.countAndSay(5)
# @lc code=end

