import csv

data=[["Ngakan","@gmail.com"],["Diah","@yahoo.com"]]

with open('../file-object/email.csv','w') as email:
   write= csv.writer(email)
   write.writerows(data)
