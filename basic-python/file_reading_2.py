# Now using a for loop to reading a files

with open("../file-object/lagu_indo_1.txt") as file:
   for line in file:
     print(line.upper())

# If you just using line.upper()
# the result will have space in each line
# add .strip() to remove it

with open("../file-object/lagu_indo_1.txt") as file:
   for line in file:
     print(line.strip().upper())

# Add lines to a list
file=open("../file-object/lagu_indo_1.txt")
lines=file.readlines()
file.close()

# Sort lines
lines.sort()
print(lines)
