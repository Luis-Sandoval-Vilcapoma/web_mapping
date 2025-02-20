#Folium facilita la visualización de datos que se han manipulado en Python en un mapa de folleto interactivo. Permite tanto la unión de datos a un mapa para visualizaciones de coropletas además de pasar ricas visualizaciones vector/raster/HTML como marcadores en el mapa.
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


#Map()
#Generar una base mapa de ancho(-80 a 80) y alto(-180 a 180) dados con cualquiera de los valores predeterminados mosaicos o una URL de mosaico personalizada.
map = folium.Map(location=[38.58,-99.09],zoom_start=7, tiles="OpenStreetMap", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")

fg = folium.FeatureGroup(name="My Map")

for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(str(el)+" msnm", parse_html=True) , icon=folium.Icon(color="green")))

#popup=folium.Popup(str(el), parse_html=True)
map.add_child(fg)

map.save("map1.html")





# tiles = "Mapbox Bright" no funciona
# tiles = "Stamen Terrain"
