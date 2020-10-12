#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#
# Accepted
# 76/76 cases passed (84 ms)
# Your runtime beats 45.14 % of python3 submissions
# Your memory usage beats 90.98 % of python3 submissions (13.3 MB)
# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c_idx = [i for i in range(len(S)) if S[i]==C ]
        return [min(abs(i- j)  for j in c_idx) for i in range(len(S))]

# 作者：JamLeon
# 链接：https://leetcode-cn.com/problems/shortest-distance-to-a-character/solution/si-lu-jian-dan-liang-xing-dai-ma-xing-neng-gao-xia/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

