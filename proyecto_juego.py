import random
while True:
    print("----------BIENVENIDO  AL JUEGO PIEDRA, PAPEL  Y TIJERA---------------")
    print("1. Jugar")
    print("2. Mostrar reglas")
    print("3. Salir")

    menu = input("Elija una de las opciones: ")

    if menu == "1":
        print("-----------------------------------------------------")
        opciones = ["piedra", "papel", "tijera"]
        # pedir el numero de partidas
        while True:
            partidas = input(" -----Cuantas partidas desea jugar ?-----: ").strip()
            #metodo isdigit()  verifica si todos los caracteres de la cadena son dígitos numéricos
            if partidas.isdigit() and int(partidas) > 0:
                partidas = int(partidas)
                break
            else:
                print("Ingrese un número válido.")
        # ciclo de partidas
        for ronda in range(1, partidas + 1):
            print(f"\n--- Partida {ronda} ---")

            # pedir jugada válida
            while True:
                usuario = input("Elige piedra, papel o tijera: ").lower().strip()
                if usuario in opciones:
                    break
                else:
                    print("Opción incorrecta")

            computadora = random.choice(opciones)

            print("Usuario eligió:", usuario)
            print("Máquina eligió:", computadora)
            # Lógica del juego
            if  usuario == computadora:
                print("Es un empate")
            elif usuario == "piedra" and computadora == "tijera":
                print("El usuario gana")
            elif usuario == "papel" and computadora == "piedra":
                print("El usuario gana")
            elif usuario == "tijera" and computadora == "papel":
                 print("El usuario gana")
            else:
                print("La maquina gana")

    elif menu == "2":
        print(" ----- Reglas del juego ----- ")
        print(" -- piedra gana a tijera")
        print(" -- papel gana a piedra")
        print(" -- tijera gana a papel\n")

    elif menu == "3":
         print(f"\n--- SALIO DEL JUEGO GRACIAS!! POR JUGAR ---")
         break

    else:
        print("Opción inválida, escoja una opción correcta")

