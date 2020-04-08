#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# Accepted
# 14/14 cases passed (224 ms)
# Your runtime beats 42.61 % of python3 submissions
# Your memory usage beats 5.74 % of python3 submissions (18.2 MB)

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        index_s = 0
        index_t = 0
        while ((index_s < s_len) and (index_t < t_len)):
            if (s[index_s] == t[index_t]):
                index_t += 1
                index_s += 1
                continue
            index_t += 1
        return index_s == s_len

# Following solution use python function
# Accepted
# 14/14 cases passed (36 ms)
# Your runtime beats 94.9 % of python3 submissions
# Your memory usage beats 5.74 % of python3 submissions (18.2 MB)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if s == '':
            return True
        loc = -1
        for i in s:
            loc = t.find(i,loc+1)
            if loc == -1:           
                return False
        return True   

# Accepted
# 14/14 cases passed (60 ms)
# Your runtime beats 73.8 % of python3 submissions
# Your memory usage beats 5.74 % of python3 submissions (18.3 MB)

class Solution(object):
    def isSubsequence(self, s, t):
       
        t = iter(t)
        return all(c in t for c in s)
        

# 作者：yu-fa-tang-you-dian-tian
# 链接：https://leetcode-cn.com/problems/is-subsequence/solution/python-3chong-jie-fa-by-yu-fa-tang-you-dian-tian/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

