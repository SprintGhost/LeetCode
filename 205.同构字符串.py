#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# Accepted
# 30/30 cases passed (48 ms)
# Your runtime beats 55.2 % of python3 submissions
# Your memory usage beats 16.3 % of python3 submissions (14.1 MB)

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (not s and t) or (not t and s):
            return False
        temp_s = dict()
        list_s = list()
        temp_t = dict()
        list_t = list()
        cs = 0
        ct = 0
        for index in range(0,len(s)):
            if (s[index] in temp_s):
                list_s.append(temp_s[s[index]])
            else:
                temp_s[s[index]] = cs
                list_s.append(cs)
                cs += 1
            if (t[index] in temp_t):
                list_t.append(temp_t[t[index]])
            else:
                temp_t[t[index]] = ct
                list_t.append(ct)
                ct += 1
            if list_t[index] != list_s[index]:
                return False
        return True

# Accepted
# 30/30 cases passed (36 ms)
# Your runtime beats 93.12 % of python3 submissions
# Your memory usage beats 40.24 % of python3 submissions (13.7 MB)

class Solution:
    def eigenValues(self, x):#
        L, p, k = {}, 0, ''
        for i in x:
            if i not in L:
                p += 1
                k, L[i] = k+str(p), str(p)
            else:
                k += L[i]
        return k
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.eigenValues(s) == self.eigenValues(t)


# A = Solution()
# print (A.isIsomorphic("aba", "baa"))

# @lc code=end

