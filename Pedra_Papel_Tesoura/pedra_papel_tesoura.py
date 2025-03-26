import random

opcaos = ["pedra", "papel", "tesoura"]

def menu():
    print("Jogo de Pedra Papel e Tesoura")
    print("- Pedra")
    print("- Papel")
    print("- Tesoura")
    opcao = str(input("Escreva sua opção: "))
    return opcao

def vencedor(opcao_maquina, opcao_jogador):
    opcao_jogador = tratamento_str(opcao_jogador)
    opcao_jogador = opcaos.index(opcao_jogador) + 1

    print(f"Jogador escolheu {opcaos[opcao_jogador - 1].capitalize()}")
    print(f"Maquina escolheu {opcaos[opcao_maquina - 1].capitalize()}")
    print("Resultado:", end=" ")

    if opcao_maquina == 1: 
        if opcao_jogador == 1:
            print("Empate")
        elif opcao_jogador == 2: 
            print("Jogador venceu")
        elif opcao_jogador == 3: 
            print("Maquina venceu")

    elif opcao_maquina == 2: 
        if opcao_jogador == 1: 
            print("Maquina venceu")
        elif opcao_jogador == 2: 
            print("Empate")
        elif opcao_jogador == 3: 
            print("Jogador venceu")

    elif opcao_maquina == 3: 
        if opcao_jogador == 1:
            print("Jogador venceu")
        elif opcao_jogador == 2:
            print("Maquina venceu")
        elif opcao_jogador == 3:
            print("Empate")


def tratamento_str(string):
    return string.lower().strip()



opcao_jogador = menu()
opcao_maquina = random.randint(1, 3)
vencedor(opcao_maquina, opcao_jogador)    