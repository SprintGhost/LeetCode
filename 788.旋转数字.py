#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# Accepted
# 50/50 cases passed (164 ms)
# Your runtime beats 15.27 % of python3 submissions
# Your memory usage beats 51.11 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        for each in range(1, N + 1):
            each = str(each)
            result += (all(d not in '347' for d in each)
                    and any(d in '2569' for d in each))
        return result
# Accepted
# 50/50 cases passed (68 ms)
# Your runtime beats 87.34 % of python3 submissions
# Your memory usage beats 12.89 % of python3 submissions (13.8 MB)
class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1] + [0] * (N - 9)
        for i in range(N + 1):
            if d[i // 10] == -1 or d[i % 10] == -1:
                d[i] = -1
            elif d[i // 10] == 1 or d[i % 10] == 1:
                d[i] = 1
        return d[:N + 1].count(1)

# 作者：JamLeon
# 链接：https://leetcode-cn.com/problems/rotated-digits/solution/si-lu-jian-dan-xing-neng-jie-jin-shuang-100-by-j-7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

