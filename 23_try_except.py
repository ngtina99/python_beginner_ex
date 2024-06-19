try:
    value = 10/0 # it is catching this error, not just the input, but inside the code as well
    number = int(input("Enter a number: "))
    print = number
except ZeroDivisionError as err: #these are predefined errors, and if you give a variable name and it will define the problem
    print(err)  # it is bettern than if, because if any error it is catching and coming here
except ValueError:
    print("invalid value")