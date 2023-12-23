import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
import requests
import seaborn as sns
import logging

# Conf iguración básica del logger
logging.basicConfig(filename='app_logs.log', level=logging.INFO)


def info_box(texto, color=None):
    st.markdown(f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        st.error("Error en la solicitud")
        logging.error(f"Error en la solicitud a {url}")
        return None
    else:
        df = pd.DataFrame(r.json())
        logging.info(f"Datos cargados desde {url}")
        return df

df = load_data("http://fastapi:8000/all_data")

if df is None or df.empty:
    st.error("Error al cargar los datos desde la API de FastAPI.")
else:

    # Resto del código para procesar y mostrar los datos en Streamlit
    num_unique_symbols = df['Symbol'].nunique()
    average_volume = df['Volume'].mean()
    max_price = df['Close'].max()
    min_price = df['Close'].min()
    volumen = df['Volume'].sum()

    st.header("Información general sobre las criptomonedas")

    col2, col3 = st.columns(2)
    col4, col5, col6 = st.columns(3)
    
    with col2:
        col2.subheader('# Nº Cryptos Analizadas')
        info_box(num_unique_symbols, col2)
    with col3:
        col3.subheader('# Vol Medio de Operaciones')
        info_box(average_volume, col3)

    with col4:
        col4.subheader('# Precio Máximo')
        info_box(max_price, col4)

    with col5:
        col5.subheader('# Precio Mínimo')
        info_box(min_price, col5)
    with col6:
        col6.subheader('# Volumen')
        info_box(volumen, col6)


# close_price_variation
response = requests.get('http://fastapi:8000/close_price_variation')
if response.status_code == 200:
    close_price_variation_data = response.json()
    
    st.header("Variación del precio de cierre por criptomoneda")
    if close_price_variation_data:
        df_close_price_variation = pd.DataFrame(close_price_variation_data)
        fig = px.scatter(df_close_price_variation, x='Date', y='Close', color='Symbol',
                        hover_data={'Date': '|%Y-%m-%d', 'Close': ':.2f', 'Symbol': True})
        st.plotly_chart(fig, use_container_width=True)
        logging.info("Visualización de la variación del precio de cierre generada exitosamente")
    else:
        st.write("No se pudieron obtener los datos para la visualización.")
        logging.warning("No se encontraron datos para la variación del precio de cierre")
else:
    st.write("No se pudieron obtener los datos para la visualización.")
    logging.error("Error en la solicitud de datos para la variación del precio de cierre")
    

# open_price_variation
response = requests.get('http://fastapi:8000/open_price_variation')
if response.status_code == 200:
    open_price_variation_data = response.json()
    
    st.header("Variación del precio de apertura por criptomoneda")
    if open_price_variation_data:
        df_open_price_variation = pd.DataFrame(open_price_variation_data)
        fig = px.scatter(df_open_price_variation, x='Date', y='Open', color='Symbol',
                        hover_data={'Date': '|%Y-%m-%d', 'Open': ':.2f', 'Symbol': True})
        st.plotly_chart(fig, use_container_width=True)
        logging.info("Visualización de la variación del precio de apertura generada exitosamente")
    else:
        st.write("No se pudieron obtener los datos para la visualización.")
        logging.warning("No se encontraron datos para la variación del precio de apertura")
else:
    st.write("No se pudieron obtener los datos para la visualización.")
    logging.error("Error en la solicitud de datos para la variación del precio de apertura")
    
# transaction_volume
response = requests.get('http://fastapi:8000/transaction_volume')
if response.status_code == 200:
    transaction_volume_data = response.json()
    st.header("Volumen de transacciones por criptomoneda")
    if transaction_volume_data:
        df_transaction_volume = pd.DataFrame(transaction_volume_data)
        fig_bar = px.bar(df_transaction_volume, x='Symbol', y='Volume', color='Symbol',
                        hover_data={'Volume': True})
        st.plotly_chart(fig_bar, use_container_width=True)
        logging.info("Visualización del volumen de transacciones por criptomoneda generada exitosamente")
    else:
        st.write("No se pudieron obtener los datos para la visualización.")
        logging.warning("No se encontraron datos para el volumen de transacciones por criptomoneda")
else:
    st.write("No se pudieron obtener los datos para la visualización.")
    logging.error("Error en la solicitud de datos para el volumen de transacciones por criptomoneda")
    
# marketcap    
response = requests.get('http://fastapi:8000/marketcap_histogram')
if response.status_code == 200:
    marketcap_histogram_data = response.json()
    
    st.header("Histograma del MarketCap por Criptomoneda")
    if marketcap_histogram_data:
        df_marketcap_histogram = pd.DataFrame(marketcap_histogram_data)
        fig_hist = px.histogram(df_marketcap_histogram, x='MarketCap', color='Symbol', marginal='rug',
                                hover_data={'MarketCap': ':.2f', 'Symbol': True})
        st.plotly_chart(fig_hist, use_container_width=True)
        logging.info("Visualización del marketcap por criptomoneda generada exitosamente")
    else:
        st.write("No se pudieron obtener los datos para la visualización.")
        logging.warning("No se encontraron datos para el valor del marketcap por criptomoneda")
else:
    st.write("No se pudieron obtener los datos para la visualización.")
    logging.error("Error en la solicitud de datos para el valor del marketcap por criptomoneda")

# high_low_relation
response = requests.get('http://fastapi:8000/high_low_relation')
if response.status_code == 200:
    high_low_relation_data = response.json()
    
    st.header("Relación entre precios altos y bajos por criptomoneda")
    if high_low_relation_data:
        df_high_low_relation = pd.DataFrame(high_low_relation_data)
        fig = px.scatter(df_high_low_relation, x='High', y='Low', color='Symbol',
                        hover_data={'High': ':.2f', 'Low': ':.2f', 'Symbol': True})
        st.plotly_chart(fig, use_container_width=True)
        logging.info("Visualización de la relación entre precios altos y bajos por criptomoneda generada exitosamente")
    else:
        st.write("No se pudieron obtener los datos para la visualización.")
        logging.warning("No se encontraron datos para la relación entre precios altos y bajos por criptomoneda")
else:
    st.write("No se pudieron obtener los datos para la visualización.")
    logging.error("Error en la solicitud de datos para la relación entre precios altos y bajos por criptomoneda")