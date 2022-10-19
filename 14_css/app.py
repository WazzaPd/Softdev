#Flying Karate Masters: Matthew Yee, Kevin Li, Joseph Wu
#SoftDev
#K14 -- Serve CSS
#2022-10-19
#time spent: 0.2 hours

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def show_website():
    return render_template('index.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()