from flask import Flask            #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def render():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    print(url)
    api_call = requests.get(url).json()
    print(api_call)

    return render_template('main.html', explanation=api_call['text'])

if __name__ == "__main__":
    app.debug = True
    app.run()
