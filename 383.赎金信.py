#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# Accepted
# 126/126 cases passed (172 ms)
# Your runtime beats 7.39 % of python3 submissions
# Your memory usage beats 8.16 % of python3 submissions (14 MB)

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == "":
            return True
        if len(ransomNote) > len(magazine):
            return False
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        index_i = 0
        index_j = 0
        while (index_i < len(ransomNote)) and (index_j < len(magazine)):
            if ransomNote[index_i] != magazine[index_j]:
                index_j += 1
                continue
            index_j += 1
            index_i += 1
        
        if (index_i == len(ransomNote)) and (ransomNote[index_i - 1] == magazine[index_j - 1]):
            return True
        return False

# Accepted
# 126/126 cases passed (56 ms)
# Your runtime beats 77.84 % of python3 submissions
# Your memory usage beats 8.16 % of python3 submissions (13.8 MB)
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
        
# @lc code=end

