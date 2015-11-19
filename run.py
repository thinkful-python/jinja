#!/usr/bin/python

import datetime

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html', my_string="Wheeeee!",
                           my_list=[0,1,2,3,4,5], current_time=datetime.datetime.now())
@app.template_filter() 
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """Convert a date time to a different format"""
    return value.strftime(format)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
