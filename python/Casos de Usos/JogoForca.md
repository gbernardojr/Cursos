### Caso de Uso: Jogo da Forca em Python (Ambiente de Prompt)

#### 1. **Título do Caso de Uso:**  
Desenvolvimento de Jogo da Forca (Ambiente de Prompt)

#### 2. **Objetivo:**  
Desenvolver um jogo da forca simples, utilizando listas, loops e condições básicas do Python, em um ambiente de prompt. O jogador tenta adivinhar uma palavra secreta por meio de letras, evitando que o boneco seja "enforcado" antes de completar a palavra.

#### 3. **Atores:**
- **Jogador:** Usuário que interage com o jogo, tentando adivinhar a palavra.
- **Sistema (Jogo da Forca):** Código Python que processa as entradas do jogador e controla o jogo.

#### 4. **Pré-condições:**
- O jogador precisa ter acesso a um ambiente onde possa rodar scripts Python.
- O sistema deve ter uma lista de palavras pré-definidas para serem usadas no jogo.

#### 5. **Descrição:**
1. O jogador inicia o jogo e uma palavra secreta é selecionada aleatoriamente pelo sistema a partir de uma lista.
2. O sistema exibe uma série de traços no prompt, representando as letras ocultas da palavra.
3. O jogador insere uma letra no prompt.
4. O sistema verifica se a letra está presente na palavra secreta:
   - Se a letra estiver correta, o sistema revela sua posição na palavra.
   - Se a letra estiver incorreta, o sistema registra um erro e atualiza o número de tentativas restantes.
5. O jogo continua até que:
   - O jogador adivinhe todas as letras da palavra, vencendo o jogo.
   - O jogador exceda o número máximo de erros permitidos, resultando em derrota.

#### 6. **Fluxo Principal:**
1. O jogador inicia o jogo.
2. O sistema seleciona uma palavra aleatória da lista.
3. O sistema exibe os traços no lugar das letras da palavra.
4. O jogador insere uma letra.
5. O sistema verifica se a letra está presente:
   - Se estiver correta, a letra é revelada.
   - Se estiver errada, o número de erros aumenta e o sistema exibe o número de tentativas restantes.
6. O fluxo se repete até que:
   - O jogador adivinhe a palavra (vitória).
   - O jogador cometa erros suficientes para perder (derrota).

#### 7. **Fluxo Alternativo:**
- Se o jogador inserir uma letra que já foi utilizada anteriormente, o sistema avisa que a letra já foi tentada e solicita outra entrada.

#### 8. **Pós-condições:**
- O sistema exibe uma mensagem indicando se o jogador venceu ou perdeu.
- O sistema oferece a opção de reiniciar o jogo ou finalizar.

#### 9. **Requisitos Funcionais:**
- O sistema deve possuir uma lista de palavras pré-definidas.
- O sistema deve registrar as letras corretas e incorretas tentadas pelo jogador.
- O sistema deve exibir o número de tentativas restantes a cada erro.
- O sistema deve permitir ao jogador ver o estado atual da palavra, com as letras adivinhadas e as restantes como traços.

#### 10. **Requisitos Não Funcionais:**
- O jogo deve ser simples e interativo, rodando de forma eficiente no prompt.
- A interface de entrada deve ser clara, exibindo as letras corretas e incorretas de forma simples e compreensível.

#### 11. **Exceções:**
- O sistema não deve aceitar entradas que não sejam letras (números ou símbolos devem ser ignorados).
- O sistema deve lidar com entradas repetidas (avisando o jogador e solicitando uma nova letra).

---

#### **Conclusão:**  
Este caso de uso descreve o fluxo básico de um jogo de forca rodando em ambiente de prompt, usando estruturas simples do Python como listas, loops e condicionais. O jogador pode interagir diretamente pelo terminal, e o sistema gerencia o progresso com base nas entradas fornecidas.
