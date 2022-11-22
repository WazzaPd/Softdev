from flask import Flask            #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request
import requests

app = Flask(__name__)

def get_key():
    with open('key_nasa.txt', 'r') as file:
        key = file.read()
    return key

@app.route("/", methods=['GET'])
def render():
    url = "https://api.nasa.gov/planetary/apod?api_key=" + get_key()
    print(url)
    api_call = requests.get(url).json()
    #print(api_call)

    return render_template('main.html', img_url=api_call['url'], explanation=api_call['explanation'])

if __name__ == "__main__":
    app.debug = True
    app.run()
