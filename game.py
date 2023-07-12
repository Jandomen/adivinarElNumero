import random

def guess_number():
    secret_number = random.randint(1, 100) 
    attempts = 0
    
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100. ¿Puedes adivinar cuál es?")
    
    while True:
        guess = int(input("Ingresa tu número: "))
        attempts += 1

        if guess < secret_number:
            print("Demasiado bajo. Intenta de nuevo.")
        elif guess > secret_number:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")
            break

guess_number()
