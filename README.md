## Panel de Control para Análisis de Criptomonedas

### Introducción:

El panel de control de análisis de criptomonedas es una aplicación web interactiva diseñada para ofrecer una experiencia educativa y visualmente atractiva sobre el mundo de las criptodivisas. Utilizando Streamlit como su marco principal, esta plataforma ofrece una presentación visual impactante que invita a los usuarios a sumergirse en el emocionante mercado de las criptomonedas.

La sección de introducción sirve como el punto de partida, presentando un diseño atractivo con un título distintivo y una imagen representativa del mundo de las finanzas descentralizadas. Además, una barra lateral facilita la navegación entre las diferentes secciones del proyecto, proporcionando un acceso intuitivo a la información sobre la tecnología blockchain, datos específicos de criptomonedas, visualizaciones y más.

### Blockchain:

El apartado dedicado a la tecnología blockchain aprovecha la potencia de Streamlit para ofrecer una explicación detallada y comprensible sobre los principios fundamentales de esta innovadora tecnología. Se abordan conceptos clave, como la descentralización, la inmutabilidad y la seguridad mediante la criptografía, presentando ejemplos claros de cómo la blockchain revoluciona la forma en que se maneja la información y se realizan las transacciones.

Para mejorar la comprensión, se incluye un recurso multimedia, como un vídeo explicativo, que complementa la información textual. Esto ayuda a los usuarios a asimilar mejor los conceptos esenciales de la blockchain y su impacto en diversos sectores.

### Información:

La sección de información proporciona datos detallados sobre una variedad de criptomonedas prominentes, ofreciendo una visión completa de su propósito, función en el ecosistema financiero descentralizado, estadísticas clave y enlaces relevantes para explorar más a fondo. Cada descripción se complementa con imágenes representativas, enlaces a recursos útiles y una narrativa concisa para facilitar la comprensión de las diferencias y similitudes entre las criptodivisas más importantes del mercado.

### Gráficos:

Esta área del proyecto emplea herramientas de visualización como Plotly Express, Matplotlib y Seaborn para generar visualizaciones interactivas basadas en datos reales de criptomonedas. Los gráficos presentan variaciones de precios, volumen de transacciones, distribuciones de capitalización de mercado y relaciones entre los precios altos y bajos. Estas representaciones visuales ayudan a los usuarios a identificar patrones, tendencias y correlaciones en el mercado de las criptodivisas y así entender mejor el desarrollo de dichas criptodivisas y su futuro.

### FastAPI:

El código implementado con FastAPI proporciona un servidor que responde a diversas solicitudes HTTP para obtener datos relacionados con las criptomonedas. Cada endpoint definido ofrece diferentes conjuntos de datos, desde estadísticas generales hasta detalles específicos de cada criptomoneda. Esto garantiza respuestas coherentes y bien formateadas para cada solicitud, mientras se mantiene un registro de eventos en un archivo de registro para rastrear las operaciones y solicitudes realizadas al servidor.

Este sistema integral combina la flexibilidad de Streamlit para visualizar datos y la interacción con el usuario, junto con la robustez de FastAPI para proporcionar datos precisos y detallados sobre las criptodivisas. La combinación de estas herramientas ofrece un panel completo y enriquecedor, útil para inversores, entusiastas o cualquier persona interesada en comprender mejor el mercado de las criptomonedas.

### Ejecución con Docker Compose:
El proyecto está configurado para ejecutarse con Docker Compose. 
Para iniciar la aplicación:

1. Clona este repositorio.
2. Asegúrate de tener Docker y Docker Compose instalados.
3. Situate en la carpeta utilizando el siguiente comando:
        cd "rutaalacarpeta"
4. Para detener y eliminar los contenedores creados por Docker Compose previamente y garantizar un inicio limpio de la aplicación:
        docker-compose down
5. Ejecuta el siguiente comando en la terminal para iniciar la aplicación:
        docker compose up
6. Haz clic en la direccion web que aparece tras ejecutarlo.
7. Si no aparece, cambia la direccion a "localhost:8501"
8. Navega entre las páginas y diviertete!
