# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
WIDTH = 160 # Largura da tela
HEIGHT = 160 # Altura da tela
FPS = 60 # Frames por segundo

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
        self.rect.x=coluna*32
        self.rect.y=linha*32
        
        

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
        self.image = pygame.transform.scale(player_img, (50, 38))
        
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
      [2,2,1,0,1],
      [3,2,1,0,1],
      [3,3,1,0,0]]


# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
agua = pygame.transform.scale(pygame.image.load("agua.png"), [32,32])
chao = pygame.transform.scale(pygame.image.load("chao.png"), [32,32])
percurso = pygame.transform.scale(pygame.image.load("percurso.png"), [32,32])

Terrenos={
        0:percurso,
        1:chao,
        2:agua ,
        3:pygame.image.load(path.join( "flor.png")).convert()
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

# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
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
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        tiles.draw(screen)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
