import json
import pandas as pd
import dateutil.parser as dparser
import folium
from urllib2 import urlopen
from flask import Flask,render_template,flash


app = Flask(__name__)

@app.route('/')
def homepage():
    assault_count = 0
    arrest_count = 0
    burglary_count = 0
    robbery_count = 0
    theft_count = 0
    other_count = 0

    data = get_data()
    address = []
    crime_type=[]
    lat=[]
    lon=[]
    date=[]
    crime_time=[]
    count = 0
    # print type(data)
    #print type(data)
    #print data.values()

    for item in data.values():
    	for value in item:
    		address.append(value['address'])
    		crime_type.append(value['type'])
    		lat.append(value['lat'])
    		lon.append(value['lon'])
    		date.append(value['date'])

    #print len(address)
    #print len(crime_type)
    #print len(date)

    for item in date:
        val=item.split(' ')
        val2=val[1]+val[2]
        crime_time.append(str(dparser.parse(val2)).split(' ')[1])

    print len(crime_time)

    map = folium.Map(location=[37.3382,-121.8863],zoom_start=5)

    df = pd.DataFrame({'Address':address,'Type':crime_type,'Latitude':lat,'Longitude':lon,'Time':crime_time})
    #print df['Type']
    for i in range(0,len(crime_type)-1):
        if crime_type[i] == "Shooting":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#f20000",radius = 5).add_to(map)
        if crime_type[i] == "Arrest":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#132b5e",radius = 5).add_to(map)
        if crime_type[i] == "Assault":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#f18500",radius = 5).add_to(map)
        if crime_type[i] == "Burglary":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#f1d900",radius = 5).add_to(map)
        if crime_type[i] == "Robbery":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#00c5f1",radius = 5).add_to(map)
        if crime_type[i] == "Theft":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#6000f1",radius = 5).add_to(map)
        if crime_type[i] == "Valndalism":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#00f189",radius = 5).add_to(map)
        if crime_type[i] == "Other":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#8000f0",radius = 5).add_to(map)
        if crime_type[i] == "Arson":
            folium.RegularPolygonMarker([lat[i],lon[i]],popup=crime_type[i],fill_color="#33ef00",radius = 5).add_to(map)

 #   map.save('templates/map.html')
    return render_template("map.html")






def get_data():
    base_url = "https://api.spotcrime.com/crimes.json?"
#    latitude = float(raw_input("\n Enter Latitude :"))
#    longitude = float(raw_input("\n Enter Longitude :"))
#    radius = float(raw_input("\n Enter the radius :"))
#    final_url = base_url + "lat=" + str(latitude) + "&lon=-" + str(longitude) + "&radius=" + str(
#        radius) + "&key=privatekeyforspotcrimepublicusers-commercialuse-877.410.1607"
    final_url = base_url + "lat=" + str(37.3382) + "&lon=-" + str(121.8863) + "&radius=" + str(
        10) + "&key=privatekeyforspotcrimepublicusers-commercialuse-877.410.1607"
    print final_url
    web = urlopen(final_url)
    data = web.read()
    #   print type(data)
    json_data = json.loads(data)
    return json_data


if __name__ == "__main__":
    app.run(debug=True)