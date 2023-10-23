import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

def get_instance_metadata():
    try:
        metadata_url = "http://169.254.169.254/latest/meta-data/"
        instance_id = requests.get(metadata_url + "instance-id").text
        availability_zone = requests.get(metadata_url + "placement/availability-zone").text
        return instance_id, availability_zone
    except requests.exceptions.RequestException as e:
        return None, None

st.set_page_config(page_title="Defensa App", page_icon="🎓", layout="wide")

# ----- CARGAR ASETS -----
lottie_cloud = load_lottieurl("https://lottie.host/735f6c67-ef44-4be4-8b72-e39bc5476636/9oyHlXIsok.json")
# ----- ENCABEZADO -----
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Aplicación para defensa de Modalidad de Grado II 🎓")
        st.title("Erick Sebastián Hoyos Arízaga")
        st.write("Universidad Privada Domingo Savio")
    with right_column:
        st_lottie(lottie_cloud, height=350, key="cloud")

# ----- CONTENIDO DE LA APLICACIÓN -----
with st.container():
    instance_id, availability_zone = get_instance_metadata()
    st.write("---")
    if instance_id != None:
        st.title(f"ID de instancia EC2: {instance_id}")
    else:
        st.title("ID de instancia EC2: desconocido")
    if availability_zone != None:
        st.title(f"Zona de Disponibilidad: {availability_zone}")
    else: 
        st.title("Zona de Disponibilidad: desconocida")
