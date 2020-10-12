#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
# Accepted
# 110/110 cases passed (40 ms)
# Your runtime beats 76.8 % of python3 submissions
# Your memory usage beats 80.34 % of python3 submissions (13.3 MB)
# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        temp_s = []
        temp_t = []
        for each in S:
            if temp_s != [] and each == "#":
                temp_s.pop(-1)
            elif each == "#":
                continue
            else:
                temp_s.append(each)
        for each in T:
            if temp_t != [] and each == "#":
                temp_t.pop(-1)
            elif each == "#":
                continue
            else:
                temp_t.append(each)
        return temp_s == temp_t


# Accepted
# 110/110 cases passed (44 ms)
# Your runtime beats 53.1 % of python3 submissions
# Your memory usage beats 45.79 % of python3 submissions (13.4 MB)
import itertools

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/backspace-string-compare/solution/bi-jiao-han-tui-ge-de-zi-fu-chuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        
# @lc code=end

