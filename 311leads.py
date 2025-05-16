###################################################
# Generador de leads V.3.1.1                      #
# Impulsado en un servidor local con streamlit    #
# Agentes impulsados con OpenAI                   #
# Desarrollador: Sergio Emiliano López Bautista   #
# Última modificación 15/05/2025                  #
###################################################


# ------------------------- Requerimentos y librerías -------------------------------
import io
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from docx import Document

# ------------------- Estructura de Cliente para almacenar datos ---------------------
class Cliente:
    def __init__(self, industria, postores, producto, zona):
        self.industria = industria
        self.postores = postores
        self.producto = producto
        self.zona = zona


# --------------------------- Seteadores ----------------------------------------------
st.set_page_config(page_title="Generador de diccionario", layout="wide")
#dotenv_path = find_dotenv()
#load_dotenv(dotenv_path, override=True)
#client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key = st.secrets("OPENAI_API_KEY"))
#OpenAI.api_key = st.secrets["OPENAI_API_KEY"]
#client = OpenAI(OpenAI.api_key)


# --------------------------- Funciones -----------------------------------------------
def agente1(cliente):
    try:
        agente1 = client.responses.create(
        model="gpt-4.1",
        input="Dame únicamente el prompt necesario para poder buscar información de clientes potenciales en "+ cliente.industria +"que sean similares a "+ cliente.postores +" y tengan como producto "+ cliente.producto +"en la zona de "+ cliente.zona + "."
        )
        return agente1.output_text
    
    except Exception as e:
        st.error(f"Error al generar una respuesta: {str(e)}")
        return None

def agente2(prompt):
    try:
        agente2 = client.responses.create(
        model= "gpt-4.1",
        input= prompt
        )
        return agente2.output_text

    except Exception as e:
        st.error(f"Prompt de busqueda inválido: {str(e)}")
        return None

def agente3(respuesta2):
    try:
        agente3 = client.responses.create(
        model= "gpt-4.1",
        input= "Si la información de "+ respuesta2 +"no es suficientemente en cantidad o detalle, optimizala para generar leads y entregame solamente el prompt neceario para generar leads basado en esa información"
        )
        return agente3.output_text

    except Exception as e:
        st.error(f"xdxdxd: {str(e)}")
        return None

def agente4(prompt2):
    try:
        agente4 = client.responses.create(
        model= "gpt-4.1",
        input= "Dame solamente los leads basado en"+ prompt2 +"y no hagas preguntas finales"
        )
        return agente4.output_text
    
    except Exception as e:
        st.error(f"Error al encontrar los clientes: {str(e)}")
        return None

def crear_documento(datos):
    return str(datos)


# ---------------------------------- Interfaz ----------------------------------------------
st.title("Generador de diccionario con clientes potenciales")

st.header("Ayudame proporcionandome esta información:")
p4 = " "
cliente = Cliente("a","b","c","d")
with st.spinner("Buscando clientes..."):
    with st.form("form"):
        ind = st.text_input("¿En qué industria estás? ")
        pos = st.text_input("¿A quiénes les vendes? ")
        prod = st.text_input("¿Qué vendes? ")
        zona = st.text_input("¿En qué zona buscas clientes? ")    

        usuario = st.form_submit_button("Aceptar")
        if usuario:
            if ind or pos or prod or zona:
                cliente = Cliente(ind, pos, prod, zona)
                p1 = agente1(cliente)
                p2 = agente2(p1)
                p3 = agente3(p2)
                p4 = agente4(p3)

                st.success("Clientes potenciales encontrados")
                st.markdown("### Vista previa de la información")
                st.markdown(p4)

            else:
                st.warning("Por favor completa los campos requeridos")

    if p4 != " ":
        st.download_button(
            label = "Descargar información",
            data = crear_documento(p4),
            file_name = "información_"+ cliente.industria + ".txt",
            mime = "text/plain"
        )
