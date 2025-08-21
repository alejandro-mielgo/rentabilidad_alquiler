
def calcular_hipoteca(principal:float, plazo:int, interes:float) -> tuple[float,float,float,list[dict[str,float]]]:
    n_cuotas = plazo*12
    i_m = interes/12
    cuota_mensual = principal * (i_m*(1+i_m)**n_cuotas) / ((1+i_m)**n_cuotas-1)

    pagos = []
    for mes in range(0,n_cuotas):
        interes = principal * i_m
        amortizacion = cuota_mensual-interes
        principal = principal - amortizacion
        pagos.append({"interes":interes,"amortizacion":amortizacion})

    intereses:float = 0.0
    intereses_1_year:float = 0.0
    amortizado:float = 0.0
    for pago in pagos:
        intereses = intereses + pago['interes']
        amortizado = amortizado + pago['amortizacion']
    
    intereses_1_year = sum(p['interes'] for p in pagos[:12])

    return cuota_mensual, intereses,intereses_1_year, pagos


if __name__ == "__main__":
    cuota, intereses,intereses_1_year, pagos = calcular_hipoteca(100000,10,0.015)