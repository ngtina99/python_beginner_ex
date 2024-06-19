print(2**3) #2^3 print(pow(2, 3))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))

def raise_pow(base_num, pow_num):
    result = 1
    i = 0
    while i < pow_num:
        result = result * base_num
        i += 1
    return(result)

print(raise_to_power(2, 3))
