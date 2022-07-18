### Projeto para estudo.
### Desenvolver um jogo de joquempo.

# Bibliotecas
import random

opcoes = ["Pedra", "Papel", "Tesoura"]   # Lista com as opções do jogo

maquina = random.randint(0, 2)

print(opcoes[maquina])

jogador = int(input("O que você deseja jogar? \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n Sua escolha: "))
jogador = jogador - 1

# Validador Pedra
if jogador == 0:
    if maquina == 0:
        print(f"EMPATE!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
    elif maquina == 1:
        print(f"VOCÊ PERDEU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
    elif maquina == 2:
        print(f"!!VOCÊ GANHOU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")

# Validador Papel
if jogador == 1:
    if maquina == 1:
        print(f"EMPATE!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
    elif maquina == 2:
        print(f"VOCÊ PERDEU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
    elif maquina == 0:
        print(f"!!VOCÊ GANHOU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")

# Validador Tesoura
if jogador == 2:
    if maquina == 2:
        print(f"EMPATE!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
    elif maquina == 0:
        print(f"VOCÊ PERDEU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
    elif maquina == 1:
        print(f"!!VOCÊ GANHOU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}")
else:
    print(f'ainda não sei esse resultado \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador-1]}')