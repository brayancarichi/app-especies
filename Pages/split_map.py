import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""
markdown2 = "Esta aplicación muestra los puntos de presencia de las especies animales más importantes del estado de Nuevo León. Adicionalmente, muestras estadísticas de cada municipio donde hay puntos de presencia de las especies.  "

options = list(['Zorra Gris','Tortuga del Desierto','Águila Real'])
index = options.index('Zorra Gris')

grafica_zorro = pd.DataFrame({"Puntos de presencia":['México: 5817','Nuevo León: 118'], "value": [5817,118]})
grafica_tortuga = pd.DataFrame({"Puntos de presencia":['México: 1063','Nuevo León: 343'], "value": [1063,343]})
grafica_aguila = pd.DataFrame({"Puntos de presencia":['México: 2333','Nuevo León: 241'], "value": [2333,241]})


c = alt.Chart(grafica_zorro).mark_arc().encode(theta="value",color="Puntos de presencia")
c2 = alt.Chart(grafica_tortuga).mark_arc().encode(theta="value",color="Puntos de presencia")
c3 = alt.Chart(grafica_aguila).mark_arc().encode(theta="value",color="Puntos de presencia")
#st.sidebar.title("About")
st.sidebar.image("Imagenes/desarrolloreg.png")
st.sidebar.info(markdown2)
#st.sidebar.altair_chart(c,use_container_width=True)




st.title("Fauna mas importante de Nuevo León")

#st.se

i = 1


with st.expander("See source code"):
        selec = st.sidebar.selectbox("Animales mas importantes del matorral",options,index)
        print(selec + "lo seleccionado fue")
        cities = 'Matorral/Zorra.csv'
        cities2 = 'Matorral/Tortuga.csv'
        cities3 = 'Matorral/Aguila.csv'
        opcion = selec 
        if opcion == 'Zorra Gris':
            seleccionado = cities
            logo = 'Imagenes/Zorra.jpg'
            grafico = c
            print(seleccionado)
            
        elif opcion == 'Tortuga del Desierto':
            seleccionado = cities2
            logo = 'Imagenes/Tortuga.jpg'
            grafico = c2
            print(seleccionado)
            
        elif opcion == 'Águila Real':
            seleccionado = cities3
            logo = 'Imagenes/Aguila.jpg'
            grafico = c3
        st.sidebar.image(logo)
        st.sidebar.altair_chart(grafico,use_container_width=True)
        
        m = leafmap.Map(center=[25.67 ,-100.31847], zoom=7,minimap_control = True)
        
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'
        regions2 = 'Nl.geojson'
        raster = 'Limon.tif'

        m.add_geojson(regions2, layer_name='US Regions')
        
        m.add_points_from_xy(
                seleccionado,
                x="x",
                y="y",
                color_column='Estatus',
                icon_names=['Presencia'],
                spin=True,
                add_legend=True,
                
                
            )
        
   
m.to_streamlit(height=800)


#streamlit run .\Pages\split_map.py --server.port 8888