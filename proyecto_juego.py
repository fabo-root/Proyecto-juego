# La biblioteca random pe permite realizar operaciones alteatorias
import random
import  funciones_juego 
# Mantiene activo el menu 
while True:
    print("----------BIENVENIDO  AL JUEGO PIEDRA, PAPEL  Y TIJERA---------------")
    print("1. Jugar")
    print("2. Mostrar reglas")
    print("3. Salir")

    menu = input("Elija una de las opciones: ")

    if menu == "1":
        result_ronda = []
        print("-----------------------------------------------------")

        #tupla no ccambia los datos
        opciones = ("piedra", "papel", "tijera")

        # Pedimos partidas usando la función
        partidas = funciones_juego.pedir_partidas()
       
        # ciclo de partidas
        # La funcion range repite el juego el numero de veces que elijio el usuario
        for ronda in range(1, partidas + 1):
            print(f"\n--- Partida {ronda} ---")

            # Valida piedra, papel, tijera 
            while True:
                # el metodo .lower() convierte las cadenas string mayusculas a minusulas
                usuario = input("Elige piedra, papel o tijera: ").lower().strip()
                if usuario in opciones:
                    break
                else:
                    print("Opción incorrecta")

            # seleccionar un elemento aleatorio de la lista
            computadora = random.choice(opciones)

            print("Usuario eligió:", usuario)
            print("Máquina eligió:", computadora)

            # Lógica del juego
            # Se llama la función determinar_ganador()
            # que devuelve quién ganó la ronda.
            # Ese resultado se guarda en la lista result_ronda.
            resultado = funciones_juego.determinar_ganador(usuario, computadora)
            # Se agrega el resultado a la lista
            result_ronda.append(resultado)

            # Al terminar todas las rondas,
            # se envía la lista completa a la función resultado_final
            # para analizar quién ganó la partida completa.
        funciones_juego.resultado_final(result_ronda)

    elif menu == "2":
       funciones_juego.ver_reglas()

    elif menu == "3":
         print(f"\n--- SALIO DEL JUEGO GRACIAS!! POR JUGAR ---")
         break

    else:
        print("Opción inválida, escoja una opción correcta")

