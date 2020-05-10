#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
import re
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans=re.findall(r'\w+',S)
        ans=''.join(ans)
        i=K if len(ans)%K==0 else len(ans)%K
        ans=[ans[:i]]+re.findall(r'.{'+str(K)+'}',ans[i:])
        return ('-'.join(ans)).upper()


# @lc code=end

