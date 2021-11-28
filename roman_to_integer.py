def romanToInt(s: str) -> int:
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum, tmp = 0, ""
    for x in s:
        if x == "V" and tmp == "I":
            sum = sum + 3
        elif x == "X" and tmp == "I":
            sum = sum + 8
        elif x == "L" and tmp == "X":
            sum = sum + 30
        elif x == "C" and tmp == "X":
            sum = sum + 80
        elif x == "D" and tmp == "C":
            sum = sum + 300
        elif x == "M" and tmp == "C":
            sum = sum + 800
        else:
            sum = sum + dict[x]
        tmp = x
    return sum

# print(romanToInt("MCMXCIIIV"))


def cheekyRoman(s: str) -> int:
    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = s.replace("IV", "IIII").\
        replace("IX", "VIIII").\
        replace("XL", "XXXX").\
        replace("XC", "LXXXX").\
        replace("CD", "CCCC").\
        replace("CM", "DCCCC")
    sum = 0
    for x in s:
        sum = sum + dict[x]
    return sum


print(cheekyRoman("MCMXCIIIV"))
