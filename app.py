
from flask import Flask, jsonify, render_template, request, flash, redirect


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc,select

import pandas as pd
import numpy as np

d = pd.read_html('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India')
df = d[7].iloc[:-2]
df.columns = ['SN', 'STATE_UT', 'ACTIVE_CASES', 'DEATHS', 'RECOVERIES', 'TOTAL'] 
df1 = df.iloc[:-1]
df2 = df.tail(1)
final_df = pd.concat([df2, df1]).reset_index(drop=True)
final_df['STATE_UT'] = final_df['STATE_UT'].map(lambda x: x.rstrip(' †'))
final_df.set_value(0, 'STATE_UT', 'All India') 

dd = pd.read_html('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India')
state_df = dd[6].iloc[:-4]
state_df.fillna(0, inplace=True)
state_df = state_df.iloc[:, :-4]
state_df = state_df.drop(state_df.columns[len(state_df.columns)-2], axis=1)
ColumnName = final_df['STATE_UT'].tolist()
ColumnName.append(ColumnName.pop(ColumnName.index('All India')))
ColumnName.insert(0, "Date")
state_df.columns = ColumnName

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("myindex.html")

@app.route('/names')
def names():
    """Return a list of sample names."""
    return jsonify(list(final_df.STATE_UT))

@app.route('/metadata/<state>')
def sample_metadata(state):
    """Return the MetaData for a given State."""
    state_metadata = {}
    state_metadata['Active Cases'] = final_df[final_df['STATE_UT']==state]['ACTIVE_CASES'].to_string(index=False)
    state_metadata['Recoveries'] = final_df[final_df['STATE_UT']==state]['RECOVERIES'].to_string(index=False)
    state_metadata['Deaths'] = final_df[final_df['STATE_UT']==state]['DEATHS'].to_string(index=False)
    state_metadata['TOTAL'] = final_df[final_df['STATE_UT']==state]['TOTAL'].to_string(index=False)
    return jsonify(state_metadata)
    
@app.route('/dates')
def sample_homedata():
    """Return all dates."""
    return jsonify(list(state_df.Date))  

@app.route('/statedata/<state>')
def state_data(state):
    """Return state related data."""
    return jsonify(list(state_df[state]))
 
@app.route('/total')
def all_india_data():
    """Return all dates."""
    return jsonify(list(state_df["All India"]))  
  

if __name__ == "__main__":
    app.run(debug=True)
   
    