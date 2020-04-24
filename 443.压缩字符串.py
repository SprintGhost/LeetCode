#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# Accepted
# 70/70 cases passed (92 ms)
# Your runtime beats 27.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/string-compression/solution/ya-suo-zi-fu-chuan-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        
# @lc code=end

