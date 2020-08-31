import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

first, second = [[item[0], item[1]] for item in calls]
print(type(first))
print(first[:10])
print(type(second))
print(second[:10])

# first, second = [item[:1] for item in calls]
