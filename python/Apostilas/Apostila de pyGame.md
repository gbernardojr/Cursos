# Apostila de Pygame

## Aula 1: Fundamentos do Pygame (3 horas)

### 1 Introdução ao Pygame (30 min)
- O Pygame é uma biblioteca Python para desenvolvimento de jogos 2D.
- **Instalação**: 
  Para instalar o Pygame, utilize o seguinte comando:
  ```bash
  pip install pygame
  ```

### 2. Conceitos básicos (60 min)
#### Criando uma janela
A estrutura básica de um jogo envolve criar uma janela e gerenciar eventos:

```python
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

```python
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

Carregar e exibir uma imagem é simples:

```python
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
Sprites são usados para gerenciar objetos em movimento. Um sprite básico:

```python
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

```python
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

```python
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

```python
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

```python
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

```python
if pygame.sprite.collide_rect(jogador, inimigo):
    print("Colisão detectada!")
    jogador.rect.x = 400  # Reinicia a posição do jogador
```

### 3. Som e Música (30 min)
#### Adicionando efeitos sonoros
Adicionar sons ao jogo, como efeitos de colisão:

```python
import pygame

pygame.init()

# Carregar um efeito sonoro
som_colisao = pygame.mixer.Sound('colisao.wav')

# Tocar o som na colisão
if pygame.sprite.collide_rect(jogador, inimigo):
    som_colisao.play()
```

#### Incluindo música de fundo
Adicione música de fundo que toca em loop:

```python
# Carregar a música de fundo
pygame.mixer.music.load('musica_fundo.mp3')

# Tocar a música indefinidamente
pygame.mixer.music.play(-1)  # O -1 significa loop infinito
```

### 4. Texto e Fontes (30 min)
#### Renderizando texto na tela
Exibir texto na tela é simples com o Pygame:

```python
import pygame

pygame.init()
tela = pygame.display.set_mode((800, 600))

# Configurar fonte
fonte = pygame.font.SysFont('Arial', 36)
texto = fonte.render('Pygame Tutorial', True, (0, 0, 0))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    tela.fill((255, 255, 255))
    
    # Renderizar o texto
    tela.blit(texto, (100, 100))

    pygame.display.flip()

pygame.quit()
```

#### Usando diferentes fontes
Para carregar uma fonte personalizada:

```python
fonte_personalizada = pygame.font.Font('minha_fonte.ttf', 36)
texto = fonte_personalizada.render('Fonte personalizada!', True, (0, 0, 0))
```

### Projeto prático: Criar um jogo Pong simples (60 min)
Aqui, você guiará os alunos para criar um Pong simples, implementando:
- Movimento das raquetes com as teclas.
- Bola se movendo e rebater nas bordas da tela.
- Detecção de colisão entre bola e raquetes.
  
---

## Aula 3: Desenvolvimento de Jogo e Conclusão (3 horas)

### 1. Revisão rápida e esclarecimento de dúvidas (30 min)

Revisão dos principais conceitos aprendidos até aqui: janelas, sprites, eventos, colisões, som, etc.

### 2. Projeto Final: Jogo de Plataforma Simples (120 min)
Neste projeto, os alunos desenvolverão um jogo de plataforma básico.

#### Planejamento do jogo
- **Objetivo**: Criar um jogo onde o personagem principal salta entre plataformas, evitando obstáculos e coletando itens.
  
#### Implementação do personagem principal
```python
import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('personagem.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400)
        self.velocidade_y = 0

    def pular(self):
        self.velocidade_y = -15

    def gravidade(self):
        self.velocidade_y += 1
        if self.velocidade_y > 10:
            self.velocidade_y = 10

    def update(self):
        self.gravidade()
        self.rect.y += self.velocidade_y

        # Limita o movimento no solo
        if self.rect.bottom > 500:
            self.rect.bottom = 500
            self.velocidade_y = 0

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
                jogador.pular()
    
    todos_sprites.update()
    
    tela.fill((255, 255, 255))
    todos_sprites.draw(tela)
    pygame.display.flip()

pygame.quit()
```

#### Criação de níveis básicos
- Implementar plataformas que o jogador pode saltar entre elas.

```python
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, largura, altura, x, y):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill((0, 255, 0))  # Cor verde
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
```

#### Adição de obstáculos e coletáveis
- Criar obstáculos e itens que o jogador deve evitar ou coletar para ganhar pontos.

#### Implementação de um sistema de pontuação
- Exibir a pontuação na tela à medida que o jogador coleta itens.

### 3. Recursos adicionais e próximos passos (30 min)
- Comunidades e fóruns para continuar aprendendo.
- Sugestões de projetos para os alunos continuarem praticando.

---
