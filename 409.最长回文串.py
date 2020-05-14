#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# Accepted
# 95/95 cases passed (36 ms)
# Your runtime beats 86.71 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp = dict()
        result = 0
        for each in s:
            if each in temp:
                temp[each] += 1
            else:
                temp[each] = 1
        for key in temp:
            if (temp[key] % 2 == 0):
                result += temp[key]
            elif temp[key] > 1:
                result += temp[key] - 1
              
        return ((result + 1)if result <len(s) else len(s))
    

# A = Solution()
# A.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
        
# @lc code=end

