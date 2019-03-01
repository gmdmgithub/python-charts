import folium
from config import Config

def main():
        #create a map
        map = folium.Map(location=[Config.MAP_LOCATION_X,Config.MAP_LOCATION_Y], zoom_start=18)

        tooltip = 'Nice place, nice city'
        #custom marker
        customIcon = folium.features.CustomIcon('./tesla.png',icon_size=(50,50))

        #create markap
        folium.Marker([50.062379, 19.936971],
                popup='<strong>My lovely place</strong>',
                tooltip=tooltip,
                icon=customIcon).add_to(map)

        folium.Marker([50.061379, 19.937671],
                popup='<strong>Market sqare</strong>',
                tooltip=tooltip,
                icon=folium.Icon(icon='cloud',color="green")).add_to(map)

        folium.Marker([50.061749, 19.938971],
                popup='<strong>Churche</strong>',
                tooltip=tooltip).add_to(map)

        #circle marker
        folium.CircleMarker(location=[50.062349, 19.93697],
                        radius=50,
                        popup='Im here',
                        tooltip=tooltip).add_to(map)

        #save map to the file
        map.save('mymap.html')

if __name__ == "__main__":
        main()