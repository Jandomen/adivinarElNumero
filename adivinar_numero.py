import random

def adivinar_numero():
   
    numero_secreto = random.randint(1, 100)
    intentos = 0
    encontrado = False

    print("¡Bienvenido al juego de adivinar el número!")

    while not encontrado:
       
        numero_usuario = int(input("Ingresa un número entre 1 y 100: "))
        intentos += 1

        
        if numero_usuario == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número en {} intentos!".format(intentos))
            encontrado = True
        elif numero_usuario > numero_secreto:
            print("El número es más pequeño. Intenta de nuevo.")
        else:
            print("El número es más grande. Intenta de nuevo.")

    print("Gracias por jugar.")


adivinar_numero()
