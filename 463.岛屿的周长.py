#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# Accepted
# 5833/5833 cases passed (628 ms)
# Your runtime beats 68.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
    def islandPerimeter(self, grid) -> int:
        last_line = dict()
        result = 0
        for each_line in grid:
            for index, each in enumerate(each_line):
                if each == 0:
                    last_line[index] = 0
                else:
                    result += 4
                    if (index > 0) and (each_line[index - 1] == 1):
                        result -= 2
                    if (index in last_line) and (last_line[index] == 1):
                        result -= 2
                    last_line[index] = 1
        return result


# A = Solution()
# A.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])


        
# @lc code=end

