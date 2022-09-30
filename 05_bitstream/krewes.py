import random as ran
'''
DISCO:
1) When we set the key to different value, original value gets overwritten with new one
2) Using .split to split strings into a list
3) range() to use int in a for loop
QCC:
1) How will be add more values to the keys?
OPS SUMMARY:
1) Read the file using open() and .read()
2) Use .split() to separate at '@@@'
3) Use .split() to separate at '$$$'
4) Check if the dictionary already have the key that we are trying to put in.
        (a) If not, add the key and set value [[devo, ducky]]
        (b) Otherwise, use .append() to add [devo, ducky] into the value
5) Print results

'''

def convert(file):
    krewes_file = open(file, "r")
    content = krewes_file.read()
    seperated = content.split('@@@')
    Big_gnome = []
    d = {}
    for n in range(len(seperated)):
        gnome = seperated[n].split('$$$')
        Big_gnome.append(gnome)
    
    #find if 0th element is/isnt a key
    for n in range(len(Big_gnome)):
        cut = Big_gnome[n]
        not_there = True
        for n in list(d):
            if n == cut[0]:
                not_there == False
        
        #create new key and empty list
        if not_there:
            d[cut[0]] = []
        
        #add values to existing keys
        for n in d:
          if cut[0] == n:
              d[n].append([cut[1],cut[2]])
    return d

def select(d):
    keys = list(d.keys())
    rand_key = ran.choice(keys)
    rand_val = ran.choice(d.get(rand_key))
    rand_val.insert(0,rand_key)
    return rand_val

def testing():
    print(select(convert('krewes.txt')))
    
testing()

def convert_2(file):
    krewes_file = open(file, "r")
    content = krewes_file.read()
    g = content.split("@@@")
    
    # [[pd, devo, ducky], [pd, devo, ducky], ...]
    i = 0
    while i < len(g):
        g[i] = g[i].split("$$$")
        i += 1
    
    d = {}
    index = 0
    while index < len(g):
        # existing_keys = list[d.keys()]
        x = g[index]
        if x[0] not in d:
            d[x[0]] = [[x[1], x[2]]]
        else:
            d[x[0]].append([x[1], x[2]])
        index += 1
    
    info = devo(d)
    
    return info
#     x = g[0]
#     return x[0]

def devo(diction):
    keys = list(diction.keys())
    rand_key = ran.choice(keys)
    rand_val = ran.choice(diction.get(rand_key))
    return 'period: ' + rand_key + '\ndevo: ' + rand_val[0] + '\nducky: ' + rand_val[1]

print(devo(convert('krewes.txt')))



