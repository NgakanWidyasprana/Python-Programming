# Using mode permission ("r": Read, "w": Write, "a": Append)
with open("../file-object/log_test.txt","w") as file:
   # The return value of .write() is number
   # character do you add
   print(file.write("This is first write data"))




