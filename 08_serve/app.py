'''
ADJ In The House! :: Joseph Wu, Anna Fang, Diana Akhmedova
SoftDev
K08 -- Putting it Together
2022-10-07
time spent: 0.5 hours

DISCO:
- \n does not work in Flask, we have to use <br> instead to create a new line.
- We have to have a main function, which is the first function underneath @app.route(), that will contain all other necessary funtions.
- The local variables cannot be underneath @app.route().

QCC:
- What exactly is __name__? What is __main__?
- Why can we not have multiple functions returning at the same time?
- Why is Flask a combination of Python and HTML?

OPS SUMMARY:

    RANDOM OCCUPATION GENERATOR:
    1.  Read the occupations.csv file and store it as a string
    2.  Split the string with the delimiter '\n'
    3.  Remove the insignifcant elements of the list
    4.  Initialize three dictionaries, one for storing the values and two for testing
    5.  For the rest of the elements in the list, reverse split them once with the delimiter ','
    6.  Using the list we got from rsplit, initialize all dictionaries with the key of list[0](occupations)
    7.  Store list[1] (percentage) as the value of one of the dictionaries (dict1)
    8.  Initalize the other two dictionaries with one(dict2) with the value of [percentage, 0] and the other(total): 0
    9:  Take the percentage of dict1 and multiplying it by 10, then store the key percentage*10 times in a list
    10. Using random.choice, pick a element from the list at random

    RETURNING OUTPUT IN FLASK:
    1.  We made sure to import random and Flask, as well as place the local variables above @app.route().
    2.  Then we created a main function called output() that holds and returns our other functions with new lines as formatting. This includes:
            3.  The roster() function that returns our TNPG and Roster.
            4.  The random_occupation() funtion that includes our random occupation generator code and returns the random occupation + its percentage of the workforce.
            5.  The list_occupations() funtion that returns a list of our occupation dictionary's keys.
    6.  We made sure to include a debug that will refresh anytime we save changes on this file.
'''

import random

from flask import Flask
app = Flask(__name__) # create instance of class Flask

a = open("occupations.csv")
b = a.read()

dict = {}
dict2 = {}
total = {}
txt = b.split("\n")
txt.pop() # remove last element: " "
txt.pop() # remove last element: "'Total': '99.8'"
txt.pop(0) # remove first element: "'Job Class': 'Percentage'"

@app.route("/")       # assign fxn to route

def output():
    return roster() + "<br><br>" + random_occupation() + "<br><br>" + str(list_occupations())

def roster():
    ret = "ADJ In The House! -- Joseph Wu, Anna Fang, Diana Akhmedova"
    return ret

def random_occupation():
    for x in txt:
        list = x.rsplit(",", 1)
        dict[list[0]]= float(list[1])
        a = int(float(list[1]) * 10)
        # print(a)
        dict2[list[0]] = [a, 0]
        total[list[0]] = 0
    list = []
    for x in dict:
        for y in range(0, int(dict[x]*10)):
            list.append(x)

    random_occupation = random.choice(list)
    random_percentage = dict[random_occupation]
    ret = "RANDOM OCCUPATION: " + random_occupation + "<br><br>PERCENTAGE OF US WORKFORCE: " + str(random_percentage)
    print(ret)
    print(__name__)
    return ret

def list_occupations():
    ret = "LIST OF OCCUPATIONS:"
    temp = list(dict.keys())
    for i in temp:
        ret += "<br>" + str(i)
    return ret

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
