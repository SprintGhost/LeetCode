#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# Time Limit Exceeded
# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        temp =int(math.sqrt(c)//1) + 1
        temp_list = list()
        for each in range(0, temp):
            temp_list.append(each)
        while True:
            if len(temp_list) < 1:
                return False
            index = 0
            while index < len(temp_list):
                if ((temp_list[0] ** 2) + (temp_list[index] ** 2)) == c:
                    return True
                index += 1
            temp_list.pop(0)
        
        return False
# Accepted
# 124/124 cases passed (44 ms)
# Your runtime beats 99.51 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions (13.7 MB)
        index = 2
        while (index * index <= c):
            count = 0
            if (c % index == 0):
                while (c % index == 0):
                    count += 1
                    c //= index
                if (index % 4 == 3 and count % 2 != 0):
                    return False
            index += 1
        return c % 4 != 3



# @lc code=end

