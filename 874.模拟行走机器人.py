#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
# Accepted
# 47/47 cases passed (412 ms)
# Your runtime beats 98.23 % of python3 submissions
# Your memory usage beats 5.15 % of python3 submissions (19.2 MB)
# @lc code=start
class Solution(object):
    def robotSim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans

# Accepted
# 47/47 cases passed (412 ms)
# Your runtime beats 98.23 % of python3 submissions
# Your memory usage beats 5.15 % of python3 submissions (19.4 MB)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not commands:
            return 0
        direx = [0, 1, 0, -1]
        direy = [1, 0, -1, 0]
        curx, cury, curdire, ans = 0, 0, 0, 0
        com_len, obs_len = len(commands), len(obstacles)
        obstacle_set = {(obstacles[i][0], obstacles[i][1]) for i in range(obs_len)}
    
        for i in range(com_len):
            if commands[i] == -1: # 向右转90度
                curdire = (curdire +1) % 4
            elif commands[i] == -2: # 向左转90度
                curdire = (curdire + 3) %4
            else: #  1 <= x <= 9: 向前移动x个单位长度
                for j in range(commands[i]):
                    # 试图走出一步，并判断是否遇到了障碍物
                    nx = curx + direx[curdire]
                    ny = cury + direy[curdire]
                    # 当前坐标不是障碍物，计算并存储的最大欧式距离的平方做比较
                    if (nx, ny) not in obstacle_set:
                        curx = nx
                        cury = ny
                        ans = max(ans, curx*curx + cury*cury)
                    else:
                        # 是障碍点，被挡住了，停留，智能等待下一个指令，那可以跳出当前指令了。
                        break
        return ans 

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/walking-robot-simulation/solution/mo-ni-xing-zou-ji-qi-ren-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

