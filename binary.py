def int_to_binary(num):
    if num == 0:
        return 0
    
    binary = ""

    while num>0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num//2

    return binary

print(int_to_binary(5))


def binary_to_int(binary):
    binary = binary[::-1]
    
    num = 0
    for i in range(len(binary)):
        if int(binary[i]) == 1:
            num += 2**i

    return(num)

print(binary_to_int('10111'))   

