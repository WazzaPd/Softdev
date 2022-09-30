# Joseph Wu, Nicole Zhou, Purple, Duck
# SoftDev
# K05 -- txt file and getting rid of not needed symbols
# 2022-09-29
# time spent: 1.6 hr

'''
DISCO:
1) When we set the key to different value, original value gets overwritten with new one
2) Using .split() to split strings into a list
3) "not in" checks what is not in something
QCC:
1) Each key will be the period number
2) The value of each key will have a nested list: [[devo, ducky], [devo, ducky], ...]
3) What ways can we check if the key is present in the dictionary?
OPS SUMMARY:
1) Read the file using open() and .read()
2) Use .split() to separate at '@@@'
3) Use .split() to separate at '$$$'
4) Check if the dictionary already have the key that we are trying to put in.
        (a) If not, add the key and set value [[devo, ducky]]
        (b) Otherwise, use .append() to add [devo, ducky] into the value
5) Print results
'''

import random as ran

def convert(file):
    # reading file
    krewes_file = open(file, "r")
    content = krewes_file.read()
    g = content.split("@@@")
    
    # [[pd, devo, ducky], [pd, devo, ducky], ...]
    i = 0
    while i < len(g):
        g[i] = g[i].split("$$$")
        i += 1
    
    # populating dictionary
    d = {}
    index = 0
    while index < len(g):
        x = g[index]
        if x[0] not in d:
            d[x[0]] = [[x[1], x[2]]]
        else:
            d[x[0]].append([x[1], x[2]])
        index += 1
    
    info = devo(d)
    return info

# dictionary in this format:
#   {key:[a, b], ...}
def devo(diction):
    keys = list(diction.keys())
    rand_key = ran.choice(keys)
    rand_val = ran.choice(diction.get(rand_key))
    return 'period: ' + rand_key + '\ndevo: ' + rand_val[0] + '\nducky: ' + rand_val[1]

print(convert('krewes.txt'))