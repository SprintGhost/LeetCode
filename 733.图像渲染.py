#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
# Accepted
# 277/277 cases passed (88 ms)
# Your runtime beats 90.13 % of python3 submissions
# Your memory usage beats 37.36 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        row = len(image)
        col = len(image[0])
        current_color = image[sr][sc]
        
        def dfs(x: int, y: int):
            if image[x][y] == current_color:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (0 <= mx < row) and (0 <= my < col)and(image[mx][my] == current_color):
                        dfs(mx, my)

        if current_color != newColor:
            dfs(sr, sc)
        return image
# Accepted
# 277/277 cases passed (96 ms)
# Your runtime beats 61.77 % of python3 submissions
# Your memory usage beats 70.12 % of python3 submissions (13.7 MB)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] != newColor:
            old, image[sr][sc] = image[sr][sc], newColor
            for i, j in zip((sr, sr+1, sr, sr-1), (sc+1, sc, sc-1, sc)):
                if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == old:
                    self.floodFill(image, i, j, newColor)
        return image

# 作者：qsctech-sange
# 链接：https://leetcode-cn.com/problems/flood-fill/solution/python3-dfs-yu-bfs-liang-chong-fang-fa-san-chong-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
# A = Solution()
# A.floodFill([[0,0,0],[0,0,0]],0,0,2)
# @lc code=end

