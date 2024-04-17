from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'app no' + requests.get('http://webshahaf:9000/').text

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7777)
