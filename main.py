#!/usr/bin/python
#-*- coding: utf-8 -*-


import json
import twitter
from twitterApi import *
from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

app = Flask(__name__)
GoogleMaps(app)
def getTweetsSearch(busqueda):
	twitter_api =  oauth_login()

	#punto de localización de la información
	spain_trends = twitter_api.search.tweets(q=busqueda, count=1000,geocode='40.40,3.567,500km')

	# almacenarlo en un fichero
	save_json('spainmore', spain_trends)

	# Vamos a extraer las consultas solamente de los tweets
	datos = json.loads(open('spainmore.json').read())


	lista = []
	for r in datos["statuses"]:
            if r["geo"]:
		latitud=r["geo"]["coordinates"][0]
		longitud=r["geo"]["coordinates"][1]
		coordenadas=[latitud,longitud]
        lista.append(coordenadas)
        return lista

#creacion del mapa
@app.route("/buscar", methods=['POST'])
def buscar():
    termino = request.form['text'] 
    coord = getTweetsSearch(termino)

    mymap = Map(
        identifier="view-side",
        lat=40.3450396,
        lng=-3.6517684,
        markers=coord,
        style="height:800px;width:800px;margin:0;"
    ) 
    return render_template('mapa.html', mymap=mymap)

@app.route("/")
def index():
	return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
