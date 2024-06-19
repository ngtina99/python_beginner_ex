is_female = True
is_tall = False

if is_female:
    print("True") # you can put anything until is intended
else:
    print("False")

if is_female or is_tall: # you can combinate
    print("True or")
else:
    print("False and")

if is_female and is_tall: # you can combinate
    print("True and")
else:
    print("False and")

if is_female and is_tall: # you can combinate
    print("True and")
elif is_female and not(is_tall): # elif and not() syntax
    print("elif true with not tall")
else:
    print("False and")