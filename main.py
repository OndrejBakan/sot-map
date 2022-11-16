import json
import folium

m = folium.Map(
    min_zoom=-1000,
    max_zoom=10,
    max_bounds=True,
    location=[-4822.2, 8691.4],
    tiles=None, crs='Simple',
    min_lat=-10000, max_lat=10000,
    min_lon=-10000, max_lon=10000,)

with open('seadetails.json') as file:
    data = json.load(file)

    for sea_detail in data['SeaDetails']:
        image = f"img/{sea_detail['Texture']['ObjectName'].split()[1]}.png"
        image_size = [448 / 2, 236 / 2]

        bounds=[[(sea_detail['Location']['Y'] - (image_size[1])) * -1, sea_detail['Location']['X'] - (image_size[0])],
                [(sea_detail['Location']['Y'] + (image_size[1])) * -1, sea_detail['Location']['X'] + (image_size[0])]]
        
        print(bounds)

        folium.raster_layers.ImageOverlay(image, bounds=bounds, icon=folium.DivIcon(html=f"""<div style="font-family: courier new; color: blue">{data.iloc[i]['name']}</div>""")).add_to(m)

m.save('index.html')
