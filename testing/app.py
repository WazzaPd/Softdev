from flask import Flask            #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def render():
    url = "https://api.countapi.xyz/hit/ThisIsForMeOnly/key"
    print(url)
    api_call = requests.get(url).json()
    #print(api_call)

    return render_template('main.html', pressed=api_call['value'])

@app.route("/adding", methods=['GET'])
def adding():
    url = "https://api.countapi.xyz/hit/ThisIsForMeOnly/key"
    print(url)
    api_call = requests.get(url).json()
    return render_template('main.html', pressed=api_call['value'])


if __name__ == "__main__":
    app.debug = True
    app.run()
