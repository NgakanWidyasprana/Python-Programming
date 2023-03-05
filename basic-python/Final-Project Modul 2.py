import sys
import re
import operator
import csv

# Make 2 Dictionary
list_user = {}
list_error = {}

with open("basic-python\syslog.log") as files:
    for text in files.readlines():
        result_match = re.search(r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$",text)

        if result_match != None:
            code, error, user = result_match.group(1), result_match.group(2), result_match.group(3)

        # Calculates the Error Message
        if error not in list_error.keys():
            list_error[error]=1
        else:
            list_error[error]+=1

        # Calculated the User
        if user not in list_user.keys():
            list_user[user] = {}
            list_user[user]["INFO"] = 0
            list_user[user]["ERROR"] = 0
        
        if code == "INFO":
            if user not in list_user.keys():
                list_user[user]={}
                list_user[user]["INFO"]=0
            else:
                list_user[user]['INFO'] +=1
        elif code == "ERROR":
            if user not in list_user.keys():
                list_user[user] = {}
                list_user["INFO"] = 0
            else:
                list_user[user]["ERROR"] +=1

# Sorted Ascending & orted Username
error_completion = sorted(list_error.items(), key=operator.itemgetter(1), reverse=True)
per_user_list = sorted(list_user.items(), key=operator.itemgetter(0))
files.close()

# Insert at the beginning of the list
error_completion.insert(0, ('Error', 'Count'))

# * Create CSV file user_statistics
with open('user_file.csv', 'w', newline='') as user_csv:
    for key, value in per_user_list:
        user_csv.write(str(key) + ',' +
                       str(value['INFO']) + ',' + str(value['ERROR'])+'\n')

# * Create CSV error_message
with open('error_file.csv', 'w', newline='') as error_csv:
    for key, value in error_completion:
        error_csv.write(str(key) + ',' + str(value)+'\n')