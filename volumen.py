import streamlit as st
import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df

def filter_by_volume(df, volume_range):
    return df[(df['volumen'] >= volume_range[0]) & (df['volumen'] <= volume_range[1])]

st.title('Explorador de Datos CSV')

# Sidebar para entrada de usuario
with st.sidebar:
    uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

    # Inicialización de variables
    volume_range = (0, 500)
    df = None

    if uploaded_file is not None:
        # Carga de datos
        df = load_data(uploaded_file)

        if 'volumen' in df.columns:
            # Selección de rango de volumen
            max_volume = int(df['volumen'].max())
            volume_range = st.slider('Selecciona el rango de volumen de búsqueda', 0, max_volume, (0, max_volume))

# Procesamiento y visualización de datos
if df is not None:
    # Filtrar datos
    filtered_df = filter_by_volume(df, volume_range)
    st.write(f"Mostrando entradas con volumen entre {volume_range[0]} y {volume_range[1]}")

    # Mostrar solo las columnas deseadas
    st.dataframe(filtered_df[['volumen','keywords', 'urls']])
else:
    st.write("Esperando la carga del archivo CSV...")

