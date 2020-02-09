from queue import Queue


class Solution:

    def minJumpsBFS(self, arr) -> int:
        n = len(arr)
        value2ids = {}  # value:{id}
        for i in range(n):
            if arr[i] in value2ids.keys():
                value2ids[arr[i]].append(i)
            else:
                value2ids[arr[i]] = [i]

        min_steps = [i for i in range(n)]  # max step is n-1
        que = Queue()
        que.put((0, 0))  # (id, step)
        while not que.empty():
            id, step = que.get()
            if id == n - 1:
                return step

            if id - 1 >= 0:
                if step + 1 < min_steps[id - 1]:
                    que.put((id - 1, step + 1))
                    min_steps[id - 1] = step + 1
            if id + 1 < n:
                if step + 1 < min_steps[id + 1]:
                    que.put((id + 1, step + 1))
                    min_steps[id + 1] = step + 1
            for j in value2ids[arr[id]]:
                if j != id:
                    if step + 1 < min_steps[j]:
                        que.put((j, step + 1))
                        min_steps[j] = step + 1

        return min_steps[n - 1]

    def minJumps(self, arr) -> int:
        if len(arr) == 1:
            return 0

        # example 1: [7,2,3,4,5,7,7,7]
        # example 1: [7,2,3,4,5,9,7,7,7,6,8,9]
        new_arr = [arr[0], arr[1]]
        for i in range(2, len(arr)):
            if arr[i] == arr[i - 1] and arr[i - 1] == arr[i - 2]:
                continue
            else:
                new_arr.append(arr[i])
        arr = new_arr
        n = len(arr)

        value2ids = {}  # value:{id}
        for i in range(n):
            if arr[i] in value2ids.keys():
                value2ids[arr[i]].append(i)
            else:
                value2ids[arr[i]] = [i]

        min_steps = [n - 1 for _ in range(n)]  # max step is n-1
        que = Queue()
        que.put((0, 0))  # (id, step)
        while not que.empty():
            id, step = que.get()
            if id == n - 1:
                return step

            if id - 1 >= 0:
                if step + 1 < min_steps[id - 1]:
                    que.put((id - 1, step + 1))
                    min_steps[id - 1] = step + 1
            if id + 1 < n:
                if step + 1 < min_steps[id + 1]:
                    que.put((id + 1, step + 1))
                    min_steps[id + 1] = step + 1
            for j in value2ids[arr[id]]:
                if j != id:
                    if step + 1 < min_steps[j]:
                        que.put((j, step + 1))
                        min_steps[j] = step + 1

        return min_steps[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minJumpsBFS(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
    print(s.minJumpsBFS(arr=[7]))
    print(s.minJumps(arr=[7, 6, 9, 6, 9, 6, 9, 7]))
    print(s.minJumps(arr=[6, 1, 9]))
    print(s.minJumps(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
    print(s.minJumps(arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]))
