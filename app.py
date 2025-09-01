# Importar librerias
import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la app
st.header("Análisis Exploratorio de Datos de Vehículos en EE.UU.")

# Crear casillas de verificación para los gráficos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Crear una casilla de verificación para filtrar por tracción 4x4
build_4x4_checkbox = st.checkbox('Incluir vehículos con tracción 4x4')

# Condicional para filtrar los datos si la casilla 4x4 está marcada
if build_4x4_checkbox:
    st.write('Se ha activado el filtro para vehículos con tracción 4x4')
    filtered_data = car_data[car_data['is_4wd'] == 1]
else:
    filtered_data = car_data

# Lógica condicional para mostrar el histograma
if build_histogram:
    st.write(
        'Creando un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(filtered_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Lógica condicional para mostrar el gráfico de dispersión
if build_scatter:
    st.write('Creando un gráfico de dispersión de precio por año del modelo')
    fig_scatter = px.scatter(filtered_data, x="model_year", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
