# 31 - Working with CSV and Pickling 
## Reading CSV Files
- CSV files are a commmon file format for tabular data
- We can read CSV files just like other text files
- Python has a built-in CSV module to read/write CSVs more easily

## CSV Module
- `reader`: Lets you iterate over rows of the CSV as lists
- `DictReader`: lets you iterate over rows of the CSV as OrderedDicts

```python

# Read a CSV file and prints two rows, 'First Name' and 'Second Name'

import csv

def print_users():
    with open('users.csv') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            print('{} {}'.format(row['First Name'], row['Last Name']))
```

## Writing CSV Files using lists
- `writer`: creates a writer object for writing to CSV
- `writerow`: method on a writer to write a row to the CSV
```python

# Write a CSV file two rows, first_name and last_name

import csv
 
def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])
```

## Writing CSV Files using dictionaries
- `DictWriter`: creates a writer object for writing using dicitionaries
- `fieldnames`: kwarg for the DictWriter specifying headers
- `writeheader`: method on a writer to write header row
- `writerow`: method on a writer to write a row based on a dictionary


