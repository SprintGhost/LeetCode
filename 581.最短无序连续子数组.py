#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# Accepted
# 307/307 cases passed (248 ms)
# Your runtime beats 81.08 % of python3 submissions
# Your memory usage beats 5.56 % of python3 submissions (14.9 MB)

# @lc code=start
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diffs = [diff for diff, (unsort, sort) in enumerate(zip(nums, sorted(nums))) if unsort != sort]
        return len(diffs) and max(diffs) - min(diffs) + 1
        



# 作者：larcenciel
# 链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/581-zui-duan-wu-xu-lian-xu-zi-shu-zu-liang-xing-ga/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
    

# @lc code=end

