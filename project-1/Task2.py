"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# process call lengths

callLength = {}
for call in calls:
    callLength[call[0]] = callLength.get(call[0], 0) + int(call[3])
    callLength[call[1]] = callLength.get(call[1], 0) + int(call[3])

longestCall = max(callLength, key=callLength.get)

print(longestCall, "spent the longest time,", callLength[longestCall],
      "seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
