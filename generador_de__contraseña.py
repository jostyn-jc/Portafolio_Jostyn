# --- AVANCE: GENERADOR DE CONTRASEÑAS ---

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

# NOTA:
# Hasta aquí el programa ya sabe el tamaño y qué letras podemos usar.
# En la siguiente parte del proyecto, vamos a rellenar la caja y a verificar que sí tenga al menos una mayúscula y un símbolo.
print("¡Listo! El programa ya sabe qué hacer.")
# Use esta ultima linea para que verifique no existe algun error y el programa finalice todo el proceso