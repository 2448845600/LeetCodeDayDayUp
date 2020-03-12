class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        for i in range(min(l1, l2), 0, -1):
            if (l1 % i) == 0 and (l2 % i) == 0:
                if str1[0:i] * (l1 // i) == str1 and str1[0:i] * (l2 // i) == str2:
                    return str1[0:i]
        return ""

    def gcdOfStringsPlus(self, str1: str, str2: str) -> str:
        import math
        gcd = math.gcd(len(str1), len(str2))
        if str1[0:gcd] * (len(str1) // gcd) == str1 and str1[0:gcd] * (len(str2) // gcd) == str2:
            return str1[0:gcd]
        return ""


if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings(str1="ABCABC", str2="ABC"))
    print(s.gcdOfStringsPlus(str1="ABCABC", str2="ABC"))
