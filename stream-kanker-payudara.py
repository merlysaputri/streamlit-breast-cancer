import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('klasifikasi-kanker-payudara.sav', 'rb'))

# judul web
st.title ('Classification of Breast Cancer Diagnoses')

col1, col2 = st.columns(2)

with col1:
    radius_mean = st.text_input('Input Nilai Radius Mean')
with col2:
    texture_mean = st.text_input('Input Nilai Texture Mean')
with col1:
    perimeter_mean = st.text_input('Input Nilai Perimeter Mean')
with col2:
    area_mean = st.text_input('Input Nilai Area Mean')
with col1:
    smoothness_mean = st.text_input('Input Nilai Smoothness Mean')
with col2:
    compactness_mean = st.text_input('Input Nilai Compactness Mean')
with col1:
    concavity_mean = st.text_input('Input Nilai Concavity Mean')
with col2:
    concave_points_mean = st.text_input('Input Nilai Concave Points Mean')
with col1:
    symmetry_mean = st.text_input('Input Nilai Symmetry Mean')
with col2:
    fractal_dimension_mean = st.text_input('Input Nilai Fractal Dimension Mean')

# code for classifier
breast_cancer_diagnosis = ''

# Membuat tombol klasifikasi diagnosa
if st.button('Hasil Diagnosa'):
    breast_cancer_prediction = model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]])

    if (breast_cancer_prediction[0]==0):
        breast_cancer_diagnosis = 'Pasien Mengidap Penyakit Kanker Payudara Bersifat Jinak'
    else:
        breast_cancer_diagnosis = 'Pasien Mengidap Penyakit Kanker Payudara Bersifat Ganas'
    st.success(breast_cancer_diagnosis)







