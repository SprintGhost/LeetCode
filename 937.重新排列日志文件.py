#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)



# Accepted
# 63/63 cases passed (44 ms)
# Your runtime beats 87.27 % of python3 submissions
# Your memory usage beats 11.43 % of python3 submissions (13.6 MB)
        
# @lc code=end

