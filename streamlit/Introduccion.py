import streamlit as st

st.set_page_config(page_title='Introduccion', layout='wide')

st.title("Análisis del crecimiento de las criptomonedas")

st.image('criptos.png', use_column_width=True)

st.sidebar.success("Páginas: selecciona según lo que quieras visualizar :)")

st.markdown(
    """
¡Bienvenido a mi panel de control personalizado para explorar el emocionante mundo de las criptomonedas! 
Este espacio está diseñado para que puedas sumergirte en el fascinante crecimiento de diversas criptodivisas a lo largo del tiempo.

Aquí, encontrarás una variedad de gráficos interactivos que capturan la evolución de las criptomonedas más destacadas, este panel te brinda una visión detallada del pasado de estos activos digitales para que así se puedan sacar conclusiones de cara a una inversion futura.

Además, verás datos en tiempo real, análisis históricos y proyecciones fundamentadas que te permitirán comprender mejor el complejo mundo de Bitcoin, Ethereum y otras criptomonedas. Podrás explorar sus ascensos, analizar las fluctuaciones del mercado y descubrir patrones de crecimiento que han transformado la economía global.

Sumérgete en la experiencia interactiva que te ofrece este dashboard. Explora las correlaciones entre diferentes monedas, descifra las tendencias emergentes y obtén una comprensión más profunda de cómo estas criptodivisas están moldeando el panorama financiero.

Estoy encantado de presentarte esta herramienta que te permitirá descubrir el vibrante universo de las criptomonedas. ¡Adelante, comienza a explorar y a desentrañar los secretos de este emocionante mercado financiero digital!
"""
)
