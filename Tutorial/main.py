from flask import Flask, render_template
from flask import Response, jsonify
import json
import collections
app = Flask(__name__)

@app.route("/")
def hello():
    return "Sever running OK! This is to follow tutorial in http://www.codeproject.com/Articles/693841/Making-Dashboards-with-Dc-js-Part-1-Using-Crossfil"

@app.route('/crossfilter')
def crossfilter():
    return render_template("part1.html")
	
@app.route('/crossfilter2')
def crossfilter2():
    return render_template("part2.html")

@app.route('/crossfilter2_ext_data')
def crossfilter2_ext_data():
    return render_template("part2_ext_data.html")

if __name__ == "__main__":
    app.run()