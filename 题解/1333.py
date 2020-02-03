class List():
    def __init__(self):
        pass


def filterRestaurants(restaurants, veganFriendly: int, maxPrice: int, maxDistance: int):
    if veganFriendly == 0:
        fRs = filter(lambda r: (r[3] <= maxPrice and r[4] <= maxDistance), restaurants)
    else:
        fRs = filter(lambda r: (r[2] == 1 and r[3] <= maxPrice and r[4] <= maxDistance), restaurants)
    res = sorted(fRs, key=lambda x: x[1], reverse=True)
    ids = [_[0] for _ in res]
    return ids

if __name__ == '__main__':
    restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3],[5, 1, 1, 15, 1]]
    veganFriendly = 1
    maxPrice = 50
    maxDistance = 10
    res = filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)
    print(res)
