from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
    msg = "happy birthday {name}"
    return msg.format(name = os.getenv("NAME","john"))

app.run(host='0.0.0.0', port=81)
