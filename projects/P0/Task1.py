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


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Using sets, O(n)
tel_nums = set()
for line in texts + calls:  # O(n)
    tel_nums.add(line[0])  # O(1)
    tel_nums.add(line[1])  # O(1)

print(f'There are {len(tel_nums)} different telephone numbers in the records.')
