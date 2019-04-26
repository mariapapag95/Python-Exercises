def bi2dec(num):

    "This funtion takes a binary number"
    "and converts it into a decimal number"
    "expected input= binary number"
    "expected output= digit"

    num=str(num)
    return int(num, 2)

print(bi2dec(1100))


def dec2bi(num):

    "This funtion takes a decimal number"
    "and converts it into a binary number"
    "expected input= digit"
    "expected output= binary number"
    
    return int(bin(num)[2:])

print(dec2bi(12))