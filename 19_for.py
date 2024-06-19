for letter in "Giraffe Academy": # all the values
    print(letter)

friend = ["Jim", "Karen", "Kevin"]
for anything in friend:
    print(anything)

for anything in range(len(friend)):
    print(anything)

for anything in range(len(friend)):
    print(friend[anything]) #because it would put 0 1 2

for index in range(10): #not including the value you put, and from 0
    print(index)

for index in range(3, 10): #not with 10
    print(index)

for index in range(5):
    if index == 0: #is zero
        print("first iteration")
    else:
        print("not first")