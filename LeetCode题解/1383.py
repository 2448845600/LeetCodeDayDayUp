def maxPerformance(n: int, speed, efficiency, k: int) -> int:
    import heapq

    items = [(speed[i], efficiency[i]) for i in range(n)]
    items = sorted(items, key=lambda x: x[1], reverse=True)

    topk_heap = []
    sumk_speeds = 0
    max_preformance = 0
    for item in items:
        heapq.heappush(topk_heap, item[0])
        if len(topk_heap) > k:
            sumk_speeds -= heapq.heappop(topk_heap)
        sumk_speeds += item[0]
        max_preformance = max(max_preformance, sumk_speeds * item[1])

    return max_preformance % 1000000007


print(maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))
