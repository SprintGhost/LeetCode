#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#
# Accepted
# 84/84 cases passed (152 ms)
# Your runtime beats 53.54 % of python3 submissions
# Your memory usage beats 20.41 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for col in zip(*A):
            if any(col[i] > col[i+1] for i in range(len(col) - 1)):
                ans += 1
        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/delete-columns-to-make-sorted/solution/shan-lie-zao-xu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

