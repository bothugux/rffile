
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

pipe = pickle.load(open('modelo.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))


ssd = st.selectbox('Disco SSD(en GB)',df['HDD_GB'].unique())
hdd = st.selectbox('Disco HDD(in GB)',df['SSD_GB'].unique())
ghz = st.selectbox("CPU GHz", df['Cpu_hgz'].unique())
ram = st.selectbox("Ram(en GB)",df['Ram'].unique())
weight = st.selectbox("Peso de la Laptop",df['Weight'].unique())
touchscreen = st.selectbox("Pantalla TouchScreen", ['No', 'Yes'])
ips = st.selectbox("Pantalla IPS", ['No', 'Yes'])
resolution = st.selectbox(' Resolucion de la pantalla',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
inches = st.selectbox('Tamaño de pantalla',df['Inches'].unique())
screen_width=0
#Prediccion

if st.button('Predecir Precio'):
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == "Yes":
        ips = 1
    else:
        ips = 0
      
    screen_width = int(resolution.split('x')[0])
    input_data = pd.DataFrame([[ssd, ghz, ram, weight, ips, touchscreen, screen_width, hdd, inches]],
                          columns=['SSD_GB', 'Cpu_hgz', 'RAM', 'Weight', 'IPS', 'Touchscreen', 'screen_width', 'HDD_GB', 'Inches'])
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_data)

    # Realizar predicción
    prediction = modelo.predict(input_data )

    # Mostrar predicción
    st.write(f'Precio predecido: {prediction[0]:.2f} euros')

  
