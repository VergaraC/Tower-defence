




# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import math
import time


# Dados gerais do jogo.
WIDTH = 960 # Largura da tela
HEIGHT = 640 # Altura da tela
FPS = 150 # Frames por segundo

VIDA=10

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
            self.image= pygame.transform.scale(pygame.image.load("sharingan.png"), [64,48])
            self.image.set_colorkey(WHITE)
            
            self.rect = self.image.get_rect()
            #self.image.set_colorkey(BLACK)
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
            self.linha_anterior=0
            self.coluna_anterior=0
            
        def update(self):
            
            
                   
           if self.linha<len(Mapa) and self.prox_col<len(Mapa[self.linha]) and Mapa[self.linha][self.prox_col]==0 and self.prox_col!=self.coluna_anterior:
               self.rect.x+=self.speedx
               self.rect.y+=0
               self.dx+=self.speedx
               if self.dx>=64:
                   self.linha_anterior=self.linha
                   self.coluna_anterior=self.coluna
                   self.coluna=self.prox_col
                   self.prox_col+=1
                   self.dx=0
           elif self.prox_linha<len(Mapa) and self.coluna<len(Mapa) and Mapa[self.prox_linha ][self.coluna]==0 and self.prox_linha!=self.linha_anterior:
               self.rect.x+=0
               self.rect.y+=self.speedy
               self.dy+=self.speedy
               if self.dy>=64:
                   self.linha_anterior=self.linha
                   self.coluna_anterior=self.coluna
                   self.linha=self.prox_linha
                   self.prox_linha+=1

                   self.dy=0
           elif self.linha<len(Mapa) and (self.coluna-1)<len(Mapa[self.linha]) and Mapa[self.linha][self.coluna-1]==0 and (self.coluna-1)!=self.coluna_anterior:
               self.rect.x-=self.speedx
               self.rect.y+=0
               self.dx+=self.speedx
               if self.dx>=64:
                   self.linha_anterior=self.linha
                   self.coluna_anterior=self.coluna
                   self.coluna=self.coluna-1
                   self.prox_col-=1
                   self.dx=0
                   
           elif (self.linha-1)<len(Mapa) and (self.coluna)<len(Mapa[self.linha-1]) and Mapa[self.linha-1][self.coluna]==0 and (self.linha-1)!=self.linha_anterior:
               self.rect.x+=0
               self.rect.y-=self.speedy
               self.dy+=self.speedy
               if self.dy>=64:
                   self.linha_anterior=self.linha
                   self.coluna_anterior=self.coluna
                   self.linha=self.linha-1
                   self.prox_linha-=1
                   self.dy=0
                   
               

# Classe Jogador que representa a nave
class Torre(pygame.sprite.Sprite):
    
    
    # Construtor da classe.
    def __init__(self,x1,y1,all_sprites,bullets):
        self.all_sprites= all_sprites
        self.bullets=bullets
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        torre_img = pygame.transform.scale(pygame.image.load("naruto.png"), [64,64])
        self.image = torre_img
        self.rect = self.image.get_rect()
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.

        self.rect.centerx=(x1//64)*64 + 32
        self.rect.centery=(y1//64)*64 + 32
        
        self.alvo=None
        self.d=None
        
        self.V=5
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 750
        
    def update(self):
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks and self.alvo != None:
            
            # Marca o tick da nova imagem.
            self.last_update = now
            bullet=Bullet(self.rect.centerx,self.rect.centery)
         
            bullet.speedx= - self.V*self.dx/self.d
            bullet.speedy= - self.V*self.dy/self.d
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)
           

class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,x,y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        bullet_img = pygame.transform.scale(pygame.image.load("rasengan.png"), [58,58])
        self.image = bullet_img
        
        # Deixando transparente.
        self.rect = self.image.get_rect()
        
        self.image.set_colorkey(BLACK)
        # Detalhes sobre o posicionamento.
        self.rect.centerx=x
        self.rect.centery=y
        self.speedyx=0
        self.speedy=0
        
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        
    
    
# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()


Mapa=[[0,0,1,0,0,0,0,2,2,0,0,0,0,0,0],
      [1,0,2,0,1,2,0,2,2,0,1,1,1,4,4],
      [0,0,2,0,0,2,0,2,2,0,0,0,0,4,4],
      [0,2,2,2,0,2,0,2,2,2,1,1,0,4,4],
      [0,0,2,0,0,2,0,2,0,0,0,0,0,4,4],
      [1,0,2,0,2,2,0,4,0,4,2,1,2,4,4],
      [1,0,2,0,2,0,0,4,0,4,2,1,1,4,4],
      [1,0,0,0,2,0,4,0,0,4,2,1,1,4,4],
      [1,1,1,2,2,0,4,0,1,4,2,1,2,4,4],
      [1,1,1,1,1,0,0,0,1,4,2,2,2,4,4]]


YY=len(Mapa)
XX=len(Mapa[0])

# Tamanho da tela.
imgX=64
imgY=64

screen = pygame.display.set_mode((WIDTH, HEIGHT))
agua = pygame.transform.scale(pygame.image.load("water.png"), [ imgX,imgY])
chao = pygame.transform.scale(pygame.image.load("grass.png"), [imgX,imgY])
percurso = pygame.transform.scale(pygame.image.load("floor.png"), [imgX,imgY])
percurso2 = pygame.transform.scale(pygame.image.load("percurso.png"), [imgX,imgY])
flor= pygame.transform.scale(pygame.image.load("flor.png"), [imgX,imgY])
casa= pygame.transform.scale(pygame.image.load("wall.png"), [imgX,imgY])

Terrenos={
        0:percurso,
        1:chao,
        2:agua ,
        3:flor,
        4:casa,
        5:percurso2
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
mobg=pygame.sprite.Group()
mobg.add(mob)
# Cria um grupo de sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
bullets= pygame.sprite.Group()
torre2=[]
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
    last_update2 = pygame.time.get_ticks()
    last_update_torre = pygame.time.get_ticks()
    last_update_VIDA = pygame.time.get_ticks()
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        now_VIDA = pygame.time.get_ticks()
        if mob.rect.x>900 and mob.rect.y<64 and now_VIDA - last_update_VIDA >=1000 :
            VIDA-=1
            if VIDA==0:
                running=False
                
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                now_torre = pygame.time.get_ticks()
                if event.key == pygame.K_1  and now_torre - last_update_torre >= 2500 or torre2==[]:
                    x=pygame.mouse.get_pos()[0]
                    y=pygame.mouse.get_pos()[1]
                    torre1=Torre(x,y,all_sprites,bullets)
                    torre2.append(torre1)
                    all_sprites.add(torre1)
                    last_update_torre= now_torre
            
            if pygame.mouse.get_pressed()[0]:
                x_tiro=pygame.mouse.get_pos()[0]
                y_tiro=pygame.mouse.get_pos()[1]
            
                for torre in torre2:
                    torre.alvo=[x_tiro,y_tiro]
                    torre.d=math.sqrt(torre.alvo[0]*2 + torre.alvo[1]*2)
                    torre.dx= torre.rect.centerx - torre.alvo[0]
                    torre.dy= torre.rect.centery - torre.alvo[1]
        #Morte e Respawn
        all_sprites.update()

        mob.image= pygame.transform.scale(pygame.image.load("sharingan.png"), [64,48])
        mob.image.set_colorkey(WHITE)
        hits = pygame.sprite.groupcollide(mobg, bullets, True, True)
        for hit in hits:
            mob2=Mob()
            all_sprites.add(mob2)
            mobg.add(mob2)
        
        #Spawn constante
        now2 = pygame.time.get_ticks()
            
        if   now2 - last_update2 > 500:
            mob2=Mob()
            all_sprites.add(mob2)
            mobg.add(mob2)
            last_update2=now2
                
                
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        tiles.draw(screen)
        all_sprites.draw(screen)
        
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()

