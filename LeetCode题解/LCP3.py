class Solution:
    def robot(self, command: str, obstacles, x: int, y: int) -> bool:
        # 超时
        cur_x = 0
        cur_y = 0
        while cur_x <= x and cur_y <= y:
            for c in command:
                if c == "U":
                    cur_y += 1
                else:
                    cur_x += 1

                if [cur_x, cur_y] in obstacles:
                    return False

                if cur_x == x and cur_y == y:
                    return True
        return False

    def robotPlus(self, command: str, obstacles, x: int, y: int) -> bool:
        # 判断是否到达
        # 是否到达obstacles和终点即可
        m = command.count("R")
        n = command.count("U")

        def isReach(x, y):
            circle, step = divmod(x + y, m + n)
            cur_x = circle * m
            cur_y = circle * n
            for i in range(step):
                if command[i] == "R":
                    cur_x += 1
                else:
                    cur_y += 1
            if cur_x == x and cur_y == y:
                return True
            else:
                return False

        if isReach(x, y):
            for obs in obstacles:
                if obs[0] > x or obs[1] > y:
                    continue
                else:
                    if isReach(obs[0], obs[1]):
                        return False
        else:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.robotPlus("URR", [], 3, 2))
    print(s.robotPlus("URRURRR", [[7, 7], [0, 5], [2, 7], [8, 6], [8, 7], [6, 5], [4, 4], [0, 3], [3, 6]], 4915, 1966))
