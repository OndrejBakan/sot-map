import folium
import json


m = folium.Map(
    min_zoom='-1000',
    max_zoom=10,
    location=[0, 0],
    tiles=None, crs='Simple')

with open('sot_world_layout_2_generatedisslands.json') as file:
    data = json.load(file)

    for island_entry in data[0].get('Properties').get('IslandEntries'):
        location = [(island_entry.get('IslandBoundsCentre').get('Y') - 200) * -1, island_entry.get('IslandBoundsCentre').get('X') - 200]
        bounds = [
            [(island_entry.get('IslandBoundsCentre').get('Y') - 20000) * - 1, island_entry.get('IslandBoundsCentre').get('X') - 20000],
            [(island_entry.get('IslandBoundsCentre').get('Y') + 20000) * - 1, island_entry.get('IslandBoundsCentre').get('X') + 20000]]
        
        print(bounds)
    
        folium.raster_layers.ImageOverlay(f"IslandMaps/{island_entry.get('IslandName')}_questgen_Default.png", bounds=bounds).add_to(m)

m.save('world.html')