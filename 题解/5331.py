def maxJumpsDFS(arr, d):
    n = len(arr)
    dp = [1 for _ in range(n)]
    res = [1 for _ in range(n)]
    used = [False for _ in range(n)]

    paths = {}  # 一跳可达
    for cur in range(n):
        paths[cur] = []
        for step in range(1, d + 1):
            if cur - step >= 0 and arr[cur] > arr[cur - step]:
                paths[cur].append(cur - step)
            else:
                break
        for step in range(1, d + 1):
            if cur + step < n and arr[cur] > arr[cur + step]:
                paths[cur].append(cur + step)
            else:
                break

    def dfs(i):
        if not used[i]:
            for path in paths[i]:
                res[i] = max(res[i], dfs(path) + 1)
            used[i] = True
        return res[i]

    max_res = dfs(0)
    for i in range(1, n):
        max_res = max(max_res, dfs(i))

    return max_res


def maxJumps(arr, d):
    n = len(arr)
    a = [[i, arr[i]] for i in range(n)]
    a = sorted(a, key=lambda x: x[1])

    res = 0
    dp = [1 for _ in range(n)]
    for cur, _ in a:
        for step in range(1, d + 1):
            if cur - step >= 0 and arr[cur] > arr[cur - step]:
                dp[cur] = max(dp[cur], dp[cur - step] + 1)
            else:
                break
        for step in range(1, d + 1):
            if cur + step < n and arr[cur] > arr[cur + step]:
                dp[cur] = max(dp[cur], dp[cur + step] + 1)
            else:
                break
        res = max(res, dp[cur])
    return res


if __name__ == '__main__':
    print(maxJumpsDFS(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))
    print(maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))
