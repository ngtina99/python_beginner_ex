#you can NOT change or modify, it is immutable, you can access easily

coordinates = (4, 5, "string")
print(coordinates[2]) #index position

print(coordinates.count(4)) # how many four inside it
print(coordinates.index(5)) # give the index of the number in the tuple

list_of_coordinates = [(4, 5), (8, 5), (6, 9)]
print(list_of_coordinates)

#coordinates[1] = 10 #gives an eror

list_of_coordinates.append((2, 3)) # because it is a list you can not do on tuples
print(list_of_coordinates)