#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
# Accepted
# 92/92 cases passed (112 ms)
# Your runtime beats 63.02 % of python3 submissions
# Your memory usage beats 5.84 % of python3 submissions (17.5 MB)
# Highly recommended to read the explanation in the link below, very good
# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            if N == 1:
                return 1
            else:
                return -1
        inDegree = (N + 1)* [0]
        outDegree = (N + 1) * [0]
        for each in trust:
            inDegree[each[1]] += 1
            outDegree[each[0]] += 1

        judge = -1 
        for each in range(N + 1):
            if (inDegree[each] == N - 1 and outDegree[each] == 0):
                judge = each
                break
        return judge

# 作者：zui-weng-jiu-xian
# 链接：https://leetcode-cn.com/problems/find-the-town-judge/solution/zhao-dao-xiao-zhen-de-fa-guan-1chong-si-xiang-3cho/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

