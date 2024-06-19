def cube(num):
    num*num*num

print(cube(3)) #nothing happen

def cube(num):
    return num*num*num # you can not place anything after it

print(cube(3)) #it is return

def cube(num):
    return num*num*num

result = cube(3)
print(result)