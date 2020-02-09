from queue import Queue


class Solution:

    def minJumps(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] == arr[n - 1]:
            return 1

        new_arr = [arr[0], arr[1]]
        for i in range(2, n):
            if arr[i] == arr[i - 1] and arr[i - 1] == arr[i - 2]:
                continue
            else:
                new_arr.append(arr[i])
        arr = new_arr
        n = len(arr)

        same = {}  # value:{id}
        same_min = {}

        for i in range(n):
            if arr[i] in same.keys():
                same[arr[i]].append(i)
            else:
                same[arr[i]] = [i]
                same_min[arr[i]] = n - 1

        ids = [n - 1 for _ in range(n)]

        que = Queue()  # id, step
        que.put((0, 0))

        while not que.empty():
            point = que.get()
            if point[0] == n - 1:
                return point[1]

            if point[0] - 1 >= 0:
                if point[1] + 1 < ids[point[0] - 1] and point[1] + 1 < same_min[arr[point[0] - 1]] + 1:
                    que.put((point[0] - 1, point[1] + 1))
                    ids[point[0] - 1] = point[1] + 1
                    same_min[arr[point[0] - 1]] = point[1] + 2
            if point[0] + 1 < n:
                if point[1] + 1 < ids[point[0] + 1] and point[1] + 1 < same_min[arr[point[0] + 1]] + 1:
                    que.put((point[0] + 1, point[1] + 1))
                    ids[point[0] + 1] = point[1] + 1
                    same_min[arr[point[0] + 1]] = point[1] + 2
            for j in same[arr[point[0]]]:
                if j != point[0]:
                    if point[1] + 1 < ids[j]:
                        que.put((j, point[1] + 1))
                        ids[j] = point[1] + 1

        return ids[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
    print(s.minJumps(arr=[7]))
    print(s.minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]))
    print(s.minJumps(arr=[6, 1, 9]))
    print(s.minJumps(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
    print(s.minJumps(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
