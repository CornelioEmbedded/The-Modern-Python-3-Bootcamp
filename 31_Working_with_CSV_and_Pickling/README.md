# 31 - Working with CSV and Pickling 
## Reading CSV Files
- CSV files are a commmon file format for tabular data
- We can read CSV files just like other text files
- Python has a built-in CSV module to read/write CSVs more easily

## CSV Module
- `reader`: Lets you iterate over rows of the CSV as lists
- `DictReader`: lets you iterate over rows of the CSV as OrderedDicts

## Writing CSV Files using lists
- `writer`: creates a writer object for writing to CSV
- `writerow`: method on a writer to write a row to the CSV

## Writing CSV Files using dictionaries
- `DictWriter`: creates a writer object for writing using dicitionaries
- `fieldnames`: kwarg for the DictWriter specifying headers
- `writeheader`: method on a writer to write header row
- `writerow`: method on a writer to write a row based on a dictionary
