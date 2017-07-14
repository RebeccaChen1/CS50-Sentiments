from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count=100)
    positive = 0
    negative = 0
    neutral = 0
    
    # runs analyses on tweets
    for i in range(len(tweets)):
        analyzer = Analyzer()
        score = analyzer.analyze(tweets[i])
    
        if score > 0.0:
            positive = positive + 1
        elif score < 0.0:
            negative = negative + 1
        else:
            neutral = neutral + 1
    # calculates percentages of each 
    positive = (positive/50)*100
    negative = (negative/50)*100
    neutral = (neutral/50)*100

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
