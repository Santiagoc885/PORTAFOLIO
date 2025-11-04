# 2. Entrada de datos (variables en Python):
# Crea un archivo inventario.py.
# Declara variables para nombre (string), precio (float) y cantidad (int).
# Solicita al usuario estos datos con la función input().
# Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
# Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.



while True:
    #solicitar datos al usuario - strip: elimina espacios en blanco
    product_name = input("Enter the name: ").strip()
    if product_name:
        break
    else:
        print("Error: the name can not be empty.")


while True:
    try:
        price = float(input("Enter the price: "))
        if price >= 0:
            break
        else:
            print("Error: the price can not be negative.")
    except ValueError:
        print("Error: You must enter a valid number for the price.")

while True:
    try:
        amount = int(input("Enter the amount: "))
        if amount >= 0:
            break
        else:
            print("Error: the amount must be greater than 0.")
    except ValueError:
        print("Error: You must enter a valid integer. ")

print("\n✅ Data entered correctly:")
print(f"Name: {product_name}")
print(f"Price: {price}")
print(f"Amount: {amount}")


# 3. Operación matemática (costo total):
# Crea una variable llamada costo_total.
# Almacena en ella el resultado de multiplicar el precio por la cantidad (precio * cantidad).
# Asegúrate de que la operación se realice después de validar los datos de entrada.

total_cost = price * amount

print(f"\nProduct: {product_name} | Price: {price} | Amount: {amount} | The total cost was: ", total_cost)



#This program calcutates the cost 