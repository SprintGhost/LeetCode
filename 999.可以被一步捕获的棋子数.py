#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#
# Accepted
# 22/22 cases passed (40 ms)
# Your runtime beats 69.36 % of python3 submissions
# Your memory usage beats 5.04 % of python3 submissions (14.8 MB)
# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt, st, ed = 0, 0, 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    st, ed = i, j
        for i in range(4):
            step = 0
            while True:
                tx = st + step * dx[i]
                ty = ed + step * dy[i]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                    break
                if board[tx][ty] == "p":
                    cnt += 1
                    break
                step += 1
        return cnt

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/available-captures-for-rook/solution/che-de-ke-yong-bu-huo-liang-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

