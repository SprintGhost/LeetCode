#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# Accepted
# 8/8 cases passed (48 ms)
# Your runtime beats 76.37 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (14.5 MB)

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int):
        result = list()
        for each in range(1,n+1):
            if each % 15 == 0:
                result.append("FizzBuzz")
            elif each % 3 == 0:
                result.append("Fizz")
            elif each % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(each))
        return result

# @lc code=end

