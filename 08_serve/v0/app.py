# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # What do the underscores between name mean?

@app.route("/") # This part of the code routes the return of hello_world() onto a web page.\
                # The "/" stands for the root of the directory.
def hello_world():
    print(__name__) # print() will print "__main__" in the terminal.
    return "No hablo queso!"  # return will display on the web page.

app.run()  # run() runs the program.
                
