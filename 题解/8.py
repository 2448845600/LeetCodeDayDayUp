import re


def myAtoi(str: str) -> int:
    symbol = ""
    digital_str = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num_str = ""
    for c in str:
        if symbol == "":
            if c == " ":
                continue
            elif c == "-" or c == "+":
                symbol = c
            elif c in digital_str:
                symbol = "+"
                num_str += c
            else:
                return 0
        else:
            if c in digital_str:
                num_str += c
            else:
                break

    start = 0
    for i in range(len(num_str)):
        if num_str[i] == "0":
            start = i
        else:
            break
    num_str = num_str[start:]

    if len(num_str) > 10:
        res = 2147483647 if symbol == "+" else -2147483648
        return res
    if len(num_str) == 10:
        MAX = 2147483647 + (symbol == "-")
        MAX, b = divmod(MAX, 10)
        MAX_str = "" + chr(ord('0') + b)
        while MAX > 0:
            MAX, b = divmod(MAX, 10)
            MAX_str += chr(ord('0') + b)
        MAX_str = MAX_str[::-1]
        for i in range(len(num_str)):
            if ord(MAX_str[i]) > ord(num_str[i]):
                break
            elif ord(MAX_str[i]) == ord(num_str[i]):
                continue
            else:
                res = 2147483647 if symbol == "+" else -2147483648
                return res

    res = 0
    for i in range(len(num_str)):
        res = res * 10
        num = (ord(num_str[i]) - ord('0'))
        res += num
    res = res * (1 if symbol == "+" else -1)
    return res


def myAtoiPlus(str: str) -> int:
    # '+'：前面一个字符的一个或多个
    # error example: "+"
    # res = re.findall('^[\+\-]?\d*')

    # '*'：前面一个字符的0个或多个
    # error example: "   -110"
    # res = re.findall('^[\+\-]?\d+')

    res = re.findall('^[\+\-]?\d+', str.lstrip())
    # res = int(res[0])
    res = int(*res) # 防止返回的res为空，*表示解包，而且int([]) = 0
    res = max(min(res, 2 ** 31 - 1), -2 ** 31)
    return res


if __name__ == '__main__':

    for i in ["2147483800", "2147483646", "2147483647", "2147483648"]:
        a = re.findall('^[\+\-]?\d*', i.lstrip())
        print(int(a[0]))
        res = max(min(int(a[0]), 2 ** 31 - 1), -2 ** 31)
        print(res)
        print(myAtoi(i))
