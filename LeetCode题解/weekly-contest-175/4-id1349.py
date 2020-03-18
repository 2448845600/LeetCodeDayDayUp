from queue import Queue


class Solution:
    def maxStudents(self, seats) -> int:
        canSeat = []
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == ".":
                    canSeat.append((i, j))

        que = Queue()  # id, step
        que.put(canSeat[0])

        while not que.empty():
            p = que.get()


if __name__ == '__main__':
    s = Solution()
    print(s.maxStudents(seats=[["#", ".", "#", "#", ".", "#"],
                               [".", "#", "#", "#", "#", "."],
                               ["#", ".", "#", "#", ".", "#"]]))
