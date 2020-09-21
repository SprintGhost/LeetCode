#
# @lc app=leetcode.cn id=836 lang=python3
#
# [836] 矩形重叠
#
# Accepted
# 43/43 cases passed (44 ms)
# Your runtime beats 43.68 % of python3 submissions
# Your memory usage beats 82.46 % of python3 submissions (13.3 MB)
# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not(rec1[2] <= rec2[0] or
                 rec1[3] <= rec2[1] or
                 rec1[0] >= rec2[2] or
                 rec1[1] >= rec2[3]);  

# Accepted
# 43/43 cases passed (36 ms)
# Your runtime beats 91.79 % of python3 submissions
# Your memory usage beats 89.79 % of python3 submissions (13.2 MB)
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/rectangle-overlap/solution/ju-xing-zhong-die-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

