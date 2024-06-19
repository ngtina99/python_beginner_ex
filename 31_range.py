numbers = range(5) #range object range(0, 5) it is always coming from 0

more_number = range(5, 10)

more_more_number = range(0, 10, 2) # you jump numbers e.g.: if you would like only even numbers

print(numbers)

for number in numbers:
    print(number)

for number in more_number:
    print(number)
    
for number in more_more_number:
    print(number)