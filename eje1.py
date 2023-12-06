# Cree un programa que lea la edad de un usuario y muestre cuántos años tendrá el usuario dentro de tantos años como el usuario indique.
edad_actual = int(input("Ingrese su edad actual: "))

anios_futuro = int(input("Ingrese la cantidad de años en el futuro: "))

edad_futura = edad_actual + anios_futuro

print(f"Dentro de {anios_futuro} años, tendrás {edad_futura} años.")
