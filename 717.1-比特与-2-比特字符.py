#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# Accepted
# 93/93 cases passed (72 ms)
# Your runtime beats 36.21 % of python3 submissions
# Your memory usage beats 96.25 % of python3 submissions (13.5 MB)
# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits_len = len(bits)
        result = bits
        index = 0
        while index < (bits_len - 1):
            if bits[index] == 1:
                index += 2
            else:
                index += 1
            result = bits[index:bits_len]
        return (result == [0])

# Accepted
# 93/93 cases passed (68 ms)
# Your runtime beats 56.8 % of python3 submissions
# Your memory usage beats 55.63 % of python3 submissions (13.7 MB)

class Solution(object):
    def isOneBitCharacter(self, bits):
        parity = bits.pop()
        while bits and bits.pop(): parity ^= 1
        return parity == 0

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/solution/1bi-te-yu-2bi-te-zi-fu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

