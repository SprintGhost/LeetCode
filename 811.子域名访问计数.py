#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#
# Accepted
# 52/52 cases passed (76 ms)
# Your runtime beats 31.93 % of python3 submissions
# Your memory usage beats 34.33 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains):
        temp_dict = {}
        for each in cpdomains:
            count,temp = each.split(" ")
            count = int(count)
            temp = temp.split(".")
            for i in range(len(temp)):
                if ".".join(temp[i:]) in temp_dict:
                    temp_dict[".".join(temp[i:])] += count
                else:
                    temp_dict[".".join(temp[i:])] = count

        return ["{} {}".format(ct, temp) for temp, ct in temp_dict.items()]

# A = Solution()
# A.subdomainVisits(["9001 discuss.leetcode.com"])



        
# @lc code=end

