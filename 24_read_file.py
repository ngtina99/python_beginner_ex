read_file = open("24_read_file.txt", "r") #read

print(read_file.readable()) # true if it is readable

#print(read_file.readline()) # with a newline at the end
#print(read_file.read())
#print(read_file.readline()) #first line but it is already read, so it is going to give empty here
#print(read_file.readline()) #second line
#read_file.close() # you have to close once you read
#open("read_file", "w") #write
#open("read_file", "a") #append, you can not change just add
#open("read_file", "r+") #read an write

for file in read_file.readlines(): #with readline it is just one by one char
    print(file)
read_file.close()