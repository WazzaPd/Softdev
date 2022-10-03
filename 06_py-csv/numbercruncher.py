# Joseph Wu, Purple, Nicole Zhou, Duck
# SoftDev
# K06 -- return random weighted by percentage
# 2022-10-02
# time spent: 1.5 hrs

'''
DISCO:
1) random.choice() and weight returns weighted random
QCC:
1) What are some other ways to separate occupation and percentages?
OPS SUMMARY:
1) Read the file using open() and read()
2) Use .split() to separate at '\n'
3) Separate each occupation and percentage
4) Use random.choice() and weight
'''
# STIL IN PROGRESS

import random

occupation_file = open('occupations.csv', 'r')
content = occupation_file.read()

# ['occupation, percentage', 'occupation, percentage', ...]
g = content.split('\n')

# [['occupation', 'percentage'], ['occupation', 'percentage'], ...]
i = 0
while i < len(g):
    g[i] = g[i].split(',')
    if len(g[i]) > 2:
        index = 1
        x = g[i]
        while index < len(g[i]):
            x[0] + x[index]
            index += 1
        x[0].strip()

    i += 1

# populating dictionary
d = {}
j = 0
while j < len(g):
    y = g[index]
    d[y[0]] = y[1].strip()

d.pop('Job Class')
total = d.pop('Total').strip()
values = list(d.values())
keys = list(d.keys())

print(random.choices(keys, weights=values))
