import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página
st.set_page_config(
    page_title="Análisis de Vehículos",
    page_icon="🚗",
    layout="wide"
)

# Cargar los datos
@st.cache_data  # Esta decoración mejora el rendimiento
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()
# Título principal
st.title('📊 Análisis de Datos de Vehículos')
st.header('Dashboard Interactivo de Vehículos')

# Crear contenedores para organizar la interfaz
col1, col2 = st.columns(2)

with col1:
    # Botón para el histograma
    hist_button = st.button('Construir histograma')

    if hist_button:
        st.write('### Histograma de Kilometraje')
        st.write('Distribución del kilometraje de los vehículos')

        fig_hist = px.histogram(
            car_data,
            x="odometer",
            title="Distribución del Kilometraje",
            labels={'odometer': 'Kilometraje'},
            nbins=30
        )
        st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    # Botón para el gráfico de dispersión
    scatter_button = st.button('Construir gráfico de dispersión')

    if scatter_button:
        st.write('### Relación Precio vs Kilometraje')
        st.write('Gráfico de dispersión que muestra la relación entre precio y kilometraje')

        fig_scatter = px.scatter(
            car_data,
            x="odometer",
            y="price",
            color="model_year",
            title="Precio vs Kilometraje",
            labels={
                'odometer': 'Kilometraje',
                'price': 'Precio',
                'model_year': 'Año del Modelo'
            }
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
# Versión con checkboxes en lugar de botones
st.sidebar.header('Opciones de Visualización')

# Checkboxes en la barra lateral
show_histogram = st.sidebar.checkbox('Mostrar Histograma')
show_scatter = st.sidebar.checkbox('Mostrar Gráfico de Dispersión')

# Contenedor principal
if show_histogram:
    st.write('### Histograma de Kilometraje')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write('### Gráfico de Dispersión')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)