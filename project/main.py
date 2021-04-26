from flask import Blueprint, jsonify, render_template, url_for, request, make_response
from flask_login import login_required, current_user
from . import db
import numpy as np
import pandas as pd
import requests
import os
import plotly
import plotly.graph_objs as go
import json
from geopy import distance


main = Blueprint('main', __name__)


@main.route("/ajar", methods=["GET","POST"])
def ajar():
    year_one=2000
    if request.method == "POST" and request.is_json:
        #print body of response as json or test method, status, etc
        print("raw request as json")
        print(request.data)
        #convert from json to python dict?
        req = request.get_json()
        print("coverted to python dict?")
        print(req)
        #convert request to a response to send back
        response = {
            #"message": "JSON received",
            "slide": req.get("slide"),
            "year": req.get("year")+7,
            "gfa": req.get("gfa")*2,
            "sponsor": req.get("sponsor")
        }
        #print response
        print("response object to be sent back to html")
        res = make_response(jsonify(response),200)
        print(res)
        slider_proxy = int(response["slide"]) * 6
        print(slider_proxy)
        return res
    else:
        tool = ["its","not","working","ok?"]
        resz = {
            "message": "No JSON Received",
            "nombre": tool[-1],
            }
        res = make_response(jsonify(resz),200)
        print(res)
        return render_template("ajar.html", res=res, tool=tool, first=year_one)

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

"""

Chicago CBD & Tribune Property Tour

"""

@main.route("/tour")
@login_required
def tour():
    return render_template("tour.html")

"""

Import Data and Filter

"""

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file_csv = os.path.join(THIS_FOLDER,'data','chicago_cbd_supply_to_date.csv')
my_file_geo = os.path.join(THIS_FOLDER,'data','chicago_cbd_supply_to_date.geojson')
my_file_cta = os.path.join(THIS_FOLDER,'data','cta_clean.csv')

def weights():

    default_weights = {
        "Union": .25,
        "Ogilvie": .2,
        "Lasalle": .04,
        "Millennium": .03,
        "Van Buren": .01,
        "Red": .10,
        "Blue": .15,
        "Brown": .10,
        "Purple": .05,
        "Green": .01,
        "Orange": .04,
        "Pink": .02
        }
    return default_weights

def route_colors():
    route_colors = {
      "Yellow":"#ffff00",
      "Blue":"#00a5e0",
      "Red":"#c60c30",
      "Purple":"#941f8a",
      "Orange":"#f79813",
      "Green":"#009b3a",
      "Pink":"#f589b0",
      "Brown":"#62361b",
      "Ogilvie": "#1152A7",
      "Union": "#1152A7",
      "Millennium": "#1152A7",
      "Van Buren": "#1152A7",
      "Lasalle": "#1152A7"
     }
    return route_colors

#make new CONFIGURATION TO ENSURE PASSING BACK AND FORTH IS WORKKING BEFOFE MODIFY CODE BELOW

@main.route("/mode", methods=["GET","POST"])
def mode():
    #THIS MAKES NO SENSE, IT SHOULD BE A RETRIEVAL JSON CONVERTED TO DICT PY
    #CHANGE TO POST
    #if request.is_json: #ensures mimetype application/json
    #req = request.get_json() #must be json otherwise returns None
    #response = {"message": "JSON received!", "name": req.get("name")}
    #res = make_response(jsonify(response), 200)
    #return res
    #
    grab = weights()
    union = request.args.get('union', grab.get('Union'), type=float)
    ogilvie = request.args.get('ogilvie', grab.get('Ogilvie'), type=float)
    lasalle = request.args.get('lasalle', grab.get('Lasalle'), type=float)
    mill = request.args.get('mill', grab.get('Millennium'), type=float)
    van = request.args.get('van', grab.get('Van Buren'), type=float)
    #get cta stations
    red = request.args.get('red', grab.get('Red'), type=float)
    blue = request.args.get('blue', grab.get('Blue'), type=float)
    brown = request.args.get('brown', grab.get('Brown'), type=float)
    purple = request.args.get('purple', grab.get('Purple'), type=float)
    green = request.args.get('green', grab.get('Green'), type=float)
    orange = request.args.get('orange', grab.get('Orange'), type=float)
    pink = request.args.get('pink', grab.get('Pink'), type=float)
    #dict of calculated weights retrieved from input
    # for k,v in dict: v
    weight_results = {
        #commuter lines
        "Union": union,
        "Ogilvie": ogilvie,
        "Lasalle": lasalle,
        "Millennium": mill,
        "Van Buren": van,
        #city lines
        "Red": red,
        "Blue": blue,
        "Brown": brown,
        "Purple": purple,
        "Green": green,
        "Orange": orange,
        "Pink": pink
    }
    #mode share calculations for display
    share_comm = sum([union,ogilvie,lasalle,mill,van])
    share_cta = sum([red,blue,brown,purple,green,orange,pink])
    #mode reconciliation to 100%
    reconcile = sum(weight_results.values())

    return jsonify(result=json.dumps(weight_results))

#flash('New entry was successfully posted')

#RUN THIS AS AN "after_request or after_request_funcs w/ a dict????"
def transit_time():
    cta = pd.read_csv(my_file_cta)
    #subject location, to be replaced w/ js marker UI
    pin = (41.885294,-87.621508)

    #convert column from string to tuple
    cta['coords'] = list(zip(cta.lon, cta.lat))
    cta['dist_subj'] = cta['coords'].apply(lambda x: round(distance.distance(pin,x).miles,2))
    cta.drop_duplicates('station_id',inplace=True)
    #city train station dictionary for creating DF
    lines = cta.columns[7:16]
    print("LINEES")
    print(lines)
    city=[]
    for i in lines:
        if i == 'ppl_exp' or i == 'yellow':
            continue
        i = i.capitalize() #cap for search
        df = cta[cta['STATION_DESCRIPTIVE_NAME'].str.contains(str(i))].sort_values('dist_subj')[0:1] #nearest station row of frame
        city.append(
          {
              'type': 'CTA',
              'line': i,
              'station': df.STATION_NAME.values[0],
              'dist': df.dist_subj.values[0],
              'coords': df.coords.values[0],
              #'color': df.color.values[0],
          })
    #dict for commuter station calcs
    sub_stations = {
        'ogilvie': (41.883728,-87.640512),
        'union': (41.877800,-87.638907),
        'millennium': (41.884322,-87.623474),
        #'clybourn': (41.917012,-87.668138), take out clybourn for now, may want to add in future
        'lasalle': (41.875812,-87.632226),
        'van buren': (41.876923,-87.622940)
    }
    #suburban train station dictionary for df
    suburbs=[]
    for k,v in sub_stations.items():
        k = k.title() #format
        suburbs.append(
          {
              'type': 'Commuter',
              'line': k,
              'station': k,
              'dist': round(distance.distance(pin,v).miles,2),
              'coords': v,
              'color': "#1152A7",
          })
    #combine dictionaries and create dataframe
    city_subs_total = city + suburbs
    #print(city_subs_total)
    total_commute = pd.DataFrame(city_subs_total)
    #initialize mode results from input forms
    d = mode()
    #c = make_response(json.dumps(d), 200)
    print('checking response for success')
    c = json.loads(d.data)
    default_weights = json.loads(c['result'])
    print(default_weights)
    total_commute['%ridership'] = total_commute.line.map(default_weights)
    total_commute['wtd_dist'] = round(total_commute['dist'] * total_commute['%ridership'],4)

    #initialize route colors dictionary for mapping for API call
    colors = route_colors()
    total_commute['color'] = total_commute.line.map(colors)
    return total_commute

def get_pin_marker():
    #placeholder for mapbox pin API retrieval and putting to route API
    return 'hold'

def mapbox_route_api():
    commuter = transit_time() #dataframe to iterate thru for routing API call
    print("check dataframe is in API")
    print(commuter)
    token='pk.eyJ1IjoibXBvdHRlciIsImEiOiJjajAxZGltM3UwNjF2MzJsczVnN3R2eTNnIn0._Sj0HRLt8VTQGTojMWYFfQ'
    mode='walking' #walking, cycling, driving
    features = []
    #get pin coordinates
    #pin = get_pin_marker()
    building = list((41.885294,-87.621508)) #placeholder for live pin drop
    orig_lng=building[1]
    orig_lat=building[0]
    count = 0
    for i, row in commuter.iterrows():
        #prepare coordinates for API call
        d = list(row['coords'])
        #destination = (41.876923,-87.622940)
        dest_lng = d[1]
        dest_lat = d[0]

        #add properties from DataFrame
        comm_type = row['type']
        train_line = row['line']
        station_name = row['station']
        color = row['color']
        #perform API call and format results
        url = 'https://api.mapbox.com/directions/v5/mapbox/'
        baseAPI = url+f'{mode}/{orig_lng}%2C{orig_lat}%3B{dest_lng}%2C{dest_lat}?alternatives=false&geometries=geojson&steps=false&access_token={token}'
        response = requests.get(baseAPI)
        formattedResponse = json.loads(response.text)
        #add properties from API results
        coords = formattedResponse['routes'][0]['geometry']['coordinates']
        dist = round(formattedResponse['routes'][0]['distance'] * 3.28084, 2)
        time = round(formattedResponse['routes'][0]['duration'] / 60, 2)
        features.append({"type":"Feature",
              "properties": {
                  "line": train_line,
                  "color": color,
                  "station": station_name,
                  "lng": dest_lng,
                  "lat": dest_lat,
                  "distance": dist,
                  "minutes": time,
                  #in the future add employee share by station for Bubble Sizing paint on map
              },
              "geometry": {
                  "type": "LineString",
                  "coordinates": coords
              }})
    stringy = json.dumps(features)
    prefix='{"type": "FeatureCollection", "features":'
    suffix = '}'
    combine = prefix+stringy+suffix
    print(combine)
    return combine

def circle_viz():
    #groupby station for circle visualization; will need to get to geojson format [data | json]
    stations = transit_time()
    station_weights = stations.groupby(['station', 'coords']).agg({'%ridership':'sum'}).reset_index()
    return station_weights

@main.route("/commuter", methods=["GET"])
def commuter():
    transit_results = transit_time()
    mapbox = mapbox_route_api()
    #station_ridership = circle_viz() #need to add to return
    return render_template('commuter.html', computer=transit_results, routes=mapbox)

@main.route("/slide", methods=["GET"])
def slide():
    slider = request.get_json()
    print(slider)
    f = list(range(2000,2025,1))
    filt = [i for i in f if i < 2010]
    print(f)
    return render_template('slide.html', years = filt)

@main.route("/suggestions", methods=["POST"])
def suggestions():
    text = request.get_json()
    return jsonify(text)


"""
Downtown Development Data & Filter

NEED TO REFACTOR FILTER GEOJSON TO SEPARATE FUNCTION ENDING IN A RETURN DF
"""

def geojson_map(slider_year):
    dft = pd.read_json(my_file_geo)
    properties = []
    for i in dft.features:
        if i['properties']['year'] <= slider_year:
            properties.append(i)
    #json string
    stringy = json.dumps(properties)
    #create FeatureCollection
    prefix ='{"type": "FeatureCollection", "features":'
    suffix = '}'
    combine = prefix+stringy+suffix
    return str(combine)

def submarket_table(slider_year):
    df_trial = pd.read_csv(my_file_csv)
    df_filt = df_trial[
             (df_trial['year']<=slider_year)
            #&(df_trial['use']=='Resi')
             ]
    subs = df_filt.groupby('submarket').agg({'gfa':'sum'}).sort_values('gfa',ascending=False)[0:5]
    subs['pct'] = subs.gfa/ subs.gfa.sum()
    subs.reset_index(inplace=True)

    resp_dict = []
    for index, row in subs.iterrows():
        a ={
            "submarket": row['submarket'],
            "gfa": row["gfa"],
            "pct": round(row["pct"],4)
            }
        resp_dict.append(a)
    return resp_dict

@main.route("/supply", methods=["GET","POST"])
def supply():
    if request.method == "POST" and request.is_json:
        req = request.get_json()
        slider_year = req.get("yr")
        data = geojson_map(slider_year)
        resp_dict = submarket_table(slider_year)
        bar = create_bar_plot(slider_year)
        print("POST METHOD")
        print(data)
        print(resp_dict)
        #res = make_response(jsonify(submkt_dict),200)
        return jsonify({ 'data': data, 'yr': slider_year, 'table': resp_dict, 'plot': bar })
    else:
        #populate default values and load template
        t = 2001
        data = geojson_map(t)
        resp_dict = submarket_table(t)
        bar = create_bar_plot(t)
        print("GET METHOD")
        print(data)
        print(resp_dict)
        #resp_dict = jsonify(resp_dict)
        return render_template("supply.html",data=data, submkt_dict=resp_dict, plot=bar)

def create_bar_plot(slider_year):
    #df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe
    cols = ['project','use','submarket','year','gfa','lon','lat']
    df = pd.read_csv(my_file_csv,usecols=cols)
    year_min = df.year.min()
    year_max = df.year.max() + 1
    horizon = list(range(year_min,year_max))
    df_mod = df[
        (df['year']>=slider_year)
        #&(df['use']=='Office')
        ]
    group = df_mod.groupby('year').agg({'gfa':'sum'}) #.sort_values('gfa',ascending=True)[0:10]
    fig = [
        go.Bar(
            x=horizon, # assign x as the dataframe column 'x'
            y=group['gfa'],
            opacity = .5,
        )
    ]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

@main.route("/plots")
def plots():
    bar = create_bar_plot(2000)
    return render_template("plots.html",plot=bar)

"""
Other Routes
"""

@main.route("/existing")
def existing():
    return render_template("existing.html")

#df = df[df['a'] == int(request.json.get('requested_code'))]

@main.route("/radio", methods=("POST", "GET"))
def html_radio():
    option = requests.form['options']
    return render_template('radio.html')

@main.route("/cagr")
def cagr():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    total = round((b / a) ** (1 / c ) - 1,4)
    return jsonify(result=total)

@main.route('/calc')
def calc():
    return render_template("calc.html")


if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
