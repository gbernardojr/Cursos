import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Define as dimensões da tela
largura_tela = 600
altura_tela = 400

# Tamanho do bloco da cobra
tamanho_bloco = 20

# Definindo a velocidade da cobra
velocidade = 15

# Configura a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Define o relógio para controlar a velocidade do jogo
relogio = pygame.time.Clock()

# Função para desenhar a cobra
def desenha_cobra(tamanho_bloco, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, VERDE, [x[0], x[1], tamanho_bloco, tamanho_bloco])

# Função principal do jogo
def jogo():
    fim_de_jogo = False
    jogo_encerrado = False

    # Posição inicial da cobra
    x = largura_tela // 2
    y = altura_tela // 2

    # Movimento inicial da cobra
    movimento_x = 0
    movimento_y = 0

    # Lista que armazena as coordenadas do corpo da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Gera a maçã em uma posição aleatória
    maca_x = round(random.randrange(0, largura_tela - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    maca_y = round(random.randrange(0, altura_tela - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

    while not fim_de_jogo:

        while jogo_encerrado:
            tela.fill(PRETO)
            fonte = pygame.font.SysFont(None, 50)
            mensagem = fonte.render("Fim de Jogo! Pressione C para continuar ou Q para sair", True, BRANCO)
            tela.blit(mensagem, [largura_tela / 6, altura_tela / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_de_jogo = True
                        jogo_encerrado = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimento_x = -tamanho_bloco
                    movimento_y = 0
                elif evento.key == pygame.K_RIGHT:
                    movimento_x = tamanho_bloco
                    movimento_y = 0
                elif evento.key == pygame.K_UP:
                    movimento_x = 0
                    movimento_y = -tamanho_bloco
                elif evento.key == pygame.K_DOWN:
                    movimento_x = 0
                    movimento_y = tamanho_bloco

        # Atualiza a posição da cobra
        x += movimento_x
        y += movimento_y

        # Verifica se a cobra colidiu com as bordas
        if x >= largura_tela or x < 0 or y >= altura_tela or y < 0:
            jogo_encerrado = True

        # Preenche a tela com a cor preta
        tela.fill(PRETO)

        # Desenha a maçã
        pygame.draw.rect(tela, VERMELHO, [maca_x, maca_y, tamanho_bloco, tamanho_bloco])

        # Atualiza a posição da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        # Verifica se a cobra colidiu com o próprio corpo
        for parte in lista_cobra[:-1]:
            if parte == cabeca_cobra:
                jogo_encerrado = True

        desenha_cobra(tamanho_bloco, lista_cobra)
        pygame.display.update()

        # Verifica se a cobra comeu a maçã
        if x == maca_x and y == maca_y:
            maca_x = round(random.randrange(0, largura_tela - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            maca_y = round(random.randrange(0, altura_tela - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comprimento_cobra += 1

        # Controla a velocidade do jogo
        relogio.tick(velocidade)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
