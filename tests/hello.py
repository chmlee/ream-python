from flask import Flask, render_template
import ream.convert

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    ream_dict = ream.convert.convert("template.md", "template.json")
    return render_template('main.jinja2', ream_dict=ream_dict)
