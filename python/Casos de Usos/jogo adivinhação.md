### Caso de Uso: Jogo de Adivinhar Número

#### **Nome**: Jogo de Adivinhar Número

#### **Ator Principal**: Jogador

#### **Descrição**:  
O jogo sorteia um número aleatório dentro de um intervalo pré-definido e o jogador deve tentar adivinhar o número. Após cada tentativa, o sistema fornece feedback, informando se o palpite foi maior ou menor que o número correto. Quando o jogador acerta, o sistema o parabeniza e oferece a opção de jogar novamente ou encerrar o jogo.

#### **Pré-condições**:
- O sistema deve estar funcionando corretamente.
- O número desconhecido deve ser sorteado aleatoriamente no início do jogo.

#### **Fluxo Principal**:

1. O jogo sorteia um número aleatório dentro de um intervalo pré-definido (por exemplo, de 1 a 100).
2. O sistema solicita ao jogador que insira um número como palpite.
3. O jogador insere um número e confirma o palpite.
4. O sistema compara o palpite com o número sorteado:
   - **Se o número digitado for maior que o número sorteado**, o sistema exibe a mensagem: "Você chutou um número muito alto!".
   - **Se o número digitado for menor que o número sorteado**, o sistema exibe a mensagem: "Você chutou um número muito baixo!".
   - **Se o jogador acertar o número**, o sistema exibe a mensagem: "Parabéns, você acertou!".
5. Após o acerto, o sistema pergunta se o jogador deseja jogar novamente:
   - **Se o jogador escolher jogar novamente**, o sistema sorteia um novo número e o fluxo retorna ao passo 2.
   - **Se o jogador optar por não jogar novamente**, o sistema encerra o jogo.

#### **Fluxo Alternativo**:

- **Erro de entrada**:
   - Se o jogador inserir um valor que não seja um número válido, o sistema exibe a mensagem: "Entrada inválida! Digite um número válido." e solicita nova tentativa.

#### **Pós-condições**:
- O sistema deve terminar o jogo corretamente se o jogador optar por não jogar novamente.

---

Esse é um caso de uso simples e direto, com regras claras para a interação entre o sistema e o jogador. Ele pode ser implementado em várias linguagens de programação e adaptado para diferentes interfaces (console, web, gráfico).
