# Using OS module to manipulating files.

import os
os.remove("name_file")
os.rename("old_name","new_name")

# Check file exist or not
os.path.exist("name_file")

# Check the size
os.path.getsize("name_files")

# Get time in file you can use os module
# or can use datetime module

# Get timestamp from 1970 Janury
os.path.getmtime("name_files")
# Result
15767...... (bunch of number)

import datetime
time_value= os.path.getmtime("nama_files")
datetime.datetime.fromtimestamp(time_value)
# Result
datetime.datetime(year, time, time,....)

# Get PATH
os.path.abspath("name_files")
