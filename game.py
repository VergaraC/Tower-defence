# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import random
import time
# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')


# Dados gerais do jogo.
WIDTH = 320 # Largura da tela
HEIGHT = 320 # Altura da tela
FPS = 10 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)




          
class Terreno(pygame.sprite.Sprite):
    def __init__(self,tipo,linha,coluna):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = Terrenos[tipo].copy()
        self.rect = self.image.get_rect()
        self.rect.x=coluna*64
        self.rect.y=linha*64
        
        
class Mob(pygame.sprite.Sprite):
    
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            # Detalhes sobre o posicionamento.
            self.image = pygame.image.load("Mob.png").convert()
            
            self.rect = self.image.get_rect()
            
            # Sorteia um lugar inicial em x
            self.rect.x = 16
            # Sorteia um lugar inicial em y
            self.rect.y = 16
            # Sorteia uma velocidade inicial
            self.speedx = 5
            self.speedy = 1
            
        def update(self):
           self.rect.x += self.speedx
           self.rect.y =0
        

# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join( "chao.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (1, 1))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()


Mapa=[[0,0,0,1,3],
      [1,1,0,0,1],
      [2,1,2,0,1],
      [3,2,1,0,1],
      [3,3,2,0,0]]


# Tamanho da tela.
imgX=64
imgY=64

screen = pygame.display.set_mode((WIDTH, HEIGHT))
agua = pygame.transform.scale(pygame.image.load("agua.png"), [imgX,imgY])
chao = pygame.transform.scale(pygame.image.load("chao.png"), [imgX,imgY])
percurso = pygame.transform.scale(pygame.image.load("percurso.png"), [imgX,imgY])
flor= pygame.transform.scale(pygame.image.load("flor.png"), [imgX,imgY])

Terrenos={
        0:percurso,
        1:chao,
        2:agua ,
        3:flor
        }


# Nome do jogo
pygame.display.set_caption("Tower Defense")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background=pygame.image.load(path.join( 'agua.png')).convert()
background_rect = background.get_rect()


# Cria uma nave. O construtor será chamado automaticamente.
player = Player()
mob=Mob()
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(mob)

tiles=pygame.sprite.Group()
for linha in range(len(Mapa)):
    for coluna in range(len(Mapa[linha])):
        terreno=Terreno(Mapa[linha][coluna],linha,coluna)
        tiles.add(terreno)

        

# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        tiles.draw(screen)
        all_sprites.draw(screen)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
