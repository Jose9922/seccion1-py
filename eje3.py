# Cree un programa que lea el monto de un préstamo y el plazo en meses, y muestre al usuario el valor las
#cuotas mensuales pagando un interés fijo del 2.7% mensual.
# Solicitar el monto del préstamo y el plazo en meses
monto_prestamo = float(input("Ingrese el monto del préstamo: "))
plazo_meses = int(input("Ingrese el plazo en meses: "))

# Calcular la tasa de interés mensual (2.7% mensual)
tasa_interes_mensual = 2.7 / 100

# Calcular la cuota mensual usando la fórmula de amortización
cuota_mensual = (monto_prestamo * tasa_interes_mensual) / (1 - (1 + tasa_interes_mensual)**-plazo_meses)

# Mostrar el resultado
print(f"\nCuota mensual a pagar: {cuota_mensual:.2f} USD")
