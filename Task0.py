"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print("First record of texts,",
          texts[0][0], "texts", texts[0][1], "at time", texts[0][2])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print("Last record of calls,",
          calls[-1][0], "calls", calls[-1][1], "at time", calls[-1][2], "lasting", calls[-1][3], "seconds")

# Performance
# The program should run in O(1) if not
# considering the runtime of the built in python functions
# like stepping through a list.

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""