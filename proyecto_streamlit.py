# ------------LIBRERIAS----------------

import streamlit as st
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from neuralprophet import NeuralProphet


# ----------CONFIGURACIÓN DE LA PÁGINA----------

st.set_page_config(page_title ="Población mundial", layout = "centered")


# ----------DATAFRAMEs--------------

ciudades_españa_recientes = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/ciudades_españa_recientes.csv")
ciudades_españa = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/ciudades_españa.csv")
comunidades_autonomas = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/comunidades_autonomas.csv")
comunidades_serie_anual = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/comunidades_serie_anual.csv")
dataset_mundial = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/dataset_mundial.csv")
dataset_paises = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/dataset_paises.csv")
españa_poblacion = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/españa_poblacion.csv")
paises_actual = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/paises_actual.csv")
dataframe_ciudades = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/dataframe_ciudades.csv")
dataframe_continentes = pd.read_csv("/Users/angelpastorsanchez/Documents/VSCode/SAMPLEREPO/w_datasets/poblacion/trabajo/dataframe_continentes.csv")


# --------------APP----------------

# Utilizo este comando para cambiar el color de diferentes lugares de la página y el icono a pie de página.
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://img.freepik.com/premium-vector/shaded-world-map-vector-illustration-white-gray-texture_547648-986.jpg?w=2000") 
    }
    .css-6qob1r {
        background: url("https://images.squarespace-cdn.com/content/v1/5c26aef0da02bc78eded93a7/1591960091450-EN42FGVSS09Z3YNAY6I4/large-group-of-people.jpg")
    }
    .st-ck{
        background-color: transparent
    }
    .css-18ni7ap {
        background-color: transparent
    }
    .st-ax {
        background-color: 
    }
    .css-629wbf {
        background-color: transparent
    }
    .css-1x8cf1d {
        background-color: transparent
    }

    
    footer {visibility: hidden;}
    footer:hover,  footer:active {
        color: #ffffff;
        background-color: transparent; 
    }
    footer:after {
        content:'Ángel Pastor Sánchez'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


# SIDEBAR

# Creo una única pestaña en la que introduciré el índice.
tabs = st.sidebar.tabs(["-"])

tab_plot = tabs[0] 
with tab_plot:
    # Creo el directorio que servirá para navegar por el cuerpo central de la página.
    indice = option_menu(menu_title=None,
            options=["Introducción", "Mundo", "España", "Conclusiones"],
            default_index=0,
            orientation="vertical")


# CUERPO CENTRAL

# Si se señala la primera pestaña en el índice, se accede a la ventana Introducción.
if indice == "Introducción":
    st.title("Evolución de la población a nivel mundial, y español.")

    # Creo dos pestañas para navegar por la sección.
    tabs0 = st.tabs(["Información", "Preprocesamiento"])
    
    tab_plot = tabs0[0]
    with tab_plot:
        st.write("""-A la hora de contar la población mundial, existen varios "contadores" de población en tiempo real, aunque cada cual da resultados
        diferentes. Como curiosidad, aqui dejo el enlace a uno de ello.""")
        st.markdown("[worlddometers](http://www.worldometers.info/es/)")
        st.write("""-Se considera a la población mundial como el número total de personas que viven en todo el mundo en
        un momento dado. Esta cifra está determinada por los nacimientos, las defunciones y por la esperanza de vida.""")
        st.write("""-Se estima que desde la aparición de la especie en el planeta han existido 117000 millones de seres humanos, de los 
        cuales el 7% estaría vivo actualmente.""")
        st.write("""-La población mundial ha crecido de forma lenta y sostenidad a lo largo de la historia, pero en
        los últimos doscientos años este crecimiento se ha incrementado de forma notoria. Para este trabajo solo tendré en 
        cuenta los últimos sesenta años.""")
        st.write("""-Otros factores que influyen directamente en la población son la alimentación, higiene, sanidad, 
        difusión de medicamentos y el desarrollo de la tecnología han sido determinantes. Han contribuido a este desarrollo 
        de los últimos años la reducción de la mortalidad y un aumento generalizado de la esperanza de vida. Pese a que la natalidad
        tambien se ha reducido en numerosos países, la llamada eficiencia reproductiva (baja natalidad pero alta supervivencia del 
        individuo) ha contribuido.""")
        st.write("""-Existen varias teorías sobre la evolución demográfica, tanto serias
        como no tan serias, pero no se entrará en ello en este trabajo.""")
    
    tab_plot = tabs0[1]
    with tab_plot:
        
        st.write("""Para realizar este proyecto he obtenido información de diversar fuentes. 
        Las principales han sido:""")
        st.markdown("[Datahub](https://datahub.io/collections)")
        st.markdown("[Wikipedia](https://es.wikipedia.org/wiki/Población_mundial)")
        st.markdown("[INE](https://www.ine.es)")
        st.write("""De estas fuentes he obtenido los ocho dataset que he utilizado y con los mismos he 
        obtenido otros, de los que utilizaré diez para este proyecto. Estos dataset apenas contaban con datos 
        nulos en algún caso, por lo que la mayor parte del preprocesamiento ha consistido en cambiar el tipo de 
        dato de las variables, en crear otros archivos csv haciendo uniones o divisiones, y en hacer web scrapping.""")
        st.write("""Empecé trabajando un dataset con información sobre población de paises. De este separé información por regiones,
        la cual deseché por obtenerla más funcional de otras fuentes, información a nivel global e información por paises.
        En este punto quise unir al dataset inicial las coordenadas de los paises, para lo que usé otro dataset con las 
        mismas. Sin embargo, ambos dataset tenian el nombre de los paises en diferente idioma, por lo que utilicé un tercer
        dataset con las traducciones de los nombres para hacer la unión. Esta unión la hice utilizando merge y join en según 
        que caso. Una vez hecho esto obtuve los siguientes dataset:""")
        st.subheader("Dataset_paises")
        st.dataframe(dataset_paises)
        st.write("----")
        st.subheader("Paises_actual")
        st.dataframe(paises_actual)
        st.write("----")
        st.subheader("Dataset_mundial")
        st.dataframe(dataset_mundial)
        st.write("----")
        st.write("""Posteriormente, en el mismo archivo, realicé una técnica de web scrapping para obtener una tabla con 
        información sobre continentes. Una vez realizado todos los pasos, cambiar tipos y nombres de columnas, obtuve el siguiente 
        dataset:""")
        st.subheader("Dataframe_continentes")
        st.dataframe(dataframe_continentes)
        st.write("----")
        st.write("""En un nuevo notebook empecé a trabajar con un dataset sobre ciudades a nivel mundial y con datos de diferentes
        años. A este dataset eliminé las últimas columnas por corresponder al índice y no considerarlo impotante. Además, separé las
        ciudades españolas de las foraneas y deseché estas últimas por no contener información completa en cuanto a ciudades.
        En su lugar, volví a utilizar técnicas de web scrapping para obtener esta información de wikipedia. Una vez obtenida esta
        información apenas tuve que cambiar nombres y tipos. De este notebook obtuve los siguientes dataframes:""")
        st.subheader("Ciudades_españa")
        st.dataframe(ciudades_españa)
        st.write("----")
        st.subheader("Ciudades_españa_recientes")
        st.dataframe(ciudades_españa_recientes)
        st.write("----")
        st.subheader("Dataframe_ciudades")
        st.dataframe(dataframe_ciudades)
        st.write("----")
        st.write("""Por último, en un nuevo notebook he trabajado dos dataset sobre comunidades autonomás. Igual que en los anteriores, 
        estos archivos no tenían valores nulos, por lo que solo tuve que cambiar algun nombre de columna, tipos o elimanar algún caracter 
        que dificultase el proceso. De estos archivos obtuve los siguientes dataframes:""")
        st.subheader("España_población")
        st.dataframe(españa_poblacion)
        st.write("----")
        st.subheader("Comunidades_serie_anual")
        st.dataframe(comunidades_serie_anual)
        st.write("----")
        st.subheader("Comunidades_autónomas")
        st.dataframe(comunidades_autonomas)
        st.write("----")


# Si se señala la segunda pestaña en el índice, se accede a la ventana Mundo.
if indice == "Mundo":
    st.title("¿Cómo ha evolucionado la población a nivel mundial?")
    
    # Creo cuatro pestañas para navegar por la sección.
    tabs1 = st.tabs(["Gobal", "Continentes", "Países", "Ciudades"])
    
    tab_plot = tabs1[0]
    with tab_plot:

        ##### GRÁFICO0 #####
        # Creo el gráfico.
        grafico0 = px.line(dataset_mundial, x = "Año", y = "Valor", title = "Evolución de la población mundial (1960-2018)")
        # Hago transparente el fondo del gráfico.
        grafico0.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico0.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico0.update_xaxes(title_font=dict(color = "black"))
        grafico0.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico0.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico0.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Cambio el eje y.
        grafico0.update_layout(yaxis = dict(range = [0, max(dataset_mundial['Valor'])]))
        # Dibujo el gráfico.
        st.plotly_chart(grafico0)
        st.write("""En este gráfico se aprecia el incremento de la población en los años 1960-2018. Se puede observar
        que el crecimiento es sostenido. En la actualidad la población mundial es de alrededor de 8 mil millones.""")

        ##### GRÁFICO1 #####
        # Para hacer el gráfico con la tendencia creo una columna ad hoc.
        dataset_mundial["Tendencia"] = 0
        for i in range(len(dataset_mundial["Valor"])-1):
            dataset_mundial["Tendencia"][i+1] = dataset_mundial["Valor"][i+1] - dataset_mundial["Valor"][i]
        # Creo el gráfico.
        grafico1 = px.line(dataset_mundial, x = "Año", y = "Tendencia", title = "Tendencia de crecimiento (1960-2018)")
        # Hago transparente el fondo del gráfico.
        grafico1.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico1.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico1.update_xaxes(title_font=dict(color = "black"))
        grafico1.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico1.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico1.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico1)
        st.write("""En esta gráfica se aprecia cómo, en mayor o menor medida, siempre hay crecimiento.""")

    tab_plot = tabs1[1]
    with tab_plot:

        ##### GRÁFICO3 #####
        # Creo el gráfico.
        grafico3 = px.treemap(dataframe_continentes, path = [px.Constant("Población"), "Continente"], values = "Población", title = "Población por continentes (2023)")
        # Hago transparente el fondo del gráfico.
        grafico3.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico3.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico3)
        st.write("""En este gráfico se puede apreciar que Asia es el continente más poblado, con más de la mitad
        de la población mundial. Aunque no se ve bien por la proporción, la Antartida tiene una población no
        permanente de alrededor de 4500 personas, generalmente científicos.""")
        
    tab_plot = tabs1[2]
    with tab_plot:

        ##### GRÁFICO_MAPA #####
        # Creo variables longitud y latitud con las coordenadas del dataframe para poder usarlas en el gráfico.
        lats = (paises_actual['latitud']).tolist()
        lons = (paises_actual['longitud']).tolist()
        locations = list(zip(lats, lons))
        # Creo el gráfico.
        grafico_mapa = px.scatter_mapbox(paises_actual, lat=lats, lon=lons, size="Población",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=50, zoom=1, height= 600,
                  width = 750, mapbox_style="open-street-map", text = "País", title = "Población por paises (2018)")
        # Hago transparente el fondo del gráfico.
        grafico_mapa.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico_mapa.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico_mapa)
        st.write("""Vista sobre un mapa de la población por países. Se aprecia con claridad que China e India son los más poblados.""")

        ##### GRÁFICO5 #####
        # Creo el gráfico.
        grafico5 = px.bar(paises_actual.sort_values(by = "Población", ascending = False), x = "País", y = "Población", title = "Población por paises (2018)")
        # Hago transparente el fondo del gráfico.
        grafico5.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico5.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico5.update_xaxes(title_font=dict(color = "black"))
        grafico5.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico5.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico5.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico5)
        st.write("""171 países ordenados por la población que tienen.""")

        ##### GRÁFICO6 #####
        # Hago una selección ad hoc de los países con más de cien millones de habitantes.
        paises_actual_max = paises_actual[paises_actual["Población"] > 100000000][["País", "Población"]]
        # Creo el gráfico.
        grafico6 = px.bar(paises_actual_max.sort_values(by = "Población", ascending = False), x = "País", y = "Población", title = "Países con más de cien millones de habitantes (2018)")
        # Hago transparente el fondo del gráfico.
        grafico6.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico6.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico6.update_xaxes(title_font=dict(color = "black"))
        grafico6.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico6.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico6.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico6)
        st.write("""Gráfico de barras en el que aparecen los países con más de cien millones de habitantes. Se puede comprobar la gran
        diferencia de China e India con respecto a los demás y la ausencia de países europeos.""")

        ##### GRÁFICO7 #####
        # Cambio el nombre de las columnas.
        dataset_paises.rename(columns = {"index":"País",
                        "Country Code": "Código",
                        "Year": "Año",
                        "Value": "Población"},
                        inplace = True)
        # Hago una selección ad hoc de los países con más de 150 millones de habitantes.
        dataset_paises_line = dataset_paises[dataset_paises["Población"] >150000000][["País", "Población", "Año"]]
        # Creo el gráfico.
        grafico7 = px.line(dataset_paises_line, x = "Año", y = "Población",  color = "País", title = "Crecimiento poblacional por paises (1960-2018)")
        # Hago transparente el fondo del gráfico.
        grafico7.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico7.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico7.update_xaxes(title_font=dict(color = "black"))
        grafico7.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico7.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico7.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico7)
        st.write("""Este gráfico representa la evolución de la población de aquellos paises que han llegado a tener 150 millones
        de habitantes. Se aprecia como el ritmo de crecimiento de China se ha reducido, mientras el de India ha aumentado, llegando a estar 
        casi al mismo nivel en 2018. En 2021 China tenía 1,412, mientras India tenía 1,408 habitantes.""")

    tab_plot = tabs1[3]
    with tab_plot:

        ##### GRÁFICO8 #####
        # Elimino una de las apariciones de Canton por contener información ya incluida en la otra aparición.
        foxtrot = dataframe_ciudades.drop(dataframe_ciudades[dataframe_ciudades["Posición"]==19].index)
        # Creo el gráfico.
        grafico8 = px.bar(foxtrot, x = "Ciudad", y = "Población", title = "Ciudades más pobladas (2021)")
        # Hago transparente el fondo del gráfico.
        grafico8.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico8.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico8.update_xaxes(title_font=dict(color = "black"))
        grafico8.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico8.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico8.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico8)
        st.write("""En este gráfico se representan las cien ciudades más pobladas del mundo.""")

        ##### GRÁFICO11 #####
        # Creo el gráfico.
        grafico11 = px.treemap(dataframe_ciudades, path = [px.Constant("Población"), "País", "Ciudad"], values = "Población", title = "Ciudades más pobladas por país (2021)", height=700, width=700)
        # Hago transparente el fondo del gráfico.
        grafico11.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico11.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico11)
        st.write("""Aquí se pueden ver las cien ciudades más pobladas por país y podemos ver cómo los países más poblados son 
        los que tienen más ciudades con esas características.""")

        ##### GRÁFICO9 #####
        # Hago un selección ad hoc de aquellas ciudades con más de quince millones de habitantes. 
        # Para ello tengo en cuenta la eliminación de una de las dos apariciones de Cantón realizada previamente.
        dataframe_ciudades_max = foxtrot[foxtrot["Población"] > 15000000][["Ciudad", "Población", "País"]]
        # Creo el gráfico.
        grafico9 = px.bar(dataframe_ciudades_max, x = "Ciudad", y = "Población", title = "Ciudades con más de 15 millones de habitantes (2021)")
        # Hago transparente el fondo del gráfico.
        grafico9.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico9.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico9.update_xaxes(title_font=dict(color = "black"))
        grafico9.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico9.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico9.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico9)
        st.write("""En este grafico podemos ver las ciudades con más de 15 millones de habitantes, con Tokio a la cabeza, seguida de
        Canton.""")

        ##### GRÁFICO10 #####
        # Creo el gráfico.
        grafico10 = px.sunburst(dataframe_ciudades_max, path = ["País", "Ciudad"], values = "Población", title = "Ciudades con más de 15 millones de habitantes por país (2021)", width = 700, height = 700)
        # Hago transparente el fondo del gráfico.
        grafico10.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico10.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico10)
        st.write("""En este gráfico sunburst se pueden ver las ciudades con más de quince millones de habitantes por país. 
        Se puede comprobar que solo cuatro paises tienen más de una ciudad con esas condiciones.""")

# Si se señala la tercera pestaña en el índice, se accede a la ventana España.
if indice == "España":
    st.title("¿Cómo ha evolucionado la población a nivel español?")

    # Creo tres pestañas para navegar por la sección.
    tabs3 = st.tabs(["Nacional", "Comunidades", "Ciudades", "Previsión"])

    tab_plot = tabs3[0]
    with tab_plot:

        ##### GRÁFICO12 #####
        # Ordeno el orden de los valores para poder trabajarlos de forma adecuada.
        españa_poblacion.sort_values(by = "Año", ascending = True, inplace = True)
        # Creo el gráfico.
        grafico12 = px.line(españa_poblacion, x = "Año", y = "Total", title = "Evolución de la población española (1998-2021)")
        # Hago transparente el fondo del gráfico.
        grafico12.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico12.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico12.update_xaxes(title_font=dict(color = "black"))
        grafico12.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico12.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico12.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico12)
        st.write("""En este gráfico podemos observar la evolución de la población española desde finales del siglo pasado hasta el año
        2021. En el periodo 1998-2012 vemos que se produce un incremento continuado de la población. Sin embargo, a partir de este
        último año, la población disminuye hasta llegar al año 2017, en que empieza de nuevo una tendencia positiva.
        En el año 2020 se produce un nuevo descenso de la población debido, seguramente, al coronavirus.""")

        ##### GRÁFICO13 #####
        # Para hacer el gráfico con la tendencia creo una columna ad hoc.
        españa_poblacion["Tendencia"] = 0
        for i in range(len(españa_poblacion["Total"])-1):
            españa_poblacion["Tendencia"][i] = españa_poblacion["Total"][i] - españa_poblacion["Total"][i+1]
        # Creo el gráfico.
        grafico13 = px.line(españa_poblacion, x = "Año", y = "Tendencia", title = "Tendencia de crecimiento (1998-2021)")
        # Hago transparente el fondo del gráfico.
        grafico13.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico13.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico13.update_xaxes(title_font=dict(color = "black"))
        grafico13.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico13.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico13.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico13)
        st.write("""Este gráfico complementa al anterior. Vemos que hay crecimiento hasta 2012 pero no siempre al mismo ritmo. A 
        partir de 2012 hasta 2017 y en 2020 vemos vemos que el crecimiento pasa a ser negativo, es decir, la población esta decreciendo.""")

    tab_plot = tabs3[1]
    with tab_plot:

        ##### GRÁFICO14 #####
        # Elimino una columna para que no me moleste.
        comunidades_autonomas.drop(["Unnamed: 0"], axis = 1, inplace = True)
        # Elimino fila de total.
        eco = comunidades_autonomas.drop(comunidades_autonomas.index[-1])
        # Creo el gráfico.
        grafico14 = px.imshow(eco.corr(method="spearman"), title = "Correlaciones")
        # Hago transparente el fondo del gráfico.
        grafico14.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico14.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico14.update_xaxes(title_font=dict(color = "black"))
        grafico14.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico14.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico14.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico14)
        st.write("""En este mapa de calor podemos ver las correlaciones que hay entre la superficie, la población y el PIB per capita por
        comunidad autonoma. En este caso hay una correlación positiva significativa de 0.6 entre superficie y cantidad de población. Tambien
        se podría reseñar que, aunque poco significativa, hay correlación negativa entre PIB y superficie, es decir, las comunidades
        autónomas con poco terreno son las que tienen un mayor PIB.""")

        ##### GRÁFICO141 #####
        # Creo el gráfico.
        grafico141 = px.scatter(eco, x = "Superficie (km²)", y = "Población", trendline = "ols", title = "Recta de regresión entre superficie y población", hover_name = "Nombre")
        # Hago transparente el fondo del gráfico.
        grafico141.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico141.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico141.update_xaxes(title_font=dict(color = "black"))
        grafico141.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico141.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico141.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico141)
        st.write("""En este caso he realizado una recta de regresión que relacione las variables población y superficie, que eran las más correlacionadas.
        Podemos observar que se produce una cierta tendencia lineal, solo entorpecida por el comportamiento de los valores atípicos.""")


        # Genero tres columnas para colocar tres gráficos en paralelo.
        col1, col2, col3 = st.columns(3)

        with col1:

            ##### GRÁFICO15 #####
            # Creo el gráfico.
            grafico15 = px.box(eco, y = ["Población"], orientation = "v", hover_name = "Nombre", title = "Espacios intercuartílicos.")
            grafico15.update_layout(autosize=False, width=250) 
            # Hago transparente el fondo del gráfico.
            grafico15.update_layout(paper_bgcolor="rgba(0,0,0,0)")
            grafico15.update_layout(plot_bgcolor="rgba(0,0,0,0)")
            # Cambio el color de los títulos de los ejes.
            grafico15.update_xaxes(title_font=dict(color = "black"))
            grafico15.update_yaxes(title_font=dict(color = "black"))
            # Cambio el color de las etiquetas de los ejes.
            grafico15.update_layout(xaxis={"tickfont": {"color": "black"}})
            grafico15.update_layout(yaxis={"tickfont": {"color": "black"}})
            # Dibujo el gráfico.
            st.plotly_chart(grafico15)

        with col2:

            ##### GRÁFICO16 #####
            # Creo el gráfico.
            grafico16 = px.box(eco, y = ["Superficie (km²)"], orientation = "v", hover_name = "Nombre")
            grafico16.update_layout(autosize=False, width=250)
            # Hago transparente el fondo del gráfico.
            grafico16.update_layout(paper_bgcolor="rgba(0,0,0,0)")
            grafico16.update_layout(plot_bgcolor="rgba(0,0,0,0)")
            # Cambio el color de los títulos de los ejes.
            grafico16.update_xaxes(title_font=dict(color = "black"))
            grafico16.update_yaxes(title_font=dict(color = "black"))
            # Cambio el color de las etiquetas de los ejes.
            grafico16.update_layout(xaxis={"tickfont": {"color": "black"}})
            grafico16.update_layout(yaxis={"tickfont": {"color": "black"}})
            # Dibujo el gráfico.
            st.plotly_chart(grafico16)

        with col3:

            ##### GRÁFICO17 #####
            # Creo el gráfico.
            grafico17 = px.box(eco, y = ["PIB per cápita en € (2021)"], orientation = "v", hover_name = "Nombre")
            grafico17.update_layout(autosize=False, width=250)
            # Hago transparente el fondo del gráfico.
            grafico17.update_layout(paper_bgcolor="rgba(0,0,0,0)")
            grafico17.update_layout(plot_bgcolor="rgba(0,0,0,0)")
            # Cambio el color de los títulos de los ejes.
            grafico17.update_xaxes(title_font=dict(color = "black"))
            grafico17.update_yaxes(title_font=dict(color = "black"))
            # Cambio el color de las etiquetas de los ejes.
            grafico17.update_layout(xaxis={"tickfont": {"color": "black"}})
            grafico17.update_layout(yaxis={"tickfont": {"color": "black"}})
            # Dibujo el gráfico.
            st.plotly_chart(grafico17)
        st.write("""En estos gráficos de barras y bigotes podemos ver los espacion intercuartílicos, es decir, dónde
        se concentra el cincuenta por ciento del total de los datos. Además, podemos apreciar los valores atípicos. En
        cuanto a población, aquellas comunidades cuya población supone un valor atípico son Andalucía, Cataluña y Madrid 
        y en cuanto a superficie el valor atípico lo supone Castilla y Leon.""")

        ##### GRÁFICO18 #####
        # Elimino una columna para que no me interfiera.
        # Creo el gráfico.
        grafico18 = px.treemap(eco, path=[px.Constant("Población"), 'Nombre'], values = "Población", title = "Comunidad autónoma por población (2022)")
        # Hago transparente el fondo del gráfico.
        grafico18.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico18.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico18)

        ##### GRÁFICO19 #####
        # Creo el gráfico.
        grafico19 = px.treemap(eco, path=[px.Constant("Superficie (km²)"), 'Nombre'], values = "Superficie (km²)", title = "Comunidades autónomas por superficie.")
        # Hago transparente el fondo del gráfico.
        grafico19.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico19.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico19)

        ##### GRÁFICO20 #####
        # Creo el gráfico.
        grafico20 = px.treemap(eco, path=[px.Constant("PIB per cápita en € (2021)"), 'Nombre'], values = "PIB per cápita en € (2021)", title = "Comunidades autónomas por PIB per capita (2021)")
        # Hago transparente el fondo del gráfico.
        grafico20.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico20.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Dibujo el gráfico.
        st.plotly_chart(grafico20)
        st.write("""En estos gráficos podemos ver la distribución de las comunidades por cantidad de población, superficie de terreno
        ocupada y PIB per capita. Como datos a reseñar podemos ver que Madrid y Cataluña están en cabeza en cuanto a población y PIB 
        pero sin embargo tienen una superficie de terreno pequeña. Pero más llamativo es el caso de Andalucia, que tiene la mayor población y es la segunda
        en cuanto a superficie, pero sin embargo cuenta con el PIB menor.""")

        ##### GRÁFICO21 #####
        # Creo el gráfico.
        grafico21 = px.line(comunidades_serie_anual, x = "Año", y = "Total", color = "CCAA", title = "Evolución de la población por CCAA.")
        # Hago transparente el fondo del gráfico.
        grafico21.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico21.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico21.update_xaxes(title_font=dict(color = "black"))
        grafico21.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico21.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico21.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico21)
        st.write("""Aquí vemos como las comunidades autónomas más pobladas siguen la misma tendencia del global de España, es decir, se
        produce una reducción de la población a partir de 2012 hasta 2017 y vuelve a caer en 2020. En las comunidades con menor población
        este comportamiento es más limitado en la mayoría de los casos.""")

    tab_plot = tabs3[2]
    with tab_plot:
        
        ##### GRÁFICO22 #####
        # Creo el gráfico.
        grafico22 = px.bar(ciudades_españa_recientes.sort_values(by = "Valor", ascending = False), x = "Ciudad", y = "Valor", title = "Población por ciudades (2012)")
        # Hago transparente el fondo del gráfico.
        grafico22.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico22.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico22.update_xaxes(title_font=dict(color = "black"))
        grafico22.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico22.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico22.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico22)
        st.write("""Podemos ver como la ciudad más poblada de España es Madrid, con más de tres millones de habitantes, el doble aproximadamente 
        que Barcelona. Estas dos ciudades son las únicas que superan el millon de habitantes.""")

        ##### GRÁFICO24 #####
        # Quiero tener en cuenta solo aquellas ciudades con más de quinientos mil habitantes.
        ciudades_max_1 = ciudades_españa[ciudades_españa["Valor"] > 500000][["Ciudad", "Valor", "Año"]]
        # Creo el gráfico.
        grafico24 = px.line(ciudades_max_1, x = "Año", y = "Valor", color = "Ciudad", title = "Evolución de la población en las ciudades más pobladas (2012)")
        # Hago transparente el fondo del gráfico.
        grafico24.update_layout(paper_bgcolor="rgba(0,0,0,0)")
        grafico24.update_layout(plot_bgcolor="rgba(0,0,0,0)")
        # Cambio el color de los títulos de los ejes.
        grafico24.update_xaxes(title_font=dict(color = "black"))
        grafico24.update_yaxes(title_font=dict(color = "black"))
        # Cambio el color de las etiquetas de los ejes.
        grafico24.update_layout(xaxis={"tickfont": {"color": "black"}})
        grafico24.update_layout(yaxis={"tickfont": {"color": "black"}})
        # Dibujo el gráfico.
        st.plotly_chart(grafico24)
        st.write("""En este gráfico se ve la evolución de la población española de las ciudades más pobladas desde 1998 hasta 2012. Se pude ver que apenas 
        hay variación a excepción de en Madrid y Barcelona. En la actualidad los datos se mantienen a un nivel similar.""")
    
    tab_plot = tabs3[3]
    with tab_plot:
        st.subheader("Neural Prophet población")
        # Realizo una previsión utilizando Neural Prophet.
        # Para ello cambio el nombre de algunas variables que he guardado previamente en un nuevo dataframe.
        españa_poblacion_neural = españa_poblacion[["Año", "Total"]]
        españa_poblacion_neural.rename(columns = {"Año":"ds", "Total":"y"}, inplace = True)
        # Cambio el tipo de dato a fecha con el formato adecuado.
        españa_poblacion_neural["ds"] = pd.to_datetime(españa_poblacion_neural["ds"], format="%Y")
        # Instancio la clase.
        m = NeuralProphet()
        # Parto datos especificando unidad mínima de tiempo.
        df_train, df_val = m.split_df(españa_poblacion_neural, freq='Y', valid_p = 0.3)
        # Entreno modelo.
        metrics = m.fit(df_train, freq='Y', validation_df=df_val)
        # Realizo predicciones.
        future = m.make_future_dataframe(españa_poblacion_neural, periods=12, n_historic_predictions=len(españa_poblacion_neural))
        forecast = m.predict(future)
        # Muestro el dataframe.
        forecast = forecast[["ds", "y", "yhat1"]]
        st.dataframe(forecast)
        # Realizo gráficos.
        grafico25 = m.plot(forecast, figsize = (6, 6))
        st.plotly_chart(grafico25)

# Si se señala la cuarta pestaña en el índice, se accede a la ventana Conclusiones.
if indice == "Conclusiones":
    st.title("Conclusiones")
    st.write("""- Crecimiento constante de la población por la mejora de las condiciones de vida.""")
    st.write("""- Mayor población en Asia por la presencia de China e India, que mantienen una gran diferencia con todos los demás paises.""")
    st.write("""- Reducción del crecimiento chino con posible adelantamiento de India.""")
    st.write("""- Ausencia de ciudades europeas entre las más pobladas. Destaca Tokio.""")
    st.write("""- Tendencia irregular en el crecimiento español, que se ve muy afectado por factores influyentes.""")

