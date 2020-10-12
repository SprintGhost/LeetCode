#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
# Accepted
# 202/202 cases passed (44 ms)
# Your runtime beats 90.22 % of python3 submissions
# Your memory usage beats 90.23 % of python3 submissions (13.2 MB)
# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str):
        result = list()
        start = 0
        total = 0
        pre = s[0]
        for index, each in enumerate(s):
            if pre == each:
                total += 1
            elif total >= 3:
                result.append([start, index - 1])
                total = 1
                start = index
                pre = each
            else:
                total = 1
                start = index
                pre = each
        if total >= 3:
            result.append([start, index])
        return result

# Accepted
# 202/202 cases passed (44 ms)
# Your runtime beats 90.22 % of python3 submissions
# Your memory usage beats 33.95 % of python3 submissions (13.4 MB)

class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/positions-of-large-groups/solution/jiao-da-fen-zu-de-wei-zhi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.largeGroupPositions("abbxxxxzzy")

# @lc code=end

