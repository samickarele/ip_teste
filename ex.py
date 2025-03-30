import pygame
from pygame.locals import *  # * para importar todas funçoes desse submodulo locals
from sys import exit  # quando clicar para fechar janela, ela sera fechada
from random import randint

pygame.init()  # para inicializar todas as funcoes

largura = 640
altura = 480
x = largura / 2
y = altura / 2  # as duas variaveis vao controlar o movimento do objeto e vao se alterar a cada loop
x_azul = randint(40, 600)
y_azul = randint(50, 430)


# tela é a variavel e essa funçao set.mode define a janela
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("projeto ip")

relogio = pygame.time.Clock()  # para definir a taxa de frames

while True:  # loop principal do jogo
    relogio.tick(200)
    # a cada loop a tela é preenchida com a cor preta para dar a percepçao de movimento
    tela.fill((0, 0, 0))
    for event in pygame.event.get():  # detecta se um evento aconteceu
        if event.type == QUIT:  # quando apertar o x é para fechar janela
            pygame.quit()
            exit()

    vel = 5
    keys = pygame.key.get_pressed()

    if keys[K_a]:
        x -= vel

    if keys[K_d]:
        x += vel

    if keys[K_w]:
        y -= vel

    if keys[K_s]:
        y += vel

    # para desenhar objetos na tela, a cor dele, posiçao em relaçao a tela (x e y) e a largura e altura dele
    retan_verde = pygame.draw.rect(tela, (100, 200, 0), (x, y, 40, 50))
    retan_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    # verifica se um triangulo colidiu com o outro
    if retan_verde.colliderect(retan_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)

    # pygame.draw.circle(tela, (90, 20, 90), (300, 260), 40) desenha circulo, posiçao x, y o raio do circulo
    # pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5) desenha linha, ponto que vai iniciar e ponto que vai finalizar

    pygame.display.update()  # para atualizar a tela do jogo a cada loop
