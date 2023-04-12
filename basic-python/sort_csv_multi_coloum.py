import csv
from datetime import datetime

# open the file for reading and writing
with open("test.csv", mode='r+', newline='') as f:

   # create a reader and writer opbject
    reader, writer = csv.reader(f), csv.writer(f)
    
    data = list()
    # iterate through the reader and update column 0 to a datetime date string
    for row in reader:

        # update column 0 to a datetime date string
        row[0] = datetime.strptime(row[0], "%d-%b-%y").date().isoformat()
        
        # append the row to data
        data.append(row)

    # sort all of the rows, based on date, with a lambda expressio

    data = sorted(data, key=lambda row: row[3])

    # change the stream position to the given byte offset
    f.seek(0)

    # truncate the file size
    f.truncate()

    # add a header to data
    data.insert(0, ['date', 1, 2, 3, 4, 5])

    # write data to the file
    writer.writerows(data)