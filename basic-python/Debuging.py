#!/usr/bin/env python3

import csv
import datetime
import requests

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    # Decode all lines into strings
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    
    # Make a new list that will contain 
    # just variable that start from input value
    list_user = list()

    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if ((row_date >= start_date) and (row_date<=datetime.datetime.today())): 
            list_user.append(row)
    
    list_user = sorted(list_user, key=lambda row: row[3])
    
    for row in list_user:
        print("Started on {}: {} {}".format(row[3],row[1],row[0]))

def main():
    date = get_start_date()
    get_same_or_newer(date)

if __name__ == "__main__":
    main()

