write_file = open("25_write_file.txt", "a") # adding text at the end of the file

write_file.write("Tina") # everytime I use it is going to append inside the file

write_file.close()

write_file = open("25_write_file.txt", "w") #overwrite the whole file

write_file.write("Tina") # same.write functuin, but here we did not use append, so it rewrites the whole

write_file.close()