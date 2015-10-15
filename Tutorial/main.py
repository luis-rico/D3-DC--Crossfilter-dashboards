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
	
@app.route('/crossfilter3')
def crossfilter3():
    return render_template("part3.html")
	
@app.route('/cont1')
def cont1():
    return render_template("cont1.html")
	
@app.route('/cont2')
def cont2():
    return render_template("cont2.html")
	
@app.route('/sysviews1')
def sysviews1():
    return render_template("SystemViews1.html")
	
@app.route('/sysviews2')
def sysviews2():
    return render_template("SystemViews2.html")
	
@app.route('/sysviews3')
def sysviews3():
    return render_template("SystemViews3.html")
	
## Not working, it would seem that the two rowChart fight against each other and no results are produced !
## This page shows two rowcharts interacting in the same dashboard
## http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/
## This FAQ page in section "Why do two charts on the same dimension not filter each other?" may shed some light on this issue
## https://github.com/dc-js/dc.js/wiki/FAQ
@app.route('/sysviews4')
def sysviews4():
    return render_template("SystemViews4.html")
	
@app.route('/sysviews5')
def sysviews5():
    return render_template("SystemViews5.html")

# Using a keen.io template	
@app.route('/sysviews6')
def sysviews6():
    return render_template("index.html")
	
# Using a custom (LHR) keen.io template	
@app.route('/sysviews7')
def sysviews7():
    return render_template("indexLHR.html")
	
@app.route('/sysviews8')
def sysviews8():
    return render_template("indexLHR_2.html")
	
#References for scrollable tables
#http://jsfiddle.net/borgboyone/gbkbhngq/
#https://www.datatables.net/

## Attempt using datatables
## Now working after sysviews10 was successful
@app.route('/sysviews9')
def sysviews9():
    return render_template("indexLHR_3.html")
	
## Attempt using datatables only as it couldn't work above
@app.route('/sysviews10')
def sysviews10():
    return render_template("dataTable_only.html")

	
## sysviews9 + Bubble Chart
## Bubble chart instead of Data Table
@app.route('/sysviews11')
def sysviews11():
    return render_template("indexLHR_4.html")

## Bubble chart wip
@app.route('/sysviews12')
def sysviews12():
    return render_template("indexLHR_5.html")
	
## Bubble chart wip2 (alternativa)
@app.route('/sysviews13')
def sysviews13():
    return render_template("indexLHR_6.html")

## Bubble chart full classication (as opposed to top 10)
## sysviews11, 12 and 13 still not working
@app.route('/sysviews14')
def sysviews14():
    return render_template("indexLHR_7.html")
	
if __name__ == "__main__":
    app.run()