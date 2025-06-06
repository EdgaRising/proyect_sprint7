import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv("../vehicles_us.csv")
st.header('Mi primer proyecto web')
# st.write('Esta aplicación aún no es funcional. En construcción.')
hist_button = st.button('Construir histograma')  # crear un botón
if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_disp = st.checkbox('Construir un diagrama de dispersion')

if build_disp:  # si la casilla de verificación está seleccionada
    # escribir un mensaje
    st.write('Construir un diagrama de dispersion para la columna odómetro')
    # crea un diagrama de dispersion
    fig = px.scatter(car_data, x="odometer", y="price")
    # mostrar un grafico Ploty interactivo
    st.plotly_chart(fig, use_container_width=True)
