n1 = int(input("Enter a positive integer: "))
while n1 < 0:
    n1 = int(input("Enter a positive integer: "))


def bit_complement(n1):
    b_n1 = bin(n1)[2:]
    n2 = 0
    for x in b_n1:
        if x == "0":
            n2 = (str(n2) + '1')
        else:
            n2 = (str(n2) + '0')
    return int(n2, 2)


print("Complement of Base 10 of the integer ",
      n1, "is the number ", bit_complement(n1))
