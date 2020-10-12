#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
# Accepted
# 57/57 cases passed (184 ms)
# Your runtime beats 59.06 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (13.8 MB)
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))

       
# @lc code=end

