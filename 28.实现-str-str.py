#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#


# Accepted
# 74/74 cases passed (32 ms)
# Your runtime beats 92.42 % of python3 submissions
# Your memory usage beats 99.53 % of python3 submissions (12.8 MB)

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        index_hay = 0
        result = -1
        hay_len = len(haystack)
        needle_len = len(needle)
        if (hay_len < needle_len):
            return -1
        shft_map = dict()
        # Get Shft map
        for index in range(needle_len - 1,-1,-1):
            if not shft_map.get(needle[index]):
                shft_map[needle[index]] = needle_len - index
        shft_map['ot'] = needle_len + 1

        while (index_hay + needle_len <= hay_len):
            cut_str = haystack[index_hay:index_hay + needle_len]
            if cut_str == needle:
                return index_hay
            else:
                if ((index_hay + needle_len) >= hay_len):
                    return -1
                if shft_map.get(haystack[index_hay + needle_len]):
                    index_hay += shft_map[haystack[index_hay + needle_len]]
                else:
                    index_hay += shft_map["ot"]
        return -1 if (index_hay + needle_len >= hay_len) else index_hay

# A = Solution()
# print (A.strStr("mississippi", "issip"))
        
# @lc code=end

