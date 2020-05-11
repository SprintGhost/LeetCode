#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# Accepted
# 50/50 cases passed (5736 ms)
# Your runtime beats 5.16 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions (13.8 MB)

# @lc code=start
class Solution:
    def constructRectangle(self, area: int):
        if area == 1:
            return [1, 1]
        l = area // 2 + 1
        w = 1
        result = [area,1]
        while l > w:
            if (area % l) == 0:
                w = area // l
            else:
                l -= 1
                continue
            if (l - w) == 0:
                return [l, w]
            if (l - w) < (result[0] - result[1]):
                result = [l, w]
            l -= 1
        return result
# Accepted
# 50/50 cases passed (44 ms)
# Your runtime beats 63.39 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions (13.7 MB)
        import math
        W = int(math.sqrt(area))  
        while area%W != 0:
            W -= 1 
        return [area//W,W]

# A = Solution()
# A.constructRectangle(16)

# @lc code=end

