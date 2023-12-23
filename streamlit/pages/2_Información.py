import streamlit as st
import pandas as pd
import requests
import logging
 
st.set_page_config(page_title='Información', layout='wide')

# Configuración básica del logger
logging.basicConfig(filename='app_logs.log', level=logging.INFO)

@st.cache_data
def load_data(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        st.error("Error en la solicitud")
        return None
    else:
        df = pd.DataFrame(r.json())
        return df

df = load_data("http://fastapi:8000/all_data")

st.title("Información sobre las distinta criptomonedas: ")

st.markdown("En este proyecto se analizaran las siguientes criptomonedas:")
st.markdown("       - BITCOIN")
st.markdown("       - ETHEREUM")
st.markdown("       - CARDANO")
st.markdown("       - POLKADOT")
st.markdown("       - SOLANA")
st.markdown("       - TETHER")
st.markdown("""Cada una de estas criptomonedas tiene su propio enfoque, tecnología subyacente y aplicación dentro del mundo de las finanzas descentralizadas y la tecnología blockchain.
            Revisemoslas una por una:""")

st.markdown("### BITCOIN ")
st.image('pages/btc.png')
st.markdown("Link pagina web: https://bitcoin.org/es/")
st.markdown("Link whitepaper: https://bitcoin.org/bitcoin.pdf")
st.markdown("Link coinmarketcap: https://coinmarketcap.com/currencies/bictoin/")
st.markdown("Símbolo: BTC")
st.markdown("Propósito: Fue creada como un sistema de efectivo digital peer-to-peer descentralizado. Busca permitir transacciones directas entre usuarios sin la necesidad de intermediarios, utilizando la tecnología blockchain para garantizar la seguridad y la transparencia de las transacciones.")
st.markdown("Valor: Es la criptomoneda más conocida y con mayor capitalización de mercado. Además de ser una forma de inversión, se utiliza como reserva de valor y como medio de intercambio en diversas transacciones en línea y comercios que la aceptan como forma de pago.")
st.markdown("Estadisticos descrptivos: ")

# Filtrar solo los datos relacionados con Bitcoin (BTC)
btc_df = df[df['Symbol'] == 'BTC']
# Calcular estadísticos descriptivos para Bitcoin
btc_stats = btc_df.describe()
st.write("Estadísticas descriptivas para Bitcoin (BTC):")
st.dataframe(btc_stats)
logging.info(f"Display de estadísticas descriptivas para Bitcoin realizado con exito")

st.markdown("### ETHEREUM ")
st.image('pages/eth.png')
st.markdown("Link pagina web: https://ethereum.org/en/")
st.markdown("Link whitepaper: https://ethereum.org/en/whitepaper/")
st.markdown("Link coinmarketcap: https://coinmarketcap.com/currencies/ethereum/")
st.markdown("Símbolo: ETH")
st.markdown("Propósito: Ethereum es una plataforma blockchain que permite la creación de contratos inteligentes y aplicaciones descentralizadas. Busca proporcionar a los desarrolladores un entorno para construir y desplegar dApps, permitiendo la programación de acuerdos digitales.")
st.markdown("Funcionalidad: Su red es fundamental en el desarrollo de tokens no fungibles (NFTs) y ha sido utilizada para lanzar numerosos proyectos y protocolos descentralizados en el ámbito financiero y más allá.")
# Filtrar solo los datos relacionados con Ethereum (ETH)
eth_df = df[df['Symbol'] == 'ETH']
# Calcular estadísticos descriptivos para Ethereum
eth_stats = eth_df.describe()
st.write("Estadísticas descriptivas para Ethereum (ETH):")
st.dataframe(eth_stats)
logging.info(f"Display de estadísticas descriptivas para Ethereum realizado con exito")

st.markdown("### CARDANO ")
st.image('pages/ada.png')
st.markdown("Link pagina web: https://cardano.org")
st.markdown("Link whitepage: https://docs.cardano.org/introduction/")
st.markdown("Link coinmarketcap:https://coinmarketcap.com/currencies/cardano/")
st.markdown("Símbolo: ADA")
st.markdown("Propósito: Cardano es una plataforma blockchain que se enfoca en la escalabilidad, la interoperabilidad y la sostenibilidad. Su objetivo principal es ofrecer una infraestructura para la creación de contratos inteligentes y aplicaciones descentralizadas (dApps), con un enfoque en la gobernanza y la seguridad.")
st.markdown("Tecnología: Utiliza un enfoque científico y una filosofía basada en la investigación académica para desarrollar su protocolo, promoviendo la escalabilidad y la seguridad.")
# Filtrar solo los datos relacionados con Cardano (ADA)
ada_df = df[df['Symbol'] == 'ADA']
# Calcular estadísticos descriptivos para Cardano
ada_stats = ada_df.describe()
st.write("Estadísticas descriptivas para Cardano (ADA):")
st.dataframe(ada_stats)
logging.info(f"Display de estadísticas descriptivas para Cardano realizado con exito")

st.markdown("### POLKADOT ")
st.image('pages/dot.png')
st.markdown("Link pagina web: https://polkadot.network")
st.markdown("Link whitepage: https://polkadot.network/whitepaper/")
st.markdown("Link coinmarketcap: https://coinmarketcap.com/currencies/polkadot-new/")
st.markdown("Símbolo: DOT")
st.markdown("Propósito: Polkadot es una red blockchain diseñada para facilitar la interoperabilidad entre diferentes blockchains. Su objetivo principal es permitir la transferencia de datos y activos entre distintas cadenas de bloques, mejorando la escalabilidad y la gobernanza descentralizada.")
st.markdown("Tecnología: Utiliza una estructura de múltiples cadenas que se comunican entre sí, permitiendo que blockchains independientes interactúen y compartan información de manera segura.")
# Filtrar solo los datos relacionados con Polkadot (DOT)
dot_df = df[df['Symbol'] == 'DOT']
# Calcular estadísticos descriptivos para Polkadot
dot_stats = dot_df.describe()
st.write("Estadísticas descriptivas para Polkadot (DOT):")
st.dataframe(dot_stats)
logging.info(f"Display de estadísticas descriptivas para Polkadot realizado con exito")

st.markdown("### SOLANA ")
st.image('pages/sol.png')
st.markdown("Link pagina web: https://solana.com/es")
st.markdown("Link whitepage: https://solana.com/solana-whitepaper.pdf")
st.markdown("Link coinmarketcap: https://coinmarketcap.com/currencies/solana/")
st.markdown("Símbolo: SOL")
st.markdown("Propósito: Solana es una red blockchain de alto rendimiento que busca mejorar la escalabilidad y el rendimiento de las aplicaciones descentralizadas. Ofrece tiempos de confirmación rápidos y tarifas bajas, siendo una plataforma atractiva para proyectos que requieren alta velocidad y capacidad.")
st.markdown("Tecnología: Utiliza un enfoque único de prueba de historia (Proof of History) combinado con otras innovaciones para lograr altas velocidades de transacción y escalabilidad.")
# Filtrar solo los datos relacionados con Solana (SOL)
sol_df = df[df['Symbol'] == 'SOL']
# Calcular estadísticos descriptivos para Solana
sol_stats = sol_df.describe()
st.write("Estadísticas descriptivas para Solana (SOL):")
st.dataframe(sol_stats)
logging.info(f"Display de estadísticas descriptivas para Solana realizado con exito")

st.markdown("### TETHER ")
st.image('pages/usdt.png')
st.markdown("Link pagina web: https://tether.to/es/")
st.markdown("Link whitepage: https://tether.to/es/transparency/#usdt")
st.markdown("Link coinmarketcap: https://coinmarketcap.com/currencies/tether/")
st.markdown("Símbolo: USDT")
st.markdown("Propósito: Tether es una criptomoneda conocida como 'stablecoin' ya que está vinculada al valor de una moneda fiduciaria, como el dólar estadounidense. Su propósito principal es proporcionar estabilidad de valor y liquidez en el ecosistema de las criptomonedas, actuando como un puente entre las monedas tradicionales y el mundo cripto.")
st.markdown("Función: Se utiliza comúnmente como un refugio de valor para los traders y como una forma de mover fondos rápidamente entre diferentes exchanges, manteniendo un valor cercano a la moneda fiduciaria a la que está anclada.")
# Filtrar solo los datos relacionados con Tether (USDT)
usdt_df = df[df['Symbol'] == 'USDT']
# Calcular estadísticos descriptivos para Tether
usdt_stats = usdt_df.describe()
st.write("Estadísticas descriptivas para Tether (USDT):")
st.dataframe(usdt_stats)
logging.info(f"Display de estadísticas descriptivas para Tether realizado con exito")


