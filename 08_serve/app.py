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
    return roster() + "<br><br>" + random_occupation()

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

# def list_occupations():
#     return list(dict.keys())

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()