#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#
# Accepted
# 26/26 cases passed (48 ms)
# Your runtime beats 33.56 % of python3 submissions
# Your memory usage beats 81.3 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def numberOfLines(self, widths, S: str):
        last_wid = 0
        line_sum = 1
        map_dic = dict(zip('abcdefghijklmnopqrstuvwxyz',widths ))

        for each in S:
            # temp = widths[ord(each) - ord('a')]
            temp = map_dic[each]
            if (last_wid + temp) > 100:
                last_wid = temp
                line_sum += 1
            else:
                last_wid += temp
        return [line_sum, last_wid]

# if use dict at first, in line 15 && line 18, is faster
# Accepted
# 26/26 cases passed (36 ms)
# Your runtime beats 93.77 % of python3 submissions
# Your memory usage beats 88.49 % of python3 submissions (13.5 MB)

        
# @lc code=end

