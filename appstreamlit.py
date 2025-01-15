# Mensaje de entrada del usuario


import os
import openai
import streamlit as st
import requests

<<<<<<< HEAD
#print(openai.api_base)
=======

print(openai.api_base)
>>>>>>> 9f8238b232a91f23cad02b299c96d95e3e08e0b7
# Configurar la clave API para OpenAI
from dotenv import load_dotenv
print("Dotenv library imported successfully!")
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key=ael repositorio de GitHub
usuario_github = "marcelomrinelli"  # Tu nombre de usuario en GitHub
repositorio = "app-curso"  # El nombre del repositorio
ruta = ""  # La ruta dentro del repositorio, déjala vacía si es la raíz

# Configuración del repositorio de GitHub
usuario_github = "marcelomrinelli"  # Tu nombre de usuario en GitHub
repositorio = "app-curso"  # El nombre del repositorio
ruta = ""  # La ruta dentro del repositorio, déjala vacía si es la raíz


# Función para obtener archivos desde un repositorio de GitHub
def obtener_archivos_github(usuario, repositorio, ruta=""):
    url = f"https://api.github.com/repos/{usuario}/{repositorio}/contents/{ruta}"
    response = requests.get(url)
    archivos = response.json()
    if isinstance(archivos, list):  # Verifica si la respuesta contiene archivos
        return archivos
    else:
        st.error("Error al obtener archivos del repositorio.")
        return []

# Función para cargar documentos desde GitHub
def cargar_documentos(ruta=""):
    """
    Lee todos los archivos de texto en un repositorio de GitHub y combina su contenido.
    """
    documentos = {}
    archivos_github = obtener_archivos_github(usuario_github, repositorio, ruta)
    for archivo in archivos_github:
        if archivo['name'].endswith('.txt'):
            url_archivo = archivo['download_url']
            contenido = requests.get(url_archivo).text
            documentos[archivo['name']] = contenido
            print(f"Archivo leído desde GitHub: {archivo['name']}")

    return documentos

def generar_respuesta(pregunta, contexto):
    """
    Genera una respuesta utilizando OpenAI basándose en el contexto proporcionado.
    """
    mensajes = [
        {"role": "system", "content": "Eres un asistente útil que responde preguntas basándose en documentos."},
        {"role": "user", "content": f"Contexto: {contexto}\n\nPregunta: {pregunta}"}
    ]
    
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=mensajes,
        max_tokens=512,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()


# Cargar los documentos al iniciar desde GitHub
documentos = cargar_documentos(ruta)
contexto = "\n".join([f"{nombre}:\n{contenido}" for nombre, contenido in documentos.items()])

# Interfaz con Streamlit
st.title("Asistente de Preguntas para Documentos")
st.write("Haz preguntas basadas en los documentos cargados.")

pregunta = st.text_input("Escribe tu pregunta aquí:")
if st.button("Enviar"):
    if pregunta:
        respuesta = generar_respuesta(pregunta, contexto)
        st.write("**Respuesta:**")
        st.write(respuesta)
    else:
        st.warning("Por favor, escribe una pregunta.")
