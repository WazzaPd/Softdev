# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # create instance of class Flask

@app.route("/")       # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   # where will this go?
                      # it will print in the terminal
    return "No hablo queso!"

app.debug = True # prints in the terminal:
                 #  * Restarting with stat
                 #  * Debugger is active!
                 #  * Debugger PIN: 769-700-215
                 # everytime the user saves new changes
                 # in the file, it reloads the debugger
app.run()
