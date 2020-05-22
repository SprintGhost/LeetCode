#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#
# Accepted
# 550/550 cases passed (36 ms)
# Your runtime beats 86.31 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.6 MB)

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_num = 0
        for each in word:
            if ord(each) <= ord("Z"):
                capital_num += 1
        if (capital_num == 0) or (capital_num == len(word)):
            return True
        if (capital_num == 1) and (ord(word[0]) <= ord("Z")):
            return True
        return False

# Accepted
# 550/550 cases passed (44 ms)
# Your runtime beats 47.55 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.8 MB)

import re
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if re.match(r'(([A-Z]+)|([A-Z]?[a-z]+))$',word) else False

# 作者：jutraman
# 链接：https://leetcode-cn.com/problems/detect-capital/solution/pythonjian-ce-da-xie-zi-mu-by-jutraman/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

