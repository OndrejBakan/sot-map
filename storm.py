import json
import folium

m = folium.Map(
    min_zoom=-10000,
    max_zoom=10,
    max_bounds=True,
    location=[0, 0],
    tiles=None, crs='Simple')

with open('storm.json') as file:
    storm_params = json.load(file)
    locations = []

    for idx, point in enumerate(storm_params[0].get('Properties').get('PositionCurve').get('Points')):
        location = [point.get('OutVal').get('Y') * -1, point.get('OutVal').get('X')]
        locations.append(location)
        
        folium.Marker(
            location=location,
            popup=storm_params[0].get('Properties').get('StormType')[idx % 240],
            icon=folium.DivIcon(html=f"<div>{storm_params[0].get('Properties').get('StormType')[idx % 240]}</div>")
        ).add_to(m)

# folium.PolyLine(locations).add_to(m)

m.save('storm.html')