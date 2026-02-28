#################################################################
#                      Generador de leads                       #
# V.3.0.0 //08 05 2025//                                        #
# V.3.0.1 //12 05 2025//                                        #
# V.3.1.1 //16 05 2025//                                        #          
# V.3.1.5 //21 05 2025//                                        #
# V.3.1.7 //23 05 2025//                                        #
# V.3.2.7 //          //                                        #
# V.3.3.8 //13 06 2025//                                        #
# V.3.4.17 //19 02 2026//                                       #
# Desplegado con streamlit                                      #
# Agentes impulsados con OpenAI hasta la versión V.3.3.8        #
# Agente impulsado con Gemini desde la versión V.3.4.17         #
# Desarrollador: Sergio Emiliano López Bautista                 #
#################################################################


# ------------------------- Requerimientos y librerías -------------------------------
import io
import os
import csv
import time
import codecs
import requests
import streamlit as st
import pandas as pd
import asyncio
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from google import genai
from utils.prompts import construir_prompt #Esto toma el archivo de prompts.py



# ------------------- Estructura de Cliente para almacenar datos ---------------------
class Cliente:
    def __init__(self, industria, postores, producto, zona, tamanio):
        self.industria = industria        
        self.postores = postores
        self.producto = producto
        self.zona = zona
        self.tamanio = tamanio
# --------------------------- Seteadores ----------------------------------------------
st.set_page_config(page_title="Robbit - Generador de Leads",
                   page_icon = "data/Robbit_01.png",
                   layout="wide")

dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


col1, col2 = st.columns([1, 5]) # Ajusta la proporción según el tamaño

with col1:
    st.image("data/Robbit_01.png", width=170)
with col2:
    st.title("" \
    "Robbit - Generador de Leads")

# --------------------------- Funciones -----------------------------------------------
def robbit(cliente):
    datos = vars(cliente)
    try:
        robbit = client.models.generate_content(
            model = "gemini-3-flash-preview",
            contents = construir_prompt("data/promptG.txt", datos)
        )
        return robbit.text
    
    except Exception as e:
        st.error(f"Error al generar una respuesta: {str(e)}")
        return None

def maquina_de_escribir(respuesta):
    for word in respuesta.split(" "):
        yield word + " "
        time.sleep(0.02)

def instrucciones():
    with codecs.open("data/instrucciones.txt", "r", encoding="utf-8") as f:
        fi = f.read()
    file = fi.split('\n')
    for linea in file:
        st.markdown(linea)

def parsear_leads(respuesta):
    bloques = respuesta.strip().split("---")
    leads = []

    for bloque in bloques:
        lead = {}
        for linea in bloque.strip().split("\n"):
            if ":" in linea:
                clave, valor = linea.split(":", 1)
                lead[clave.strip()] = valor.strip()
        if lead:
            leads.append(lead)
    return leads
# -------------------------------- Interfaz (MAIN)-----------------------------------------
st.markdown("## ¡Bienvenido!")
instrucciones()

st.sidebar.markdown("# Encontremos a tus clientes ideales")
st.sidebar.header("Completa estos datos clave:")

industria = st.sidebar.selectbox("Industria principal:", 
                                ["Agroindustria", "Alimentos", "Arquitectura", "Artes/Cultural", "Automotriz",
                                 "Bebidas", "Bienes Raíces",
                                 "Ciberseguridad", "Construcción", "Consultoría", "Contabilidad",
                                 "Diseño", "Dispositivos Médicos",
                                 "e-commerce", "e-learning", "Educación", "Energía", "Entretenimiento",
                                 "Farmacéutica", "Finanzas", "Fintech", "Fitness/Wellness",
                                 "Gobierno",
                                 "Hardware Tecnológico", "Hospitales/Clínicas", "Hotelería",
                                 "Industrial", "Inteligencia Artificial",
                                 "Legal", "Logística",
                                 "Manufactura", "Medios", "Moda",
                                 "Nutrición",
                                 "ONGs/Social", "Organismos Gubernamentales",
                                 "Plásticos", "Publicidad/Marketing",
                                 "Química",
                                 "Recursos Humanos", "Retail/Comercio",
                                 "Salud", "Seguros", "Software", "Suplementos",
                                 "Tecnología", "Telecomunicaciones", "Textil", "Transporte", "Turismo",
                                 "Videojuegos", "Otra"],
                                index=None,
                                placeholder="¿En qué sector operas?")

if industria == "Otra":
    industria = st.sidebar.text_input("Especifica:")

postores = st.sidebar.text_input("Clientes ideales:", 
                                 placeholder="¿Qué empresas o perfiles buscas?")
producto = st.sidebar.text_input("Tu producto/servicio", 
                                 placeholder="¿Qué ofreces específicamente?")
zona = st.sidebar.text_input("Zona de cobertura", 
                             placeholder="Estados, regiones, ciudades")
#prioridad = st.sidebar.pills("¿Qué datos son relevantes para ti?", ["Correos", "Telefonos", "Redes sociales"], selection_mode="multi")

tamanio = st.sidebar.pills("Tamaño del cliente", ["Pequeño", "Mediano", "Grande"], selection_mode="multi")

acuerdo = st.sidebar.checkbox("Confirmo que comprendo y acepto que los prospectos son generados automáticamente " \
                      "por Inteligencia Artificial (IA) mediante análisis de fuentes públicas.  " \
                      "La información debe ser verificada antes de ser utilizada, ya que no se garantiza precisión ni disponibilidad de datos. " \
                      "Me comprometo a cumplir con leyes aplicables de protección de datos.")


if acuerdo:
    if st.sidebar.button("🔍 Buscar Prospectos"):
        if all([industria, postores, producto, zona, tamanio]):

            with st.spinner("Recopilando información..."):
                cliente = Cliente(industria, postores, producto, zona, tamanio)

                p4 = robbit(cliente)
                st.success("Clientes encontrados")
                st.markdown(p4)

                leads = parsear_leads(p4)
                df = pd.DataFrame(leads)
                csv_completo=df.to_csv(index=False)

                iz, der = st.columns([1,1], gap="small")
                with iz:
                    st.download_button(
                        label = "Info completa",
                        data = str(p4),
                        file_name = f"información_{cliente.industria}.txt",
                        mime = "text/plain"
                    )
                with der:
                    st.download_button(
                        label="Sólo leads en CSV",
                        data= csv_completo,
                        file_name="leads_CSV.csv",
                        mime="text/csv"
                    )
        else:
            st.sidebar.warning("Por favor completa todos los campos.")