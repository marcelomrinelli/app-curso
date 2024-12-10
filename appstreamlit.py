import os
import openai
import streamlit as st



# Mensaje de entrada del usuario

# Ruta a la carpeta con los documentos
ruta_carpeta = r"D:\Datos Usuario\Desktop\curso-electronica"

def cargar_documentos(ruta):
    """
    Lee todos los archivos de texto en una carpeta y combina su contenido.
    """
    documentos = {}
    for archivo in os.listdir(ruta):
        if archivo.endswith(".txt"):
            ruta_completa = os.path.join(ruta, archivo)
            with open(ruta_completa, "r", encoding="utf-8") as f:
                documentos[archivo] = f.read()
    return documentos

def generar_respuesta(pregunta, contexto):
    """
  
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

# Cargar los documentos al iniciar
documentos = cargar_documentos(ruta_carpeta)
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
