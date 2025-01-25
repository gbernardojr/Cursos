
# Apostila de Pygame

## Aula 1: Fundamentos do Pygame (3 horas)

### 1. Introdução ao Pygame (30 min)
- O Pygame é uma biblioteca Python para desenvolvimento de jogos 2D.
- **Instalação**: 
  Para instalar o Pygame, utilize o seguinte comando:
  ```
  pip install pygame
  ```

### 2. Conceitos básicos (60 min)

#### Criando uma janela
A estrutura básica de um jogo envolve criar uma janela e gerenciar eventos:

```
import pygame

# Inicializa o Pygame
pygame.init()

# Configura a janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Primeiro Jogo")

# Loop do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

# Encerra o Pygame
pygame.quit()
```

#### Desenhando formas simples
Agora vamos desenhar formas, como retângulos e círculos:

```
import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Preenche a tela com cor
    tela.fill((255, 255, 255))  # Branco

    # Desenha um retângulo vermelho
    pygame.draw.rect(tela, (255, 0, 0), (100, 100, 50, 50))

    # Desenha um círculo azul
    pygame.draw.circle(tela, (0, 0, 255), (400, 300), 75)

    pygame.display.flip()

pygame.quit()
```

### 3. Gráficos e Imagens (45 min)

#### Carregando e exibindo imagens
Carregar e exibir uma imagem:

```
import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

# Carrega a imagem
imagem = pygame.image.load('exemplo.png')

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))
    
    # Desenha a imagem
    tela.blit(imagem, (100, 100))

    pygame.display.flip()

pygame.quit()
```

#### Sprites básicos
Sprites são usados para gerenciar objetos em movimento:

```
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('jogador.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

pygame.init()
tela = pygame.display.set_mode((800, 600))
jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill((255, 255, 255))
    
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

### 4. Animações simples (45 min)

#### Movendo objetos na tela
Aqui adicionamos movimento ao jogador:

```
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('jogador.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    
    def update(self):
        self.rect.x += 5  # Movimento para a direita

pygame.init()
tela = pygame.display.set_mode((800, 600))
jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    todos_sprites.update()
    
    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

#### Animação de sprites
A animação é feita alterando as imagens exibidas:

```
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load(f'frame_{i}.png') for i in range(3)]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    
    def update(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image = self.images[self.current_image]

pygame.init()
tela = pygame.display.set_mode((800, 600))
jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    todos_sprites.update()
    
    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

### Exercício prático: Cena simples com objetos animados (30 min)
Crie uma cena onde um personagem se move continuamente e uma animação simples acontece ao mesmo tempo.

---

## Aula 2: Interatividade e Física Básica (3 horas)

### 1. Interação do usuário (60 min)

#### Capturando eventos de teclado e mouse
Capturando eventos de teclado e reagindo a inputs:

```
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('jogador.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

pygame.init()
tela = pygame.display.set_mode((800, 600))
jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Captura o estado das teclas
    keys = pygame.key.get_pressed()
    todos_sprites.update(keys)
    
    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

### 2. Colisões (60 min)

#### Detecção de colisão básica
Detectar colisões entre dois sprites:

```
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('jogador.png')
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('inimigo.png')
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

pygame.init()
tela = pygame.display.set_mode((800, 600))
jogador = Jogador()
inimigo = Inimigo()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)
todos_sprites.add(inimigo)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador com as setas do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jogador.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        jogador.rect.x += 5
    
    # Verificar colisão entre jogador e inimigo
    if pygame.sprite.collide_rect(jogador, inimigo):
        print("Colisão detectada!")

    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

#### Reagindo a colisões
Após a colisão, podemos reagir mudando a cor ou movendo os objetos:

```
if pygame.sprite.collide_rect(jogador, inimigo):
    print("Colisão detectada!")
    jogador.rect.x = 400  # Reinicia a posição do jogador
```

### 3. Som e Música (30 min)

#### Adicionando efeitos sonoros
Adicionar sons ao jogo, como efeitos de colisão:

```
import pygame

pygame.init()

# Carregar um efeito sonoro
som_colisao = pygame.mixer.Sound('colisao.wav')

# Tocar o som na colisão


if pygame.sprite.collide_rect(jogador, inimigo):
    som_colisao.play()
```

#### Música de fundo
Para adicionar música de fundo:

```
pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1)  # Loop infinito
```

---

## Aula 3: Desenvolvimento de um Jogo de Plataforma Simples (3 horas)

### 1. Mecânica de plataformas (60 min)

#### Gravidade e pulo
Adicionando gravidade e um sistema de pulo básico:

```
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('jogador.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.vel_y = 0  # Velocidade vertical
        self.no_chao = False  # Verificar se está no chão

    def update(self):
        # Aplicar gravidade
        self.vel_y += 0.5  # Gravidade constante
        if self.vel_y > 10:
            self.vel_y = 10  # Limitar a velocidade de queda
        
        # Mover jogador
        self.rect.y += self.vel_y

        # Limitar a movimentação para não atravessar o chão
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
            self.vel_y = 0
            self.no_chao = True

    def pular(self):
        if self.no_chao:
            self.vel_y = -15  # Velocidade para o pulo
            self.no_chao = False

pygame.init()
tela = pygame.display.set_mode((800, 600))
jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.pular()  # O jogador pula ao apertar a barra de espaço

    todos_sprites.update()

    tela.fill((135, 206, 235))  # Cor de fundo (azul claro)
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

### 2. Plataformas e colisões (60 min)

#### Criando plataformas
Adicionando plataformas onde o jogador pode pular e andar:

```
import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill((0, 255, 0))  # Cor verde para a plataforma
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

pygame.init()
tela = pygame.display.set_mode((800, 600))

# Criar plataformas
plataforma1 = Plataforma(100, 400, 300, 20)
plataforma2 = Plataforma(500, 300, 200, 20)

plataformas = pygame.sprite.Group()
plataformas.add(plataforma1, plataforma2)

jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)
todos_sprites.add(plataforma1, plataforma2)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.pular()

    # Aplicar a gravidade e a colisão com as plataformas
    todos_sprites.update()

    # Verificar colisão do jogador com as plataformas
    colisoes = pygame.sprite.spritecollide(jogador, plataformas, False)
    if colisoes:
        jogador.rect.bottom = colisoes[0].rect.top
        jogador.vel_y = 0
        jogador.no_chao = True

    tela.fill((135, 206, 235))  # Fundo azul claro
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

### 3. Criando um inimigo simples (30 min)

#### Inimigos com movimento básico
Adicionando inimigos com movimentação automática que o jogador deve evitar:

```
import pygame

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Vermelho para o inimigo
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.vel_x = 3  # Velocidade de movimento

    def update(self):
        # Movimento do inimigo
        self.rect.x += self.vel_x
        if self.rect.left < 0 or self.rect.right > 800:
            self.vel_x = -self.vel_x  # Mudar a direção ao atingir as bordas

pygame.init()
tela = pygame.display.set_mode((800, 600))

# Criar plataformas e inimigos
plataforma1 = Plataforma(100, 400, 300, 20)
plataforma2 = Plataforma(500, 300, 200, 20)
inimigo = Inimigo(200, 350)

plataformas = pygame.sprite.Group()
plataformas.add(plataforma1, plataforma2)

inimigos = pygame.sprite.Group()
inimigos.add(inimigo)

jogador = Jogador()

todos_sprites = pygame.sprite.Group()
todos_sprites.add(jogador)
todos_sprites.add(plataforma1, plataforma2, inimigo)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jogador.pular()

    todos_sprites.update()

    # Verificar colisão do jogador com as plataformas
    colisoes = pygame.sprite.spritecollide(jogador, plataformas, False)
    if colisoes:
        jogador.rect.bottom = colisoes[0].rect.top
        jogador.vel_y = 0
        jogador.no_chao = True

    # Verificar colisão do jogador com o inimigo
    if pygame.sprite.spritecollide(jogador, inimigos, False):
        print("Você foi atingido!")

    tela.fill((135, 206, 235))  # Fundo azul claro
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

### 4. Refinamentos finais e ajustes (30 min)

#### Pontuação e Game Over
Adicionando um sistema de pontuação e tela de Game Over:

```
import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

# Variáveis de jogo
pontos = 0
game_over = False

# Fontes
fonte = pygame.font.Font(None, 36)

# Jogador, plataformas, inimigos...

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN and not game_over:
            if evento.key == pygame.K_SPACE:
                jogador.pular()

    if not game_over:
        todos_sprites.update()
        
        # Lógica de jogo
        # Colisão com inimigos
        if pygame.sprite.spritecollide(jogador, inimigos, False):
            game_over = True
        
        # Atualizar a pontuação
        pontos += 1

    # Desenhar tudo na tela
    tela.fill((135, 206, 235))  # Fundo azul claro
    todos_sprites.draw(tela)
    
    # Exibir a pontuação
    texto_pontos = fonte.render(f'Pontos: {pontos}', True, (0, 0, 0))
    tela.blit(texto_pontos, (10, 10))
    
    # Exibir mensagem de game over
    if game_over:
        texto_game_over = fonte.render('Game Over', True, (255, 0, 0))
        tela.blit(texto_game_over, (350, 300))

    pygame.display.flip()

pygame.quit()
```

---

## Conclusão

Ao longo das três aulas, você aprendeu os fundamentos do Pygame, incluindo como criar janelas, desenhar formas e sprites, lidar com eventos, colisões e adicionar interatividade. Além disso, construímos um jogo de plataforma simples que pode ser expandido com mais funcionalidades, como níveis, inimigos adicionais, power-ups e muito mais. Continue praticando e explorando os recursos do Pygame para criar jogos mais complexos e divertidos!
```
