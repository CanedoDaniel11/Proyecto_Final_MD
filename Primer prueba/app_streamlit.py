import streamlit as st
import pandas as pd
import math

#Escribimos texto con este comando
st.write('Esta es mi primer app web')
st.write('El mejor día es...')
st.write('Faltan 3 días para el examen')

#creamos un slider con limites [0,10] y salto de 1
s=st.slider('slider', 0, 10,1)
#asociamos el slider con una función f(x)=x^2
st.write('El cuadrado de {} es'.format(s), s*s)


st.write('PROBLEMA 1: Genera un slider que comience en 0 y termine en 50 con saltos del 10 y dar los resultados de evaluar los valores del slider en la función f(x)=e^x')

slider1 = st.slider('Valores', 0, 50, 10,)
st.write('La función evaluada en {} da: '.format(slider1), math.e**slider1)