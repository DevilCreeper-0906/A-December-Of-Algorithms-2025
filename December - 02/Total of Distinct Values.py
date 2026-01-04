def convert(num, base):
    digits = "0123456789ABCDEF"
    res = ""

    while num > 0:
        rem = num % base
        res = digits[rem] + res
        num = num // base

    return res

N = int(input())

width = len(convert(N, 2))


for i in range(1, N + 1):
    dec = str(i)
    octal = convert(i, 8)
    hexa = convert(i, 16)
    binary = convert(i, 2)

    print(
        " " * (width - len(dec)) + dec,
        " " * (width - len(octal)) + octal,
        " " * (width - len(hexa)) + hexa,
        " " * (width - len(binary)) + binary
    )


