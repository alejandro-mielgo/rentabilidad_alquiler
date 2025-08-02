from montecarlo import generate_variable, generate_histogram
from hipoteca import calcular_hipoteca

n=100000

precio_compra = generate_variable(170_000, 190_000, n, "normal")
impuestos_compra = 0.08
gastos_notaria = generate_variable(800,1000,n,"normal")
coste_reforma = generate_variable(40_000, 45_000 ,n ,"normal")
coste_muebles = generate_variable(4500, 5500,n,"normal")

alquiler_mensual = generate_variable(900,1000,n,"normal")

comunidad = 1200
ibi = generate_variable(120,130,n,"normal")
basuras = generate_variable(80,100,n,"normal")
seguro = generate_variable(120,130,n,"normal")
mantenimiento = generate_variable(800,900,n,"normal")
ocupacion = generate_variable(0.93,0.97,n,"normal")


inversion_total = precio_compra*(1+impuestos_compra) + coste_reforma + coste_muebles + gastos_notaria
alquiler_anual_bruto = alquiler_mensual*12*ocupacion
alquiler_anual_neto = alquiler_anual_bruto -comunidad -ibi -basuras -seguro -mantenimiento

rentabilidad_bruta = alquiler_anual_bruto/inversion_total
rentabilidad_neta = alquiler_anual_neto/inversion_total

generate_histogram(inversion_total, title="inversion total", bins=20 )
generate_histogram(alquiler_anual_bruto, title="alquiler anual bruto", bins=20)
generate_histogram(alquiler_anual_neto, title="alquiler anual neto", bins=20 )
generate_histogram(rentabilidad_bruta, title="rentabilidad bruta", bins=20 )
generate_histogram(rentabilidad_neta, title="rentabilidad neta", bins=20)


print(f"inversion total: {inversion_total.mean()}")
print(f"rentabilidad bruta: {rentabilidad_bruta.mean()}")
print(f"rentabilidad neta: {rentabilidad_neta.mean()}")
