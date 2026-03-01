
# Función para mostrar reglas
def ver_reglas():
    print(" ----- Reglas del juego ----- ")
    print(" -- piedra gana a tijera")
    print(" -- papel gana a piedra")
    print(" -- tijera gana a papel\n")

# Función para pedir partidas
def pedir_partidas():
    while True:
         # Se utilixo el metodo .sttrrip()
        # ya que me permite borrar espacios en blanco 
        partidas = input("¿Cuántas partidas desea jugar?: ").strip()
        # Metodo isdigit()  verifica si todos los caracteres 
        # de la cadena son dígitos numéricos
        if partidas.isdigit() and int(partidas) > 0:
            return int(partidas)
        else:
            print("Ingrese un número válido.")

# Función para determinar ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate"
    elif usuario == "piedra" and computadora == "tijera":
        return "usuario"
    elif usuario == "papel" and computadora == "piedra":
        return "usuario"
    elif usuario == "tijera" and computadora == "papel":
        return "usuario"
    else:
        return "maquina"
    
#Resultado final Esta función recibe la lista con los resultados
def resultado_final(result_ronda):
    
    # cuenta cuántas veces aparece un valor dentro de la lista.
    usuario_total = result_ronda.count("usuario")
    maquina_total = result_ronda.count("maquina")
    empates_total = result_ronda.count("empate")

    print("\n===== GANADOR DE LA PARTIDA =====")
    # Comparación para decidir ganador general
    if usuario_total > maquina_total:
        print("El USUARIO ganó la partida completa")

    elif maquina_total > usuario_total:
        print("La MÁQUINA ganó la partida completa")

    else:
        print("La partida terminó en EMPATE")
    
    print("Usuario ganó:", result_ronda.count("usuario"))
    print("Máquina ganó:", result_ronda.count("maquina"))
    print("Empates:", result_ronda.count("empate"))
