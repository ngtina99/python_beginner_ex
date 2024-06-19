# Jan->January
# Feb->February

monthConversions = {
    "Jan": "January",
    "Feb": "February", # etc, could be any amount
}

print(monthConversions["Jan"]) # I refer to the index, it is not a function
#print(monthConversions["January"]) it is not going to work Keywerror

print(monthConversions.get("Something"))

print(monthConversions.get("Something", "Not a valid key")) #get second argument if it is not found

print(monthConversions.get("Jan", "Not a valid key")) # it is going to get the pair

monthConversions = {
    1: "One",
    2: "Two", # etc, could be any amount
}

print(monthConversions[1]) # it is working with integers too, and the pair could be another type

something = {a:2, b:3}
print(something)