

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
FPS = 15 # Frames por segundo

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
            self.speedx = 4
            self.speedy = 4
            self.linha=0
            self.coluna=0
            self.prox_linha=1
            self.prox_col=1
            self.dx=0
            self.dy=0
            
        def update(self):
            
            if Mapa[self.linha][self.prox_col]==0:
                self.rect.x+=self.speedx
                self.rect.y+=0
                self.dx+=self.speedx
                if self.dx>=64:
                    self.coluna=self.prox_col
                    self.prox_col+=1
                    self.dx=0
            elif Mapa[self.prox_linha ][self.coluna]==0:
                self.rect.x+=0
                self.rect.y+=self.speedy
                self.dy+=self.speedy
                if self.dy>=64:
                    self.linha=self.prox_linha
                    self.prox_linha+=1
                    self.dy=0
                    

            
            
               
               

# Classe Jogador que representa a nave
class Torre(pygame.sprite.Sprite):
    
    
    # Construtor da classe.
    def __init__(self,x1,y1):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        torre_img = pygame.image.load(path.join( "torre.png")).convert()
        self.image = torre_img
        self.rect = self.image.get_rect()
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.
        print(Mapa[y1//64])
        print(x1)
        print(y1)
        self.rect.centerx=(x1//64)*64 + 32
        self.rect.centery=(y1//64)*64 + 32
        


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()


Mapa=[[0,0,0,1,2],
      [1,1,0,2,1],
      [2,2,0,0,1],
      [3,2,1,0,1],
      [3,2,2,0,1]]


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
#torre = Torre()
mob=Mob()
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
#all_sprites.add(torre)
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
            if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_1:
                    x=pygame.mouse.get_pos()[0]
                    y=pygame.mouse.get_pos()[1]
                    torre2=Torre(x,y)
                    all_sprites.add(torre2)
                    
                    
                    
                    
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