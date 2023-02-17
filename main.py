from flask import Flask,render_template
import json
from model import predictDisease

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return '<h2>Hello from Flask!</h2>'

@app.route('/prusinfo/<string:info>', methods=['POST'])
def prusinfo(info):
    output = json.loads(info)
    syms = output['query']
    print(syms)
    print(predictDisease(syms))
  
app.run(
  host = "0.0.0.0", # or 127.0.0.1
  port = 8080,  # this will allow us to easily fix problems and bugs
)
