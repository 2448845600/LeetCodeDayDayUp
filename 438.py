class Solution:
    def isAnagrams(self, s, p):
        needs = {}
        windows = {}
        for c in p:
            if c in windows.keys():
                needs[c] += 1
            else:
                needs[c] = 1
                windows[c] = 0
        for c in s:
            if c in windows.keys():
                windows[c] += 1
            else:
                return False
        for key in windows.keys():
            if windows[key] != needs[key]:
                return False
        return True

    def findAnagrams(self, s: str, p: str):
        s_len = len(s)
        p_len = len(p)

        if p_len > s_len:
            return []

        count = []
        left = 0
        right = p_len
        while right < s_len + 1:
            if self.isAnagrams(s[left:right], p):
                count.append(left)
                left += 1
            else:
                if right < s_len and s[right] in p:
                    left += 1
                else:
                    left = right
            right = left + p_len
        return count

    def findAnagramsPlus(self, s: str, p: str):
        n = len(s)
        k = len(p)

        if k > n:
            return []

        sArr = [ord(c) - 97 for c in s]
        pArr = [ord(c) - 97 for c in p]
        hashArr = [0 for _ in range(26)]
        for i in pArr:
            hashArr[i] += 1

        right = 0
        left = 0
        count = 0
        res = []
        while right < n:
            hashArr[sArr[right]] -= 1
            if hashArr[sArr[right]] >= 0:
                count += 1
            if right > k - 1:
                hashArr[sArr[left]] += 1
                if hashArr[sArr[left]] > 0:
                    count -= 1
                left += 1

            if count == k:
                res.append(left)
            right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagramsPlus("cbaebabacd", "abc"))
    print(s.findAnagramsPlus("op", "by"))
