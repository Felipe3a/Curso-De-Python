#---programa que reproduz um aequivo  Mp3

import pygame

# Inicializa o pygame
pygame.init()


# Carrega e reproduz a música
pygame.mixer.music.load('100 Desafios/ex021.mp3')
pygame.mixer.music.play()

# Aguarda a reprodução do áudio
input("Pressione Enter para encerrar...")

pygame.quit()

