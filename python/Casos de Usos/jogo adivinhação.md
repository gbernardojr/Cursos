# Caso de Uso: Jogo de Adivinhação - "Mais ou Menos"

## Descrição do Sistema:
Desenvolver um jogo em console onde o programa sorteia um número aleatório e o jogador deve adivinhá-lo dentro de 10 tentativas.

## Requisitos Funcionais:

**RF01 - Inicialização do Jogo**
- O sistema deve gerar um número aleatório entre 1 e 100
- O sistema deve informar ao usuário que o jogo começou

**RF02 - Entrada do Usuário**
- O sistema deve aceitar apenas números inteiros como entrada
- O sistema deve validar se a entrada é um número válido

**RF03 - Feedback das Tentativas**
- Se o palpite for **MAIOR** que o número secreto → mostrar "MENOS"
- Se o palpite for **MENOR** que o número secreto → mostrar "MAIS"
- Se o palpite for **IGUAL** ao número secreto → encerrar jogo

**RF04 - Controle de Tentativas**
- O usuário tem exatamente 10 tentativas
- O sistema deve mostrar o número de tentativas restantes

**RF05 - Finalização do Jogo**
- Se acertar dentro de 10 tentativas → mostrar "GANHOU"
- Se esgotar as tentativas → mostrar "PERDEU" e revelar o número

## Regras de Negócio:

**RN01:** Número secreto deve estar entre 1 e 100
**RN02:** Cada palpite conta como uma tentativa, mesmo se inválido
**RN03:** O jogo encerra imediatamente ao acertar o número
**RN04:** Mensagens devem ser em CAIXA ALTA conforme especificado

## Fluxo Esperado:

```
=== JOGO DE ADIVINHAÇÃO ===
Tente adivinhar o número entre 1 e 100
Você tem 10 tentativas!

Tentativa 1/10: 50
MAIS

Tentativa 2/10: 75
MENOS

Tentativa 3/10: 63
MAIS

...

Tentativa 6/10: 69
GANHOU!
```

**OU**

```
...

Tentativa 10/10: 45
PERDEU! O número era 42
```

## Critérios de Aceitação:

- [ ] Gera número aleatório entre 1-100
- [ ] Aceita apenas números inteiros
- [ ] Mostra "MAIS" para palpites menores
- [ ] Mostra "MENOS" para palpites maiores  
- [ ] Limita a 10 tentativas
- [ ] Mostra "GANHOU" ao acertar
- [ ] Mostra "PERDEU" ao esgotar tentativas
- [ ] Informa número secreto ao perder

## Template de Código para Implementação:

```python
import random


# Gerar número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas_maximas = 10
tentativas = 0
    
print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente adivinhar o número entre 1 e 100")
print(f"Você tem {tentativas_maximas} tentativas!\n")
    
# TODO: Implementar o loop principal do jogo
# TODO: Receber input do usuário
# TODO: Implementar a lógica de "MAIS" e "MENOS"
# TODO: Controlar as tentativas
# TODO: Verificar vitória/derrota



Este caso de uso é perfeito para alunos praticarem:
- **Loops** (while/for)
- **Condicionais** (if/elif/else) 
- **Input/Output**
- **Lógica de programação**
- **Validação de entrada**


## EXERCÍCIO RESOLVIDO:

```python
import random

while True:
    print('Jogo da Adivinhação')
    print('Tente adivinha um número entre 1 e 100')
    print('Você tem 10 tentativas.')
    print('')
    
    numerosecreto = random.randint(1,100)

    ganhou = False
    for tentativa in range(10):
        palpite = int(input('Dê um palpite: '))
        print(f'Tentativa {tentativa+1}/10')
        if palpite > numerosecreto:
            print('Menos')
        elif palpite < numerosecreto:
            print('Mais')
        else:
            ganhou = True
            break

    if ganhou:
        print('GANHOU!!!')    
    else:
        print('PERDEU!!!')
    
    sair = input('Jogar novamente? S/N');
    if sair =='S':
        break




