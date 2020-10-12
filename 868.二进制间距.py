#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#
# Accepted
# 260/260 cases passed (40 ms)
# Your runtime beats 78.51 % of python3 submissions
# Your memory usage beats 29.91 % of python3 submissions (13.4 MB)
# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        last = None
        ans = 0
        for i in range(32):
            if (n>> i) & 1:
                if last is not None:
                    ans = max(ans, i - last)
                last = i
        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/binary-gap/solution/er-jin-zhi-jian-ju-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# A = Solution()
# A.binaryGap(22)

# @lc code=end

