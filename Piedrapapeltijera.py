
import random
import time

while True:
    
    aleatorio = random.randrange(0,6)
    maquina = ""
    print("A continuación te indico los elementos aceptados")
    time.sleep(0.5)
    print("1.Piedra")
    time.sleep(0.1)
    print("2.Papel")
    time.sleep(0.1)
    print("3.Tijeras")
    time.sleep(0.1)
    print("4.Lagarto")
    time.sleep(0.1)
    print("5.Spock")
    time.sleep(0.1)
    opcion = int(input("Elije tu opción"))


###TIRADAS###
    if opcion == 1:
        usuario = "Piedra"
    elif opcion == 2:
        usuario = "Papel"
    elif opcion == 3:
        usuario ="Tijeras"
    elif opcion == 4:
        usuario ="Lagarto"
    elif opcion == 6:
        usuario ="Spock"
    print("Has elegido: ", usuario)
    time.sleep(0.5)

    if aleatorio == 1:
        maquina = "Piedra"
    elif aleatorio == 2:
        maquina = "Papel"
    elif aleatorio == 3:
        maquina ="Tijeras"
    elif aleatorio == 4:
        maquina ="Lagarto"
    elif aleatorio == 6:
        maquina ="Spock"
    print("La máquina ha elegido: ", maquina)
    time.sleep(1)
    print("...")


    ###LOGICA PARTIDA###

    if usuario == "Tijeras" and maquina == "Papel":
        print("Gana usuario, tijeras cortan a papel")
    elif usuario == "Papel" and maquina == "Piedra":
        print("Gana usuario, Papel tapa a piedra")
    elif usuario == "Piedra" and maquina == "Lagarto":
        print("Gana usuario, Piedra aplasta a lagarto")
    elif usuario == "Lagarto" and maquina == "Spock":
        print("Gana usuario, Lagarto envenena a spock")
    elif usuario == "Spock" and maquina == "Tijeras":
        print("Gana usuario, Spock rompe tijeras")
    elif usuario == "Tijeras" and maquina == "Lagarto":
        print("Gana usuario, Tijeras decapitan a lagarto")
    elif usuario == "Lagarto" and maquina == "Papel":
        print("Gana usuario, Lagarto devora papel")
    elif usuario == "Papel" and maquina == "Spock":
        print("Gana usuario, Papel desautoriza Spock")
    elif usuario == "Spock" and maquina == "Piedra":
        print("Gana usuario, Spock vaporiza piedra")
    elif usuario == "Piedra" and maquina == "Tijeras":
        print("Gana usuario, Piedra aplasta a tijeras")

    elif maquina == "Tijeras" and usuario == "Papel":
        print("Gana maquina, tijeras cortan a papel")
    elif maquina == "Papel" and usuario == "Piedra":
        print("Gana maquina, Papel tapa a piedra")
    elif maquina == "Piedra" and usuario == "Lagarto":
        print("Gana maquina, Piedra aplasta a lagarto")
    elif maquina == "Lagarto" and usuario == "Spock":
        print("Gana maquina, Lagarto envenena a spock")
    elif maquina == "Spock" and usuario == "Tijeras":
        print("Gana maquina, Spock rompe tijeras")
    elif maquina == "Tijeras" and usuario == "Lagarto":
        print("Gana maquina, Tijeras decapitan a lagarto")
    elif maquina == "Lagarto" and usuario == "Papel":
        print("Gana maquina, Lagarto devora papel")
    elif maquina == "Papel" and usuario == "Spock":
        print("Gana maquina, Papel desautoriza Spock")
    elif maquina == "Spock" and usuario == "Piedra":
        print("Gana maquina, Spock vaporiza piedra")
    elif maquina == "Piedra" and usuario == "Tijeras":
        print("Gana maquina, Piedra aplasta a tijeras")
    elif maquina == usuario:
        print("empate")
    
    repetirJuego = input("¿Quieres jugar de nuevo? (s/n)")
    if repetirJuego.lower()!="s":
        time.sleep(0.5)
        print("JUEGO TERMINADO")
        break