import csv
f = open("../file-object/csv_file.txt")
csv_f=csv.reader(f)
for row in csv_f:
   name, nim, role = row
   print("Name: {},Nim: {},Role: {}".format(name,nim,role))


