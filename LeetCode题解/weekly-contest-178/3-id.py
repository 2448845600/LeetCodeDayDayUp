class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        slaves = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                slaves[m].append(i)

        from queue import Queue
        que = Queue()
        que.put((headID, 0))

        res = 0
        while not que.empty():
            leader, usedt = que.get()
            for slave in slaves[leader]:
                que.put((slave, usedt + informTime[leader]))
            res = max(res, usedt)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]))
    print(s.numOfMinutes(11, 4, [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4], [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]))
