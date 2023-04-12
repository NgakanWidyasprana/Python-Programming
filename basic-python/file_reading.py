# Using to open a file
file=open("../file-object/lagu_indo_1.txt")

# Print one-line
print(file.readline())

# Print all-line
print(file.read())

# Close file
file.close()

# If you want don't want to forget using
# .close() functions, you cant use 'with'

with open("../file-object/lagu_indo_1.txt") as file:
   print(file.read())
