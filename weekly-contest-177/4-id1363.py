class Solution:
    def largestMultipleOfThree(self, digits) -> str:
        arr0 = []
        arr1 = []
        arr2 = []

        for digit in digits:
            if digit % 3 == 0:
                arr0.append(digit)
            elif digit % 3 == 1:
                arr1.append(digit)
            else:
                arr2.append(digit)

        arr1.sort(reverse=True)
        arr2.sort(reverse=True)
        l1 = len(arr1)
        l2 = len(arr2)

        tail1 = l1 % 3
        tail2 = l2 % 3
        yes1 = l1 - tail1
        yes2 = l2 - tail2

        res = arr0
        if (tail1 == 1 and tail2 == 1 or (tail1 == 2 and tail2 == 2) or (tail1 == 0 and tail2 == 0)):
            res = digits
        elif tail1 == 1 and tail2 == 2:
            res.extend(arr1[0:yes1])
            res.extend(arr2[0:yes2])
            res.append(arr1[-1])
            res.append(max(arr2[-1], arr2[-2]))
        elif tail1 == 2 and tail2 == 1:
            res.extend(arr1[0:yes1])
            res.extend(arr2[0:yes2])
            res.append(max(arr1[-1], arr1[-2]))
            res.append(arr2[-1])
        elif tail1 == 0 and tail2 == 2:
            if l1 > 2:
                res.extend(arr1[0:-1])
                res.extend(arr2)
            else:
                res.extend(arr1[0:yes1])
                res.extend(arr2[0:yes2])
        elif tail1 == 2 and tail2 == 0:
            if l2 > 2:
                res.extend(arr1)
                res.extend(arr2[0:-1])
            else:
                res.extend(arr1[0:yes1])
                res.extend(arr2[0:yes2])
        else:
            res.extend(arr1[0:yes1])
            res.extend(arr2[0:yes2])
        res.sort(reverse=True)
        res_str = ''
        for r in res:
            res_str += str(r)

        if len(res_str) == 0:
            return ''
        elif res_str[0] == '0':
            return '0'
        else:
            return res_str


if __name__ == '__main__':
    s = Solution()
    print(s.largestMultipleOfThree(digits=[8, 1, 9]))
    print(s.largestMultipleOfThree(digits=[1]))
    print(s.largestMultipleOfThree(digits=[0, 0, 0]))
    print(s.largestMultipleOfThree(digits=[2, 2, 1, 1, 1]))
    print(s.largestMultipleOfThree(digits=[1, 1, 1]))
    print(s.largestMultipleOfThree(digits=[3, 1, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0]))
