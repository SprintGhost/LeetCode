#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# Accepted
# 15/15 cases passed (40 ms)
# Your runtime beats 47.62 % of python3 submissions
# Your memory usage beats 65.53 % of python3 submissions (13 MB)

# @lc code=start
class Solution:
    def generate(self, numRows: int):
        result_list = list()
        for index in range(numRows):
            if index == 0:
                result_list.append([1])
                continue
            if index == 1:
                result_list.append([1,1])
                continue
            temp_list = list()
            temp_list.append(1)
            for index_temp in range(len(result_list[index - 1]) - 1):
                temp_list.append(result_list[index - 1][index_temp] + result_list[index - 1][index_temp + 1])
            temp_list.append(1)
            result_list.append(temp_list)
        return result_list

# A = Solution()
# print(A.generate(1))
        
# @lc code=end

