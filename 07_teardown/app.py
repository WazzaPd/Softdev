"""
AJJ Eating Blue Pho: Joseph Wu, Jun Hong Wang, Anjini Katari
07_teardown
SoftDev period 7
2022-10-03
time spent: 0.5 hrs
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* We can see what's returned in the webpage itself, as plain text.
* There's no value for name, so the name doesn't show.
* The __name__ convention (2 underscores before and after var name) might be Python OOP convention
QCC:
0. Looks like a constructor from object oriented programming, like Java from last year.
1. Could refer to location (like in local files?), based on what route means, as well as the meaning of / in the terminal.
2. Print to webpage?
3. Doesn't print anything, since we don't know what name is, but when we assign a value to name, then it might print something. 
4. Since it's return, it probably won't say anything until we print it. However, since it launches a webpage, it might be visible somewhere there, like in the console. 
5. app.run() looks like it's making the object app do something, like in an object-oriented programming language
* What does the @ in front of app.route() mean?
* Why is the flask module missing? Do we need to have it installed for this to work?
* From flask import Flask might assume that we have to have flask downloaded.
* What does flask do?
* We think that the link this program returns is a local link, which is why when we copy-pasted it from the lab computer to my actual computer, the link didn't work.
...
INVESTIGATIVE APPROACH:
At first, it was mainly based on inference and assumption, but we got to see the link for a few minutes, and that answered some questions.
However, at home, we couldn't open the link, so we had to assume again.
* Noticed possibly object-oriented conventions
* thought about app.route() and its function
* thought about what would be displayed when printed and returned
* at home, we couldn't get the link, so we assumed that we needed to have a local copy of flask
'''
