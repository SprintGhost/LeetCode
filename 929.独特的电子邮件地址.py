#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#
# if type(result) = list
# Accepted
# 184/184 cases passed (64 ms)
# Your runtime beats 71.12 % of python3 submissions
# Your memory usage beats 74.13 % of python3 submission

# if type(result) = set
# Accepted
# 184/184 cases passed (60 ms)
# Your runtime beats 84.69 % of python3 submissions
# Your memory usage beats 26.88 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for each in emails:
            local_name, domain_name = each.split("@")
            local_name = local_name.split("+")[0].replace(".","") + "@"
            result.add(local_name + domain_name)
        return len(result)
        
# @lc code=end

