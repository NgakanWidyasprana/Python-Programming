import os
os.getcwd()  # get position
  .mkdir()   # make new
  .rmdir()   # remove
  .chdir()   # move to directory
  .listdir() # list files in directoryn

# Using function to know the directory or nor

dir = "nama_file"
for name in os.listdir(dir):      # iterates the know file
   path = os.path.join(dir, name) # add to variabel path
   if os.path.isdir(path):        # check path is directory or not
       print()                    # TRUE, print
   else:
       print()                    # FALSE, print
