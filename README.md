# leads300
Desarrollado por SERGIO EMILIANO LOPEZ BAUTISTA [08 05 2025]
Colaboración con:


NOTA IMPORTANTE:En caso de hacer una modificación, colocarla en una nueva rama.
                Si se logra una nueva versión estable, coloca tu nombre en el apartado de COLABORACIÓN y notificalo en este README.md con los cambios agregados respecto a la versión anterior.

= V.3.0.0 = 
    Versión beta
La comunicación entre agentes no Fue eficiente, debido a la topología de comunicación diseñada inicialmente, lo que arrojaba

= V.3.0.1 = 
    Primera versión estable
Usando agentes de IA, impulsados por Open AI, se espera conseguir una herramienta de busqueda y analisis, para alcanzar nuevos clientes y dar pie a un directorio actualizado para pequeños negocios y empresas. 
Esta versión se probó solamente con la lógica de los agentes trabajando en colaboración en un entorno de colab.

= V.3.1.1 =
    Versión web
Se tomó la primera versión estable y se integró con el framework de streamlit para poder desplegarse en la web usando los servicios disponibles de interfaz y de distribución.
POR MOTIVOS DE SEGURIDAD el archivo .env que incluye la API KEY de OpenAI no se incluye en el repositorio, evitando exponer datos sensibles, además de que al intentarlo, OpenAI inabilita automáticamente la API key.
Deido a ese motivo, para poder probarlo localmente, se necesita una API KEY propia.
    FUN FACT: Esta fue la primera versión que se colocó en un repositorio de GitHub, de ahí el nombre del archivo principal "311leads.py"

= V.3.1.5 =
Los pequeños cambios hechos a la versión involucran:
    El cambio de las cadenas concatenadas con variables al formato f-strings
    La eliminación de la función crear_documento(), ya que no era necesario ese paso extra en el procesamiento
    La optimización de los prompts para una busqueda más objetiva, logrando tener un directorio y no solamente información general
    La petición directa y específica de que los datos proporcionados sean verídicos y ninguno sea generado artificalmente con fines ilustrativos

= V.3.1.7 =
Respecto a la versión anterior se agrega:
    Pequeñas sugerencias de respuesta en la pregunta de la zona
    La información de la vista previa se despliega como una maquina de escribir
*Esta versión no se incluyó en un commit de Git*

= V.3.2.7 =
    Cambios a la interfaz visual
Dentro de los cambios más notables ala interfaz para mejorar el uso:
    Se agregó una lista de opciones a la pregunta acerca de la industria y una opción para agregar una especificación fuera de la lista propuesta
    Instrucciones generales del proposito del formulario y el modo de uso