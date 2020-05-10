def findComplement( num: int):

    bit = 1
    temp = num
    while temp:
        num = num ^ bit
        bit = bit << 1
        temp = temp >> 1
    return num
#         num = bin(num)

#         num = int(num)
#         return num
print(findComplement(6)) 