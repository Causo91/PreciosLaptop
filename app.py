import streamlit as st
import joblib
import numpy as np

# Cargar el modelo entrenado
model = joblib.load('modelo_entrenado.pkl')

# Título del sitio web
st.title("Predicción del Precio de Laptops")

# Descripción
st.write("Proporcione las especificaciones de la laptop para predecir el precio:")

# Entradas del usuario para las especificaciones de la laptop
memory_size = st.number_input("Tamaño de Memoria (GB):", min_value=1)
screen_widht = st.number_input("Ancho de Pantalla (píxeles):", min_value=800)
screen_height = st.number_input("Alto de Pantalla (píxeles):", min_value=600)
cpu_speed = st.number_input("Velocidad de CPU (GHz):", min_value=0.5, step=0.1)
ram = st.number_input("RAM (GB):", min_value=2)
weight = st.number_input("Peso (kg):", min_value=0.5)
inches = st.number_input("Tamaño de Pantalla (pulgadas):", min_value=10.0)

# Calcular PPI (Pixels Per Inch)
ppi = np.sqrt(screen_widht**2 + screen_height**2) / inches

# Crear features personalizadas
ram_per_weight = ram / weight
cpu_per_weight = cpu_speed / weight
cpu_per_ram = cpu_speed / ram
ppi_per_weight = ppi / weight

# Crear un array con los valores de entrada
input_features = np.array([[memory_size, screen_widht, screen_height, cpu_speed, ram, weight, inches]])

# Predicción
if st.button("Predecir Precio"):
    predicted_price = model.predict(input_features)
    st.write(f"El precio estimado de la laptop es: €{predicted_price[0]:.2f}")