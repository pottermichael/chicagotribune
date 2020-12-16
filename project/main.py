from flask import Blueprint, jsonify, render_template, url_for, request
from flask_login import login_required, current_user
from . import db
import numpy as np
import pandas as pd
import requests
import plotly
import plotly.graph_objs as go
import json

main = Blueprint('main', __name__)

"""

From Auth File


"""

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)

"""Import Data and Filter"""

#cols = ['project','use','submarket','year','gfa','developer']
#df = pd.read_csv("chicago_cbd_supply_to_date.csv",usecols=cols)
#year = 2020
#df_filt = df[
#    (df['use']=='Resi')
#    &(df['year']>=year)
#    ]
#total_gfa = df_filt.gfa.sum()
#subs = df_filt.groupby('submarket').agg({'gfa':'sum'}).sort_values('gfa',ascending=False)[0:10]

@main.route("/table", methods=("POST", "GET"))
def html_table():
    return render_template('table.html', tables=[subs.to_html(classes='data')], titles=subs.columns.values)

"""Other Routes"""

@main.route("/existing")
def existing():
    return render_template("existing.html")

@main.route("/retail")
def retail():
    return render_template("retail.html")

@main.route("/radio", methods=("POST", "GET"))
def html_radio():
    option = requests.form['options']
    return render_template('radio.html')

@main.route("/tour")
@login_required
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


@main.route("/plots")
def plots():
    bar = create_plot()
    return render_template("plots.html",plot=bar)

"""

RUN

"""

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
