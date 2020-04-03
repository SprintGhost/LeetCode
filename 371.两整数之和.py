#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# Accepted
# 13/13 cases passed (48 ms)
# Your runtime beats 19.44 % of python3 submissions
# Your memory usage beats 6.1 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0x100000000
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            carry = (a & b) << 1 
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)   

# 作者：jalan
# 链接：https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

