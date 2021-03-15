import flask
from flask import request, jsonify
import sqlite3
import os
import pandas as pd
from pandas import DataFrame
from datetime import date
from datetime import datetime
import glob


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>404</h1>
<p>not found</p>'''


@app.route('/api/v1/getnmsgs/', methods=['GET'])
def get_new_msgs():
    #args=%APIKEY%...%id/msg%
    argsn = int(request.args['args'])
    argss = argsn.split("...")
    if str(argss[1]) in open("api.keys"):
        newestMsgId = argss[1]
        curm = sqlite3.connect('./cmbs.db')
        cur = curm.cursor()
        cur.execute("SELECT * FROM MESSAGES WHERE gen_id>=" + str(newestMsgId))
        rows = cur.fetchall()
        return str(rows)
    else:
        return "API-Key invalid"


@app.route('/api/v1/putmsg/', methods=['GET'])
def get_new_msgs():
    #args=%APIKEY%...%msg%
    argsn = int(request.args['args'])
    argss = argsn.split("...")
    if str(argss[1]) in open("api.keys"):
        msg = argss[1]
        curm = sqlite3.connect('./cmbs.db')
        cur = curm.cursor()
        cur.execute("SELECT * FROM MESSAGES ORDER BY gen_id DESC")
        rows = cur.fetchall()
        fetched = False
        for row in rows:
            if not fetched:
                last_row = row
                
                fetched = True
    else:
        return "API-Key invalid"




app.run()
