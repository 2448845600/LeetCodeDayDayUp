class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        count = 0
        n = len(arr)
        ksum = 0
        for i in range(0, k):
            ksum += arr[i]
        if ksum >= k * threshold:
            count += 1
        for i in range(k, n):
            ksum = ksum - arr[i - k] + arr[i]
            if ksum >= k * threshold:
                count += 1

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubarrays(arr = [1,1,1,1,1], k = 1, threshold = 0))
    print(s.numOfSubarrays(arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))
    print(s.numOfSubarrays(arr = [4,4,4,4], k = 4, threshold = 1))
