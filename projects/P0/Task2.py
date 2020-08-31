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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# Dict in python is O(1) in the average case.
# Worst case is O(n) if the hash function has completely broken down.
# O(n) to iterate over list, O(1) or O(n) to set item in dict.
# So either O(n^2) or O(n), depending on how pessimistic you want to be about the hash function.
call_minutes = {}
for call in calls:  # O(n)
    call_minutes[call[0]] = int(call_minutes.get(call[0], 0)) + int(call[3])  # O(1), average case
    call_minutes[call[1]] = int(call_minutes.get(call[1], 0)) + int(call[3])  # O(1), average case

winner = max(call_minutes, key=call_minutes.get)  # O(n)
print(f'{winner} spent the longest time, {call_minutes[winner]} seconds, on the phone during September 2016.')
