import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)

# Configurações da tela
largura_tela = 800
altura_tela = 300
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo do Dinossauro")

# Configurações do jogo
velocidade_jogo = 10
gravidade = 1
dinossauro_saltando = False
altura_salto = 15

# Define o relógio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

# Fonte do placar
fonte = pygame.font.SysFont(None, 35)

# Função para mostrar o placar
def exibir_pontuacao(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, [10, 10])

# Classe para o dinossauro
class Dinossauro:
    def __init__(self):
        # Carregar a imagem do dinossauro
        self.imagem = pygame.image.load("dinossauro.png")
        self.imagem = pygame.transform.scale(self.imagem, (60, 60))  # Redimensiona a imagem
        self.rect = self.imagem.get_rect()
        self.rect.x = 50
        self.rect.y = altura_tela - 60
        self.velocidade_y = 0

    def pular(self):
        if self.rect.y == altura_tela - 60:  # Verifica se o dinossauro está no chão
            self.velocidade_y = -altura_salto

    def atualizar(self):
        self.velocidade_y += gravidade
        self.rect.y += self.velocidade_y

        # Evita que o dinossauro caia abaixo do chão
        if self.rect.y >= altura_tela - 60:
            self.rect.y = altura_tela - 60
            self.velocidade_y = 0

        tela.blit(self.imagem, self.rect)

# Classe para os cactos
class Cacto:
    def __init__(self):
        # Carregar a imagem do cacto
        self.imagem = pygame.image.load("cacto.png")
        self.imagem = pygame.transform.scale(self.imagem, (20, 40))  # Redimensiona a imagem
        self.rect = self.imagem.get_rect()
        self.rect.x = largura_tela
        self.rect.y = altura_tela - 60

    def atualizar(self):
        self.rect.x -= velocidade_jogo
        if self.rect.x < -20:  # Se o cacto sair da tela
            self.rect.x = largura_tela + random.randint(100, 300)

        tela.blit(self.imagem, self.rect)

# Função principal do jogo
def jogo():
    fim_de_jogo = False
    pontos = 0

    dinossauro = Dinossauro()
    cacto = Cacto()

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    dinossauro.pular()

        # Atualiza o dinossauro e o cacto
        tela.fill(BRANCO)
        dinossauro.atualizar()
        cacto.atualizar()

        # Verifica colisão
        if dinossauro.rect.colliderect(cacto.rect):
            fim_de_jogo = True

        # Atualiza o placar
        pontos += 1
        exibir_pontuacao(pontos)

        pygame.display.update()
        relogio.tick(30)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
