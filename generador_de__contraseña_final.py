# --- GENERADOR DE CONTRASEÑAS ---

# Primero, llamamos a la herramienta random que nos ayuda a elegir cosas al azar
import random 

print("=== Generador de contraseñas ===")

# --- PASO 1: Pedir los datos ---
# Aquí usamos un bucle para obligar al programa a pedir el número 
# hasta que el usuario escriba uno que nos sirva (de 4 en adelante).
while True:
    texto = input("¿Cuántos digitios quieres tu contraseña? (Mínimo 4): ")
    try:
        # Convertimos lo que escribió el usuario a un número
        longitud = int(texto)
        
        # Si el número es valido, salimos del bucle y seguimos
        if longitud >= 4:
            break 
        else:
            print("Por favor, escribe un número de 4 o más.")
    except ValueError:
        # Si escribió letras en vez de números, le avisamos
        print("Eso no parece un número, intenta de nuevo.")

# --- PASO 2: Preparar los materiales ---
# Aquí guardamos todo lo que podemos usar para crear la contraseña
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
especiales = "!@#$%&*"
todo = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

# Esta es nuestra "cajita" vacía donde después guardaremos la contraseña
mi_contraseña = ""

# --- PASO 3: Generación de la contraseña ---
# Usamos un bucle 'for' para repetir el proceso tantas veces como la longitud elegida
for i in range(longitud):
    # random.choice elige un carácter al azar de nuestra cadena 'todo'
    caracter = random.choice(todo)
    mi_contraseña += caracter

print(f"Tu nueva contraseña es: {mi_contraseña}")