#break your code

#first thing in python to use a function is keyword def

def say_hi():
    print("Hello User") #no return, but it is going to print out
print("Hey") #if it is not intended it is not a part of the function

print("TOP")
say_hi()
print("BOTTOM")

def say_hello(name):
    print("Hello " + name)

say_hello("Tina")
say_hello("Merci")

def say_some(name, age):
    print("Hello " + name + age) #  print("Hello " + name + (str)age) and you can use INT below in print

say_some("Tina", str(1))
say_some("Merci", str(2))
