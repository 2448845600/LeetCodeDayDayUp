from itertools import product


class Solution:
    def letterCombinations(self, digits: str):
        if digits == "":
            return []

        d = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
             "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        res = []
        for p in product(*[d[s] for s in digits]):
            s = ""
            for c in p:
                s += c
            res.append(s)

        return res

    def letterCombinationsPlus(self, digits: str):
        if digits == "":
            return []
        d = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
             "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        res = [""]
        for c in digits:
            res = [x + y for x in res for y in d[c]]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinationsPlus("23"))
