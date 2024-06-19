def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(1, 2, 3)) # it is going to give the biggest one

def equal_num (num1, num2):
    if num1 == num2:
        return num1
    else:
        return num2

print(equal_num(1, 2)) 

def notequal_num (num1, num2):
    if num1 != num2:
        return num1
    else:
        return num2

print(notequal_num(1, 2)) 