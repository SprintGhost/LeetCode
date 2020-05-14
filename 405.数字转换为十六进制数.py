#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# Accepted
# 100/100 cases passed (32 ms)
# Your runtime beats 79.91 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        return hex(num&0xffffffff).replace('0x','')


# Another CPP solution:
# class Solution {
# public:
#     string toHex(int num) {
#         if (num == 0)
#             return "0";
#         string ret;
#         constexpr char hex[] = "0123456789abcdef";
#         unsigned int N = num > 0 ? num : 0x100000000 + num;
#         while (N != 0) {
#             ret = hex[N & 0b1111] + ret;
#             N = N >> 4;
#         }
#         return ret;
#     }
# };

# 作者：yrand
# 链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/solution/c-0ms-by-yrand/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

