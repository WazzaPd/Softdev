import random as rng

"""
AJJ Eating Blue Pho: Joseph Wu, Jun Hong Wang, Anjini Katari
04_choose
SoftDev period 7
2022-09-22

DISCO:
When importing a package, make sure to use the package name before the function.
For example, rng.randint(0,2)

.keys() access the keys in an dictionary

QCC:
OPS SUMMARY:
-choose a list first, then a devo from that list
-but how to randomly choose a list?

1) Testing with random and random package
2) Figured out how to use key to get value in dictionary
3) Figured out how to randomly choose a key
4) Randomly choose developer out of chosen list
"""

krewes = {2:['Ivan', 'Talia', 'Julia'], 7:['Joseph', 'Jun Hong', 'Anjini'], 8:['Gordon', 'Joshua', 'Yuki']}

def choosedev(dictionary):
    period = rng.randint(0,2)
    devs = []
    if period == 0:
        devs = krewes[2]
    elif period == 1:
        devs = krewes[7]
    else:
        devs = krewes[8]
    return devs[rng.randint(0, len(devs) - 1)]

def devo(diction):
    keys = list(diction.keys())
    rand_key = rng.choice(keys)
    rand_val = rng.choice(diction.get(rand_key))
    return rand_val

def randomtesting():
    return rng.randint(0,2)

def testing():
    print(choosedev(krewes))
    print(devo(krewes))

    
testing()