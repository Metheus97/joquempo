### Projeto para estudo.
### Desenvolver um jogo de joquempo.

# Bibliotecas
import random
import pygame
from pygame.locals import *
from sys import exit

# Abrir janela do jogo
pygame.init()      # Inicializa o pygame

screen_width=700
screen_height=400
tela = screen=pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Super Joquempo')

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (255, 255, 255), (175, 300, 350, 40))


    pygame.display.update()





opcoes = ["Pedra", "Papel", "Tesoura"]   # Lista com as opções do jogo

maquina = random.randint(0, 2)

print(opcoes[maquina])

jogador = int(input("O que você deseja jogar? \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n Sua escolha: "))
jogador = jogador - 1

# Validador Pedra
if jogador == 0:
    if maquina == 0:
        print(f"EMPATE!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
    elif maquina == 1:
        print(f"VOCÊ PERDEU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
    elif maquina == 2:
        print(f"!!VOCÊ GANHOU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")

# Validador Papel
elif jogador == 1:
    if maquina == 1:
        print(f"EMPATE!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
    elif maquina == 2:
        print(f"VOCÊ PERDEU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
    elif maquina == 0:
        print(f"!!VOCÊ GANHOU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")

# Validador Tesoura
elif jogador == 2:
    if maquina == 2:
        print(f"EMPATE!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
    elif maquina == 0:
        print(f"VOCÊ PERDEU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
    elif maquina == 1:
        print(f"!!VOCÊ GANHOU!! \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}")
else:
    print(f'ainda não sei esse resultado \n A maquina fez {opcoes[maquina]} \n Você fez {opcoes[jogador]}')