#Folium facilita la visualización de datos que se han manipulado en Python en un mapa de folleto interactivo. Permite tanto la unión de datos a un mapa para visualizaciones de coropletas además de pasar ricas visualizaciones vector/raster/HTML como marcadores en el mapa.
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"
    
#Map()
#Generar una base mapa de ancho(-80 a 80) y alto(-180 a 180) dados con cualquiera de los valores predeterminados mosaicos o una URL de mosaico personalizada.
map = folium.Map(location=[38.58,-99.09],zoom_start=7, tiles="CartoDB Positron", attr="Map data © OpenStreetMap contributors, Tiles © CartoDB")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=5, popup=folium.Popup(str(el)+" msnm", parse_html=True), color="grey", fill = True, fill_color=color_producer(el), fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding='utf-8-sig').read(), 
                             style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005']< 20000000 else 'red'}))


#popup=folium.Popup(str(el), parse_html=True)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")





# tiles = "Mapbox Bright" no funciona
# tiles = "Stamen Terrain"
