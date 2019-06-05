"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

uniqueNumbers = set()

# Find all unique numbers in texts
for text in texts:
    uniqueNumbers.add(text[0])
    uniqueNumbers.add(text[1])

# Find all unique numbers in calls
for call in calls:
    uniqueNumbers.add(call[0])
    uniqueNumbers.add(call[1])

print("There are", len(uniqueNumbers),
      "different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
