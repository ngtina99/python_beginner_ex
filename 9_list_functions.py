
lucky_numbers = [1, 3, 2, 4, 5,]

friend = ["Kevin", "Karen", "Jim", "Jim", "Anna"]

friend.extend(lucky_numbers)
print(friend)

friend.append("Tina")
print(friend)

friend.insert(1, "Anna") #insert on the index position
print(friend)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friend2 = friend.copy()
print("this is copy of friend: " + str(friend2))

print(friend.count("Anna")) # how many times in the list
print(friend.count("Jim"))

print(friend.index("Anna"))
#print(friend.index(Tina)) # it is not working not on the list, not a string

friend.remove("Anna") # remove just one
print(friend)

friend.pop() #remove the last element of the list
print(friend)

friend.clear() #delete all of them
print(friend)