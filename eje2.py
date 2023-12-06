#Cree un programa que lea dos números y muestre su producto, su cociente, su módulo, su suma y su resta.
# Solicitar dos números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar operaciones matemáticas
producto = numero1 * numero2
cociente = numero1 / numero2
modulo = numero1 % numero2
suma = numero1 + numero2
resta = numero1 - numero2

# Mostrar los resultados
print(f"Producto: {producto}")
print(f"Cociente: {cociente}")
print(f"Módulo: {modulo}")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
