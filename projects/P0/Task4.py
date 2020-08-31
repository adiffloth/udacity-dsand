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

candidates = set()
exclude = set()

for call in calls:  # O(n)
    candidates.add(call[0])  # O(1)
    exclude.add(call[1])  # O(1)

for text in texts:  # O(n)
    exclude.add(text[0])  # O(1)
    exclude.add(text[1])  # O(1)

print('These numbers could be telemarketers: ')
print(*sorted(candidates - exclude), sep='\n')  # O(nlogn) for the sort, O(n) for the set difference
