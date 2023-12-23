import streamlit as st
 
st.set_page_config(page_title='Información', layout='wide')

st.title("Blockchain: ")
st.markdown("Para entender este proyecto relacionado con las criptomonedas, previamente tenemos que entender lo que es la blockchain: ")

st.markdown("La blockchain es una tecnología prometedora que ofrece una forma segura y transparente de almacenar y transferir datos, y su potencial va más allá de las criptomonedas.")

st.markdown("### ")
st.markdown("### ¿Qué es la Blockchain? ")
st.markdown("La blockchain es un registro digital (o libro mayor) que registra transacciones de manera permanente en bloques, que luego se encadenan entre sí cronológicamente. Cada bloque contiene un conjunto de transacciones verificadas y una referencia al bloque anterior, formando así una cadena continua de bloques.")

st.markdown("### Principios Fundamentales:")
st.markdown("Descentralización: En lugar de estar almacenada en un servidor centralizado, la información en la blockchain se distribuye a través de una red de nodos (computadoras) que verifican y validan las transacciones.")
st.markdown("Inmutabilidad: Una vez que la información se agrega a un bloque y este se añade a la cadena, es extremadamente difícil o casi imposible modificar esa información debido a la criptografía y a la estructura de enlace de los bloques.")
st.markdown("Seguridad mediante Criptografía: Cada bloque en la blockchain contiene un hash criptográfico único, generado a partir de la información del bloque anterior y su propio contenido. Esto asegura que cualquier intento de modificar un bloque se haga evidente en toda la red.")

st.markdown("### ¿Cómo Funciona?")
st.markdown("Registro de Transacciones: Cuando se realiza una transacción, esta se agrupa con otras transacciones en un bloque.")
st.markdown("Verificación y Consenso: Los nodos de la red (mineros o validadores) verifican la validez de las transacciones y compiten para resolver complejos problemas matemáticos para añadir el bloque a la cadena.")
st.markdown("Consenso Distribuido: Una vez que la mayoría de los nodos validan la autenticidad de las transacciones en un bloque, se alcanza un consenso y se agrega el bloque a la cadena.")

st.markdown("### Tipos de Blockchain:")
st.markdown("Públicas: Accesibles para cualquiera, como Bitcoin y Ethereum. Cualquier persona puede unirse, ver transacciones y participar en la red.")
st.markdown("Privadas: Restringidas y controladas por una entidad o un consorcio. Se utilizan en aplicaciones empresariales donde la transparencia total no es necesaria o no está permitida.")
st.markdown("Consorcio o Federadas: Un grupo de organizaciones administra la red, común en aplicaciones de industrias específicas donde se requiere un cierto nivel de permisos.")

st.markdown("### Aplicaciones de la Blockchain:")
st.markdown("Criptomonedas y Finanzas: Facilita transacciones seguras y sin intermediarios.")
st.markdown("Contratos Inteligentes: Programas autoejecutables que funcionan según reglas predefinidas.")
st.markdown("Gestión de Identidad: Ofrece una forma segura de verificar la identidad sin revelar información sensible.")
st.markdown("Cadena de Suministro: Rastrea el origen y el recorrido de productos desde su fabricación hasta su entrega.")

st.markdown("### Para entenderlo mejor dejo un vídeo en el que se explica la blockchain y todo lo que hay que saber de ella: ")

video_file = open('pages/video_blockchain.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
