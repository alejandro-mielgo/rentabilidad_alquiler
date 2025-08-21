import streamlit as st
from montecarlo import generate_variable, generate_histogram
from hipoteca import calcular_hipoteca

dist_options = {"normal":"normal","uniforme":"uniform","triangular":"triangular"}

st.markdown("# Calculadora rentabilidad del alquiler")


precio_compra= st.number_input("Precio de compra", min_value=0, value=200_000, step=1000)
impuestos_compra = st.number_input("Impuestos", min_value=0.0, max_value=1.0, value=0.08)

hipoteca = st.checkbox("Hipoteca")
if hipoteca:
    importe_hipoteca = st.number_input("Importe hipoteca", min_value=0, value=150000, step=1000)
    plazo_hipoteca = st.number_input("Plazo de la hipoteca (años)", min_value=1, value=30, step=1)
    tipo_interes = st.number_input("Tipo de interés (anual)", min_value=0.0, value=3.0, step=0.1)
    cuota,total_intereses, intereses_1_year,pagos = calcular_hipoteca(importe_hipoteca, plazo_hipoteca, tipo_interes/100)
    st.write(f"Cuota mensual: {cuota:.2f} €")
    st.write(f"Intereses primer año: {intereses_1_year:.2f} €")
    st.write(f"Intereses total: {total_intereses:.2f} €")
    st.markdown("---")

c1,c2,c3 = st.columns(3)
with c1:
    alquiler_mensual_min = st.number_input("Alquiler (estimación baja)", min_value=0, value=800)
    tasa_ocupacion_min = st.number_input("Tasa ocupación (est baja)", min_value=0.0, max_value=1.0, value=0.94)   
with c2:
    alquiler_mensual_max = st.number_input("Alquiler (estimación alta)", min_value=0, value=1000)
    tasa_ocupacion_max = st.number_input("Tasa ocupación (est alta)", min_value=0.0, max_value=1.0, value=0.97)  
with c3:
    dist_alquiler = dist_options[st.selectbox("Distribución",options=dist_options.keys(),key=111)]
    dist_tasa_ocupacion = dist_options[st.selectbox("Distribución",options=dist_options.keys(),key=112)] 

st.markdown("---")
col_1, col_2, col_3 =st.columns(3)
with col_1:
    gastos_notaria_min = st.number_input("Gastos de notaría (estimación baja)", min_value=0, value=800)
    coste_reforma_min = st.number_input("Gastos de reforma (estimación baja)", min_value=0, value=20000)
    coste_muebles_min = st.number_input("Gastos en mobiliario (estimación baja)", min_value=0, value=5000)
with col_2:
    gastos_notaria_max = st.number_input("Gastos de notaría (estimación alta)", min_value=0, value=900)
    coste_reforma_max = st.number_input("Gastos de reforma (estimación alta)", min_value=0, value=25000)
    coste_muebles_max = st.number_input("Gastos en mobiliario (estimación baja)", min_value=0, value=6000)
with col_3:
    dist_gatos_notaria = dist_options[st.selectbox("Distribución",options=dist_options.keys(), key=11)]
    dist_gatos_reforma = dist_options[st.selectbox("Distribución",options=dist_options.keys(), key=12)]
    dist_gatos_muebles = dist_options[st.selectbox("Distribución",options=dist_options.keys(), key=13)]

st.markdown("---")

c_1, c_2, c_3 =st.columns(3)
with c_1:
    gastos_comunidad_min = st.number_input("Comunidad (anual, estimación baja)", min_value=0, value=800)
    gastos_ibi_min = st.number_input("IBI (anual, estimación baja)", min_value=0, value=500)
    gastos_seguro_min = st.number_input("seguro (anual, estimación baja)", min_value=0, value=90)
    gastos_mantenimiento_min=st.number_input("mantenimiento (anual, est baja)", min_value=0, value=600)
with c_2:
    gastos_comunidad_max = st.number_input("Comunidad (anual, estimación alta)", min_value=0, value=900)
    gastos_ibi_max = st.number_input("IBI (anual, estimación alta)", min_value=0, value=600)
    gastos_seguro_max = st.number_input("seguro (anual, estimación alta)", min_value=0, value=120)
    gastos_mantenimiento_max=st.number_input("mantenimiento (anual, est alta)", min_value=0, value=800)
with c_3:
    dist_gatos_comunidad = dist_options[st.selectbox("Distribución", options=dist_options.keys(), key=21)]
    dist_gatos_ibi = dist_options[st.selectbox("Distribución", options=dist_options.keys(), key=22)]
    dist_gatos_seguro = dist_options[st.selectbox("Distribución", options=dist_options.keys(), key=23)]
    dist_gatos_mantenimiento = dist_options[st.selectbox("Distribución", options=dist_options.keys(), key=24)]

st.markdown("---")
 
n = st.slider("Número de simulaciones", min_value=0, max_value = 100000, value=50000)


gastos_notaria = generate_variable(gastos_notaria_min,gastos_notaria_max, n,dist_gatos_notaria)
coste_reforma = generate_variable(coste_reforma_min, coste_reforma_max, n ,dist_gatos_reforma)
coste_muebles = generate_variable(coste_muebles_min, coste_muebles_max,n,dist_gatos_muebles)

alquiler_mensual = generate_variable(alquiler_mensual_min,alquiler_mensual_max,n,dist_alquiler)
tasa_ocupacion = generate_variable(tasa_ocupacion_min, tasa_ocupacion_max, n, dist_tasa_ocupacion)



comunidad = generate_variable(gastos_comunidad_min, gastos_comunidad_max, n, dist_gatos_comunidad)
ibi = generate_variable(gastos_ibi_min, gastos_ibi_max, n, dist_gatos_ibi)
seguro = generate_variable(gastos_seguro_min, gastos_seguro_max, n, dist_gatos_seguro)
mantenimiento = generate_variable(gastos_mantenimiento_min,gastos_mantenimiento_max,n,dist_gatos_mantenimiento)



inversion_total = precio_compra*(1+impuestos_compra) + coste_reforma + coste_muebles + gastos_notaria
alquiler_anual_bruto = alquiler_mensual*12*tasa_ocupacion
alquiler_anual_neto = alquiler_anual_bruto -comunidad -ibi -seguro -mantenimiento

cash_flow_mensual = alquiler_anual_neto/12
rentabilidad_bruta = alquiler_anual_bruto/inversion_total
rentabilidad_neta = alquiler_anual_neto/inversion_total

if hipoteca:
    inversion_total = precio_compra*impuestos_compra + (precio_compra-importe_hipoteca) + coste_reforma + coste_muebles + gastos_notaria
    cash_flow_mensual = cash_flow_mensual - cuota
    rentabilidad_bruta = alquiler_anual_bruto/inversion_total
    rentabilidad_neta = (alquiler_anual_neto - intereses_1_year)/inversion_total

fig_rentabilidad = generate_histogram(rentabilidad_neta,"rentabilidad neta", bins=30)
fig_cash_flow= generate_histogram(cash_flow_mensual,"cash flow mensual neto", bins=30)
st.pyplot(fig_rentabilidad)
st.pyplot(fig_cash_flow)