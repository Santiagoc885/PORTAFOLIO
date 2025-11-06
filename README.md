# Nivel 1 — Fundamentos y Variables
# Objetivo: Practicar tipos de datos, entrada y salida, concatenación y operaciones básicas.

# Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
# Suma de dos números.
# Área del triángulo.
# Conversor de grados Celsius a Fahrenheit.
# Tipo de dato: usar type() para mostrar el tipo de cada variable.
# Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.

import datetime

user = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
print (f"Hola {user}, tienes {age} años")

print("\n-------------------- SUMA DE 2 NUMEROS --------------------")

sum1 = int(input("Ingrese numero 1: "))
sum2 = int(input("Ingrese numero 2: "))
result = sum1 + sum2
print(f"La suma total es: {result}")

print("\n-------------------- AREA DE UN TRIANGULO -----------------")

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
area = (base*altura)/2
print(f"El area del triángulo es: {area}")

print("\n------------ CONVERSOR DE CELCIUS A FAHRENHEIT ------------")

c = float(input("Ingrese los grados celcius: "))
f = (c * 9/5) + 32 
print(f"El resultado es {f}")


# print(type(user))
# print(type(age))
# print(type(c))

print("\n-------------------- EDAD EN 10 AÑOS -------------------")
age_f = int(input("Ingrese su edad actual: "))
future_age = age_f + 10
print(f"Tu edad en 10 años es: {future_age}")
