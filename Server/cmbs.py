import sqlite3
import os
import pandas as pd
from pandas import DataFrame

#initialize Database
def initdb():
    conn = sqlite3.connect('cmbs.db')
    c = conn.cursor()
    # Create table - Messages
    c.execute('''CREATE TABLE MESSAGES
                 ([gen_id] FLOAT PRIMARY KEY,[message] text)''')
    conn.commit()
