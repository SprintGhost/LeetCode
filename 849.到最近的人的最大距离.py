#
# @lc app=leetcode.cn id=849 lang=python3
#
# [849] 到最近的人的最大距离
#
# Accepted
# 79/79 cases passed (60 ms)
# Your runtime beats 63.8 % of python3 submissions
# Your memory usage beats 48.59 % of python3 submissions (13.9 MB)
# @lc code=start
# class Solution:
#     def maxDistToClosest(self, seats) -> int:
#         start = -1
#         end = 0
#         max_index = 0
#         for index, each in enumerate(seats):
#             if each == 1:
#                 end = index
#                 if start == -1:
#                     max_index = max(end - 0, max_index)
#                 else:
#                     max_index = max((end - start) // 2, max_index)
#                 start = index
#             elif index == len(seats) - 1:
#                 end = index
#                 max_index = max(end - start,max_index)
#             else:
#                 pass
#         return max_index

# Accepted
# 79/79 cases passed (52 ms)
# Your runtime beats 88.34 % of python3 submissions
# Your memory usage beats 97.89 % of python3 submissions (13.7 MB)
import itertools

class Solution(object):
    def maxDistToClosest(self, seats):
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)//2)

        return max(ans, seats.index(1), seats[::-1].index(1))

A = Solution()
A.maxDistToClosest([1,0,0,0,0,1,1,0,1,0,0,0,0,0])
# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/maximize-distance-to-closest-person/solution/dao-zui-jin-de-ren-de-zui-da-ju-chi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

