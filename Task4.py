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

telemarketers = set()

# Create set with numbers that make outgoing calls
for call in calls:
    telemarketers.add(call[0])

# Remove numbers that receive incoming calls
for call in calls:
    telemarketers.discard(call[1])

# Remove numbers that receive incoming texts or send texts
for text in texts:
    telemarketers.discard(text[0])
    telemarketers.discard(text[1])

telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers: ")
for number in telemarketers:
    print(number)

# Performance
# The program should run in O(4n) if not
# considering the runtime of the built in python functions

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
