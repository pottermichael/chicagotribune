from flask import Flask, render_template, url_for, redirect
import pandas as pd
import requests


app = Flask(__name__)

"""
scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'chicagodowntowndevelopments-62ea5fbc2a1e.json', scope)
gc = gspread.authorize(credentials)
cbd = gc.open("ChicagoNewConstruction").sheet1
data = cbd.get_all_values()
headers = data.pop(0)
#create dataframe and convert all available column to floats
df = pd.DataFrame(data, dtype=float, columns=headers)
df_mod=df.nsmallest(5,'gfa')
"""
@app.route("/")
def existing():
    return render_template("existing.html")

@app.route("/retail")
def retail():
    return render_template("retail.html")

@app.route("/table", methods=("POST", "GET"))
def html_table():
    return render_template('table.html', tables=[df_mod.to_html(classes='data')], titles=df_mod.columns.values)

@app.route("/radio", methods=("POST", "GET"))
def html_radio():
    option = requests.form['options']
    return render_template('radio.html')

@app.route("/tour")
def tour():
    return render_template("tour.html")

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
