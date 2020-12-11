#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#
# Accepted
# 36/36 cases passed (64 ms)
# Your runtime beats 46.27 % of python3 submissions
# Your memory usage beats 5.07 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)
        return len({count(word) for word in A})

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/groups-of-special-equivalent-strings/solution/te-shu-deng-jie-zi-fu-chuan-zu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# A = Solution()
# A.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"])
# @lc code=end

