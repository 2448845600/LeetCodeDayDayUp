class Solution:
    def maxProduct(self, words) -> int:
        bitmasks = []
        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << (ord(ch) - ord("a"))
            bitmasks.append(bitmask)

        max_res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_res = max(max_res, len(words[i]) * len(words[j]))

        return max_res

    def maxProductPlus(self, words) -> int:
        from collections import defaultdict
        hashbitmasks = defaultdict(int)
        for word in words:
            bitmask = 0
            for ch in word:
                bitmask |= 1 << (ord(ch) - ord("a"))
            hashbitmasks[bitmask] = max(hashbitmasks[bitmask], len(word))

        max_res = 0
        bitmasks = list(hashbitmasks.keys())
        for i in range(len(bitmasks)):
            for j in range(i + 1, len(bitmasks)):
                if bitmasks[i] & bitmasks[j] == 0:
                    max_res = max(max_res, hashbitmasks[bitmasks[i]] * hashbitmasks[bitmasks[j]])

        return max_res


if __name__ == '__main__':
    s = Solution()
    print(s.maxProductPlus(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
