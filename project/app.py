from flask import Flask, render_template, url_for, redirect
import numpy as np
import pandas as pd
import requests
import plotly
import plotly.graph_objs as go
import json

app = Flask(__name__)

"""Import Data and Filter"""

cols = ['project','use','submarket','year','gfa','developer']
df = pd.read_csv("data/chicago_cbd_supply_to_date.csv",usecols=cols)
year = 2020
df_filt = df[
    (df['use']=='Resi')
    &(df['year']>=year)
    ]
total_gfa = df_filt.gfa.sum()
subs = df_filt.groupby('submarket').agg({'gfa':'sum'}).sort_values('gfa',ascending=False)[0:10]

@app.route("/table", methods=("POST", "GET"))
def html_table():
    return render_template('table.html', tables=[subs.to_html(classes='data')], titles=subs.columns.values)

"""Other Routes"""

@app.route("/")
def existing():
    return render_template("existing.html")

@app.route("/retail")
def retail():
    return render_template("retail.html")

@app.route("/radio", methods=("POST", "GET"))
def html_radio():
    option = requests.form['options']
    return render_template('radio.html')

@app.route("/tour")
def tour():
    return render_template("tour.html")

"""

PLOTLY GRAPH & CHART INFORMATION

"""

def create_plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

    dta = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(dta, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route("/plots")
def plots():
    bar = create_plot()
    return render_template("plots.html",plot=bar)

"""

RUN

"""

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
