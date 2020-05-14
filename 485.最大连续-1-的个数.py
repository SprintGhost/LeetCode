#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# Accepted
# 41/41 cases passed (412 ms)
# Your runtime beats 86.55 % of python3 submissions
# Your memory usage beats 7.69 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        temp = 0
        for each in nums:
            if each == 1:
                temp += 1
            else:
                result = max(temp, result)
                temp = 0
        result = max(temp, result)
        return result
# Accepted
# 41/41 cases passed (468 ms)
# Your runtime beats 46.2 % of python3 submissions
# Your memory usage beats 7.69 % of python3 submissions (14.4 MB)
        return max(map(len, ''.join(map(str, nums)).split('0')))

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/max-consecutive-ones/solution/zui-da-lian-xu-1de-ge-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

